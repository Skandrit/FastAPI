from fastapi import HTTPException
from datetime import datetime
from typing import Dict
from models.Post import Post, CreatePost, ChangePost, ResponsePost
from validator.validation import validate_post_title, validate_post_content
from CRUD.CRUD_users import users_db


posts_db: Dict[int, Post] = {}
post_id_c = 1

async def create_post(post: CreatePost, author_id: int):
    if author_id not in users_db:
        raise HTTPException(
            status_code=404,
            detail="Автор не найден"
        )

    if not validate_post_title(post.title):
        raise HTTPException(
            status_code=400,
            detail="заголовок должен быть меньше 50 символов"
        )

    if not validate_post_content(post.content):
        raise HTTPException(
            status_code=400,
            detail="Текст должен быть от 1 до 200 символов"
        )

    global post_id_c
    now = datetime.now()

    new_post = Post(
        id=post_id_c,
        author_id=author_id,
        title=post.title,
        content=post.content,
        created_at=now,
        updated_at=now
    )

    posts_db[post_id_c] = new_post
    post_id_c += 1

    return "Пост добавлен"


async def get_post(post_id: int):
    post = posts_db.get(post_id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="Пост не найден"
        )
    return ResponsePost

async def update_post(post_id: int, post_update: ChangePost):
    post = posts_db.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if not validate_post_title(post_update['content']):
        raise HTTPException(
            status_code=400,
            detail="заголовок должен быть меньше 50 символов"
        )

    if not validate_post_content(post_update['content']):
        raise HTTPException(
            status_code=400,
            detail="Текст должен быть от 1 до 200 символов"
        )

    for field, value in post_update.items():
        setattr(post, field, value)
    post.updated_at = datetime.now()

    return ResponsePost


async def delete_post(post_id: int):
    if post_id not in posts_db:
        raise HTTPException(
            status_code=404,
            detail="Пост не найден"
        )

    del posts_db[post_id]
    return {"message": "Пост удален"}