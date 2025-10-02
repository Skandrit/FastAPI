from fastapi import HTTPException, status, FastAPI
from datetime import datetime
from typing import Dict
from blog.app.models.users import User, CreateUser, ChangeUserInfo, ResponseUser
from blog.app.validator.validation import validate_email, validate_password, validate_login


users_db: Dict[int, User] = {}
user_id_c = 1 #счетчик для айдишников у пользователей


async def create_user(user: CreateUser):

    if not validate_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Неверный формат почты"
        )

    if not validate_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пароль меньше 6 символов"
        )

    if not validate_login(user.login):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Логин должен быть от 3 до 20 символов"
        )

    for existing_user in users_db.values():
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Почта занята"
            )

    for existing_user in users_db.values():
        if existing_user.login == user.login:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Логин занят"
            )

    global user_id_c
    now = datetime.now()

    new_user = User(
        id=user_id_c,
        email=user.email,
        login=user.login,
        password=user.password,
        created_at=now,
        updated_at=now
    )

    users_db[user_id_c] = new_user
    user_id_c += 1

    return ResponseUser


async def get_user(user_id: int):

    if not users_db.get(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден"
        )

    return ResponseUser

async def update_user(user_id: int, user_update: ChangeUserInfo):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Поьзователь не найден")

    if not validate_email(user_update['email']):
        raise HTTPException(
            status_code=400,
            detail="Неверный формат почты"
        )

    if not validate_password(user_update['password']):
        raise HTTPException(
            status_code=400,
            detail="Пароль меньше 6 символов"
        )

    if not validate_login(user_update['login']):
        raise HTTPException(
            status_code=400,
            detail="Логин должен быть от 3 до 20 символов"
        )


    for field, value in user_update.items():
        setattr(user, field, value)
    user.updated_at = datetime.now()

    return ResponseUser


async def delete_user(user_id: int):

    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден"
        )

    del users_db[user_id]

    return {
        "message": "Пользователь удален",
        "user_id": user_id
    }

async def get_user_by_email(email: str):

    for user in users_db.values():
        if user.email == email:
            return ResponseUser

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Пользователь не найден"
    )