# api_v1/__init__.py
from fastapi import APIRouter
from .UserController import app as user
from .OrgController import app as org

api_router = APIRouter()
api_router.include_router(user, prefix="/v1")
api_router.include_router(org, prefix="/v1")
