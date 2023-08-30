from fastapi import APIRouter

from models import *

app = APIRouter()

@app.get("/user/{id}")
async def getUser(id: int):
    return await User.get(id=id)


@app.get("/user")
async def getUserList():
    return await User.all().values("name")


@app.post("/user")
async def saveUser(user: UserModel):
    return await User.create(**user.model_dump())


@app.put("/user/{id}")
async def updateUser(id: int, user: UserModel):
    await User.filter(id=id).update(**user.model_dump())
    return {}


@app.delete("/user/{id}")
async def deleteUser(id: int):
    await User.filter(id=id).delete()
    return {}
