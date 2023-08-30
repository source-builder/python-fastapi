# python-fastapi

### install dependencies
```
pip install fastapi
pip install uvicorn
pip install tortoise-orm
pip install pydantic
pip install aerich
pip install asyncpg
pip install python-dotenv
```


### migrations config
```
aerich init -t {fileName}.TORTOISE_ORM   #TORTOISE_ORM配置的位置
```


### initialize database
```
aerich init-db
```


### dev run
```
python main.py
```


### deploy
**change the database connect string to the docker service name:** 

*postgresql://username:password@{service}:port/database*

```
docker-compose up -d
```