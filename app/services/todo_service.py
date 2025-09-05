from models.todo_model import Todo
from models.user_model import User
from schemas.todo_schema import TodoCreate, TodoDetails

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