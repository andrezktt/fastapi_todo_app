from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timezone
from pydantic import ValidationError

from core.config import settings
from models.user_model import User
from schemas.auth_schema import TokenPayload
from services.user_service import UserService

reusable_oauth = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/login',
    scheme_name='JWT',
)

async def get_current_user(token: str = Depends(reusable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITHM],
            options={'verify_aud': False}
        )
        token_data = TokenPayload(**payload)
        
        # if datetime.fromtimestamp(token_data.exp) < datetime.now(timezone.utc):
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED, 
        #         detail='Token expirado.', 
        #         headers={'WWW-Authenticate': 'Bearer'}
        #     )
    
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
    
    return user