from fastapi import Query
from pydantic import BaseModel


class PageQuery(BaseModel):
    limit: int
    offset: int


def getPage(pageNum: int = Query(1, description="Page number"),
            pageSize: int = Query(10, description="Items per page")):
    limit = pageSize
    offset = (pageNum - 1) * pageSize
    return {"offset": offset, "limit": limit}
