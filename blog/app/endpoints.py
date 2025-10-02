from fastapi import FastAPI

from blog.app.models.Post import CreatePost, ChangePost
from blog.app.models.users import CreateUser, ChangeUserInfo, ResponseUser
from blog.app.CRUD.CRUD_users import get_user

app = FastAPI()

@app.post('/{user}')
async def create_new_user(user: CreateUser):
    return ResponseUser

@app.get("/{user_id}")
async def get_user(user_id:int):
    return get_user(user_id)

@app.put("/{user_id}")
async def update_user(user_id: int, user_update: ChangeUserInfo):
    return update_user(user_id)

@app.delete("/{user_id}")
async def delete_user(user_id: int):
    return delete_user(user_id)

@app.get("email/{email}")
async def get_user_by_email(email: str):
    return get_user_by_email(email)

@app.post("/post/post")
async def create_post(post: CreatePost, author_id: int):
    return create_post(post)

@app.get("/{post_id}")
async def get_post(post_id: int):
    return get_user(post_id)

@app.put("/{post_id}")
async def update_post(post_id: int, post_update: ChangePost):
    return update_post(post_id)

@app.delete("/delete/{post_id}")
async def delete_post(post_id: int):
    return delete_post(post_id)






