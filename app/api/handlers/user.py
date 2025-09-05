from fastapi import APIRouter, HTTPException, status, Depends
import pymongo

from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService
from api.dependencies.user_deps import get_current_user
from models.user_model import User

user_router = APIRouter()

@user_router.post('/create', summary='Cria um novo usuário', response_model=UserDetail)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='O username ou email deste usuário já existe.'
        )

@user_router.get('/me', summary='Detalhes do usuário logado.', response_model=UserDetail)
async def get_me(user: User = Depends(get_current_user)):
    return user