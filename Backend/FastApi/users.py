from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1,name= "Jose", surname="Jimenez", age=20),
              User(id=2,name= "Joseph", surname="Jimenez", age=50),
              User(id=3,name= "Josh", surname="Jimenez", age=23)]

#path
@app.get("/users/{id}")
async def usersclass(id: int):
    return search_user(id)

#query
@app.get("/users/")
async def users(id: int):
    return search_user(id)

def search_user (id: int):
    users = filter(lambda u: u.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error" : "no se ha encontrado el usuario"}
    
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error" : "El usuario ya existe"}
    
    users_list.append(user)
    return user

found = False

@app.put("/user/")
async def user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id== user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error" : "No se ha actualizado el usuario"}
