from fastapi import APIRouter, Depends
from typing import List
from uuid import UUID

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

@todo_router.get('/{todo_id}', summary='Busca os Detalhes pelo ID da Nota', response_model=TodoDetails)
async def find_by_id(todo_id: UUID, current_user: User = Depends(get_current_user)):
    return await TodoService.find_by_id(user=current_user, todo_id=todo_id)