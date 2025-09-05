from fastapi import APIRouter, Depends

from schemas.todo_schema import TodoDetails
from api.dependencies.user_deps import get_current_user
from models.user_model import User

todo_router = APIRouter()

@todo_router.get('/', summary='Lista todas as Notas.', response_model=TodoDetails)
async def find_all(current_user: User = Depends(get_current_user())):
    pass