from fastapi import APIRouter

app = APIRouter()

@app.get("/user")
def getUser():
    return [{"item": "item_a"}, {"item": "item_b"}]
