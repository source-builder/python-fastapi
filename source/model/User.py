from fastapi import Query
from tortoise import fields
from tortoise.models import Model
from pydantic import BaseModel, Field
from source.utils.Paging import PageQuery, getPage


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.TextField()
    password = fields.TextField()


class UserModel(BaseModel):
    username: str = Field(..., description="the username is required")
    password: str = Field(..., description="the password is required")


class UserInModel(BaseModel):
    username: str = None
    password: str = None


class UserOutModel(BaseModel):
    username: str
    password: str = None


class UserPageQuery(PageQuery):
    username: str = None


def getUserQueryPage(
    username: str =  Query('', description="username"),
    pageNum: int = Query(1, description="Page number"),
    pageSize: int = Query(10, description="Items per page"),
):
    page = getPage(pageNum, pageSize)
    return UserPageQuery(offset=page['offset'], limit=page['limit'], username=username)
