from fastapi import APIRouter, Depends
from typing import List

from schemas.todo_schema import TodoDetails, TodoCreate
from api.dependencies.user_deps import get_current_user
from models.user_model import User
from models.todo_model import Todo
from services.todo_service import TodoService

todo_router = APIRouter()

@todo_router.get('/', summary='Lista todas as Notas.', response_model=List[TodoDetails])
async def find_all(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user)

@todo_router.post('/create', summary='Adiciona nova Nota', response_model=Todo)
async def create_todo(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(current_user, data)