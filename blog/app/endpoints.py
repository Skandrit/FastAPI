from fastapi import FastAPI
from CRUD.CRUD_post import create_post, update_post, delete_post, get_post
from models.Post import CreatePost, ChangePost, ResponsePost
from models.users import CreateUser, ChangeUserInfo, ResponseUser
from CRUD.CRUD_users import get_user, update_user, delete_user, get_user_by_email, create_user

app = FastAPI()

@app.post('/users/create', response_model=ResponseUser)
async def create_new_user1(user: CreateUser):
    return await create_user(user)

@app.get("/users/{user_id}")
async def get_user1(user_id:int, response_model=ResponseUser):
    return await get_user(user_id)

@app.put("/users/update/{user_id}", response_model=ResponseUser)
async def update_user1(user_id: int, change: ChangeUserInfo):
    return await update_user(user_id, change)
#
@app.delete("/users/delete/{user_id}")
async def delete_user1(user_id: int):
    return await delete_user(user_id)

@app.get("/users/get-by-email/{email}", response_model=ResponseUser)
async def get_user_by_email1(email: str):
    return await get_user_by_email(email)

@app.post("/posts/create", response_model=CreatePost)
async def create_post1(post: CreatePost, idd:int):
    return await create_post(post, idd)

@app.get("/post/{post_id}")
async def get_post1(post_id: int):
    return await get_post(post_id)

@app.put("/post/update/{post_id}", response_model=ResponsePost)
async def update_post1(post_id: int, change: ChangePost):
    return await update_post(post_id, change)

@app.delete("/post/delete/{post_id}")
async def delete_post1(post_id: int):
    return await delete_post(post_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)