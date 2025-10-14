from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    login: str
    password: str
    created_at: datetime
    updated_at: datetime

class CreateUser(BaseModel):
    email: str
    login: str
    password: str

class ChangeUserInfo(BaseModel):
    email: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
#
class ResponseUser(BaseModel):
    id: int
    email: str
    login: str
    created_at: datetime
    updated_at: datetime