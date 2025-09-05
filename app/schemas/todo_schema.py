from typing import Optional
from pydantic import Field
from pydantic.v1 import BaseModel
from uuid import  UUID
from datetime import  datetime


class TodoCreate(BaseModel):
    title: str = Field(..., title='Título', min_length=1, max_length=50)
    description: str = Field(..., title='Descrição', min_length=1, max_length=150)
    status: Optional[bool] = False

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[bool] = False

class TodoDetails(BaseModel):
    todo_id: UUID
    status: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime