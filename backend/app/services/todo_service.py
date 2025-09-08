from uuid import UUID

from models.todo_model import Todo
from models.user_model import User
from schemas.todo_schema import TodoCreate, TodoDetails, TodoUpdate

from typing import List

class TodoService:

    @staticmethod
    async def list_todos(user: User) -> List[TodoDetails]:
        todos =  await Todo.find(Todo.owner.id == user.id).to_list()
        return [TodoDetails(**todo.dict()) for todo in todos]

    @staticmethod
    async def create_todo(user: User, data: TodoCreate) -> Todo:
        todo = Todo(**data.dict(), owner=user)
        return await todo.insert()

    @staticmethod
    async def find_by_id(user: User, todo_id: UUID):
        todo = await Todo.find_one(Todo.todo_id == todo_id, Todo.owner.id == user.id)
        return todo

    @staticmethod
    async def update_todo(user: User, todo_id: UUID, data: TodoUpdate):
        todo = await TodoService.find_by_id(user, todo_id)
        await todo.update({
            '$set': data.dict(exclude_unset=True)
        })
        await todo.save()
        return todo

    @staticmethod
    async def delete_todo(user: User, todo_id: UUID):
        todo = await TodoService.find_by_id(user, todo_id)
        if todo:
            await todo.delete()
        return None