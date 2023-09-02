from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel



router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1,name= "Jose", surname="Jimenez", age=20),
              User(id=2,name= "Joseph", surname="Jimenez", age=50),
              User(id=3,name= "Josh", surname="Jimenez", age=23)]

@router.get("/users/")
async def usersclass():
    return users_list

#path
@router.get("/user/{id}")
async def usersclass(id: int):
    return search_user(id)

#query
@router.get("/users/")
async def users(id: int):
    return search_user(id)

def search_user (id: int):
    users = filter(lambda u: u.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error" : "no se ha encontrado el usuario"}
    
@router.post("/user/",response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise  HTTPException(status_code=404, detail="El usuario ya existe")
    
    users_list.append(user)
    return user

found = False

@router.put("/user/")
async def user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id== user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error" : "No se ha actualizado el usuario"}

@router.delete("/user/{id}")
async def user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id== id:
            del users_list[index]
            found = True
    if not found:
            return {"error" : "No se ha eliminado el usuario"}