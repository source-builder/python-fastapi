from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from source.service.UserService import *
from models import *

app = APIRouter(prefix='/user', tags=["v1/user"])


@app.get("/{id}", response_model=UserOutModel)
async def getUser(id: int):
    return await User.get(id=id)


@app.get("", response_model=list[UserOutModel])
async def getUserList():
    return await User.all().values("username")


@app.post("", response_model=UserOutModel)
async def saveUser(user: UserModel):
    u = await User.filter(username=user.username).first()
    if u is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user is not empty")
    return await User.create(**user.model_dump())


@app.put("/{id}", response_model=UserOutModel)
async def updateUser(id: int, user: UserModel):
    await User.filter(id=id).update(**user.model_dump())
    return {}


@app.patch("/{id}", response_model=UserOutModel)
async def modifyUser(id: int, user: UserModel):
    u = await User.get(id=id)
    for key, value in user.model_dump():
        setattr(u, key, value)
    return u


@app.delete("/{id}")
async def deleteUser(id: int):
    await User.filter(id=id).delete()
    return {}


@app.post("/token")
async def loginForAccessToken(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.filter(username=form_data.username).first()
    if user is None or user.password != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    accessToken = createAccessToken(data={"sub": form_data.username})
    return {"accessToken": accessToken, "tokenType": "bearer"}


@app.post("/info")
def userInfo(current_user: User = Depends(getCurrentUser)):
    return current_user
