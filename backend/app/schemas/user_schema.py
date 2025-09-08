from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description='Email Usuário')
    username: str = Field(..., min_length=5, max_length=50, description='Username Usuário')
    password: str = Field(..., min_length=5, max_length=20, description='Password Usuário')
    
class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]