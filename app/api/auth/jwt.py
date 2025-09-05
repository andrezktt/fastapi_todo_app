from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from jose import jwt, JWTError, ExpiredSignatureError
from pydantic import ValidationError

from api.dependencies.user_deps import get_current_user
from core.config import settings
from core.security import create_access_token, create_refresh_token
from models.user_model import User
from schemas.auth_schema import TokenSchema, TokenPayload
from schemas.user_schema import UserDetail
from services.user_service import UserService

auth_router = APIRouter()

@auth_router.post('/login', summary='Cria um Access Token e um Refresh Token', response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(
        email=data.username,
        password=data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='E-mail ou Senha estão incorretos.'
        )
    return {
        'access_token': create_access_token(user.user_id),
        'refresh_token': create_refresh_token(user.user_id)
    }
    
@auth_router.post('/test-token', summary='Testando o Token', response_model=UserDetail)
async def test_token(user: User = Depends(get_current_user)):
    return user

@auth_router.post('/refresh', summary='Refresh Token', response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            token=refresh_token,
            key=settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token Expirado.',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    except(JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Erro na validação do Token.',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    user = await UserService.get_user_by_id(id=token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não foi possível encontrar o usuário.',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return {
        'access_token': create_access_token(user.user_id),
        'refresh_token': create_refresh_token(user.user_id)
    }