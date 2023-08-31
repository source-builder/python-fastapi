from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from source.service.UserService import *
from models import *

app = APIRouter()


@app.get("/user/{id}", response_model=UserOutModel)
async def getUser(id: int):
    return await User.get(id=id)


@app.get("/user", response_model=list[UserOutModel])
async def getUserList():
    return await User.all().values("username")


@app.post("/user", response_model=UserOutModel)
async def saveUser(user: UserModel):
    u = await User.filter(username=user.username).first()
    if u is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user is not empty")
    return await User.create(**user.model_dump())


@app.put("/user/{id}")
async def updateUser(id: int, user: UserModel):
    await User.filter(id=id).update(**user.model_dump())
    return {}


@app.delete("/user/{id}")
async def deleteUser(id: int):
    await User.filter(id=id).delete()
    return {}


@app.post("/user/token")
async def loginForAccessToken(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.filter(username=form_data.username).first()
    if user is None or user.password != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = createAccessToken(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/user/info")
def userInfo(current_user: User = Depends(getCurrentUser)):
    return current_user
