# api_v2/__init__.py
from fastapi import APIRouter
from .UserController import app as v2_router

api_router = APIRouter()
api_router.include_router(v2_router, prefix="/v2")
