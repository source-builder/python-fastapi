from tortoise import fields
from tortoise.models import Model
from pydantic import BaseModel, Field


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
