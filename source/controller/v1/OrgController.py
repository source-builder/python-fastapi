from fastapi import APIRouter

app = APIRouter(prefix="/org", tags=["v1/org"])


@app.get("")
def getOrg():
    return [{"item": "item_a"}, {"item": "item_b"}]
