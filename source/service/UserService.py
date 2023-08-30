from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from source.service.SystemService import getEnv
import jwt
from datetime import datetime, timedelta
from models import *

secret_key = getEnv("SECRET_KEY")

def createAccessToken(data: dict, expires_delta: timedelta = timedelta(hours=24)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")
    return encoded_jwt


async def getCurrentUser(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        username = payload.get('sub')
        user = await User.filter(username=username).first()
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token has expired")
    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token decode error")
