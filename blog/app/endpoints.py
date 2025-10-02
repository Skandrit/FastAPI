from fastapi import FastAPI
from blog.app.CRUD.CRUD_post import create_post, update_post, delete_post
from blog.app.models.Post import CreatePost, ChangePost
from blog.app.models.users import CreateUser, ChangeUserInfo
from blog.app.CRUD.CRUD_users import get_user, update_user, delete_user, get_user_by_email

app = FastAPI()

@app.post('/{user}', response_model=CreateUser)
async def create_new_user1(user: CreateUser):
    return create_new_user1(user)

@app.get("/{user_id}")
async def get_user1(user_id:int):
    return get_user(user_id)

@app.put("/{user_id}", response_model=ChangeUserInfo)
async def update_user1(user_id: int, change:ChangeUserInfo):
    return update_user(user_id, change)

@app.delete("/{user_id}")
async def delete_user1(user_id: int):
    return delete_user(user_id)

@app.get("email/{email}")
async def get_user_by_email1(email: str):
    return get_user_by_email(email)

@app.post("/post/post", response_model=CreatePost)
async def create_post1(post: CreatePost, idd:int):
    return create_post(post, idd)

@app.get("/{post_id}")
async def get_post1(post_id: int):
    return get_user(post_id)

@app.put("/{post_id}", response_model=ChangePost)
async def update_post1(post_id: int, change:ChangePost):
    return update_post(post_id, change)

@app.delete("/delete/{post_id}")
async def delete_post1(post_id: int):
    return delete_post(post_id)