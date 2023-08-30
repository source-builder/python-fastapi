FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir fastapi \
    uvicorn \
    tortoise-orm \
    pydantic \
    aerich \
    asyncpg \
    python-dotenv

CMD ["python", "/app/main.py"]