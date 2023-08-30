from tortoise.contrib.fastapi import register_tortoise
from source.controller.v2 import api_router as api_v2_router
from source.controller.v1 import api_router as api_v1_router
import fastapi
import os
from dotenv import main
main.load_dotenv()


app = fastapi.FastAPI()

database_url = os.getenv("DATABASE_URL")
port = int(os.getenv("PORT"))

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

app.include_router(api_v1_router, prefix="/api", tags=["v1"])
app.include_router(api_v2_router, prefix="/api", tags=["v2"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
