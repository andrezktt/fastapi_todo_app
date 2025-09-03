from fastapi import APIRouter
from api.handlers.user import user_router

router = APIRouter()

router.include_router(
    router=user_router, 
    prefix='/users', 
    tags=['users']
)

