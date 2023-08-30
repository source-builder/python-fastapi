from tortoise import fields
from tortoise.models import Model
from pydantic import BaseModel, Field


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()


class UserModel(BaseModel):
    name: str = Field(..., description="The name is required")
