from fastapi import APIRouter, Depends
from typing import List
from uuid import UUID

from schemas.todo_schema import TodoDetails, TodoCreate, TodoUpdate
from api.dependencies.user_deps import get_current_user
from models.user_model import User
from models.todo_model import Todo
from services.todo_service import TodoService

todo_router = APIRouter()

# Create
@todo_router.post('/create', summary='Adiciona nova Nota', response_model=Todo)
async def create_todo(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(current_user, data)

# Retrieve
@todo_router.get('/', summary='Lista todas as Notas.', response_model=List[TodoDetails])
async def find_all(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user)

@todo_router.get('/{todo_id}', summary='Busca os Detalhes pelo ID da Nota', response_model=TodoDetails)
async def find_by_id(todo_id: UUID, current_user: User = Depends(get_current_user)):
    return await TodoService.find_by_id(user=current_user, todo_id=todo_id)

# Update
@todo_router.put('/{todo_id}', summary='Atualiza os dados da Nota', response_model=TodoDetails)
async def update_todo(todo_id: UUID, data: TodoUpdate, current_user: User = Depends(get_current_user)):
    return await TodoService.update_todo(user=current_user, todo_id=todo_id, data=data)

# Delete
@todo_router.delete('/{todo_id}', summary='Exclusão de Nota')
async def delete_todo(todo_id: UUID, current_user: User = Depends(get_current_user)):
    await TodoService.delete_todo(user=current_user, todo_id=todo_id)
    return None