from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from source.service.UserService import *
from source.utils.Paging import *
from models import *

app = APIRouter(prefix='/user', tags=["v1/user"])


@app.get("/{id}", response_model=UserOutModel)
async def getUser(id: int):
    return await User.get(id=id)


@app.get("", response_model=list[UserOutModel])
async def getUserList():
    return await User.all().values("username")


@app.post("/page", response_model=list[UserOutModel])
async def getUserPageList(pageQuery: UserPageQuery = Depends(getUserQueryPage)):
    offset = pageQuery.offset
    limit = pageQuery.limit
    res = []
    if pageQuery.username is not '':
        res = await User.filter(username__icontains=pageQuery.username).offset(offset).limit(limit)
    else:
        res = await User.all().offset(offset).limit(limit)
    return res


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
    return user


@app.patch("/{id}", response_model=UserOutModel)
async def modifyUser(id: int, user: UserInModel):
    u = await User.get(id=id)
    if u.username != user.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="username cannot be modified")

    objs = user.model_dump(exclude={"username"})
    await User.filter(id=id).update(**objs)
    return await User.get(id=id)


@app.delete("/{id}")
async def deleteUser(id: int):
    await User.filter(id=id).delete()
    return {}


@app.post("/token")
async def loginForAccessToken(data: OAuth2PasswordRequestForm = Depends()):
    user = await User.filter(username=data.username).first()
    if user is None or user.password != data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    accessToken = createAccessToken(data={"sub": data.username})
    return {"accessToken": accessToken, "tokenType": "bearer"}


@app.post("/info")
def userInfo(currentUser: User = Depends(getCurrentUser)):
    return currentUser
