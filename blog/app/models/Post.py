from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

class CreatePost(BaseModel):
    title: str
    content: str

class ChangePost(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class ResponsePost(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime