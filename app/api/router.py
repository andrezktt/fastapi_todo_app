from fastapi import APIRouter
from api.handlers.user import user_router
from api.auth.jwt import auth_router

from api.handlers.todo import todo_router

router = APIRouter()

router.include_router(
    router=user_router, 
    prefix='/users', 
    tags=['users']
)

router.include_router(
    router=auth_router,
    prefix='/auth',
    tags=['auth']
)

router.include_router(
    router=todo_router,
    prefix='/todo',
    tags=['todo']
)

