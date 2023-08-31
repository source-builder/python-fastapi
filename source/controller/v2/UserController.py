from fastapi import APIRouter

app = APIRouter(prefix="/user")

@app.get("")
def getUser():

    return [{"item": "item_a"}, {"item": "item_b"}]
