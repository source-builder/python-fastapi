# api_v1/__init__.py
from fastapi import APIRouter
from .UserController import app as v1_router

api_router = APIRouter()
api_router.include_router(v1_router, prefix="/v1")
