from fastapi import FastAPI
from source.service.SystemService import getEnv
from tortoise.contrib.fastapi import register_tortoise
from source.controller.v1 import api_router as api_v1_router
from source.controller.v2 import api_router as api_v2_router

app = FastAPI()
database_url = getEnv("DATABASE_URL")
port = int(getEnv("PORT"))

TORTOISE_ORM = {
    'connections': {
        "default": database_url
    },
    'apps': {
        'models': {
            'models': ['models', 'aerich.models'],
            'default_connection': 'default',
        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(api_v1_router, prefix="/api")
app.include_router(api_v2_router, prefix="/api")

openapi_schema = app.openapi()
openapi_schema["info"]["title"] = "API Docs"
openapi_schema["info"]["description"] = "API Description"
openapi_schema["info"]["version"] = "2.0"
app.openapi_schema = openapi_schema

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
