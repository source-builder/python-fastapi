from fastapi import Query
from pydantic import BaseModel, Field
from tortoise import fields
from tortoise.models import Model

from source.utils.Paging import PageQuery, getPage


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.TextField()
    password = fields.TextField()
    createdAt = fields.DatetimeField(auto_now_add=True)
    updatedAt = fields.DatetimeField(auto_now=True)


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
    username: str = Query('', description="parameter username"),
    pageNum: int = Query(1, description="page number"),
    pageSize: int = Query(10, description="items per page"),
):
    page = getPage(pageNum, pageSize)
    return UserPageQuery(offset=page['offset'], limit=page['limit'], username=username)
