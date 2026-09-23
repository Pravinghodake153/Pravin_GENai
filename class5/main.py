from fastapi import FastAPI
from pydantic import BaseModel
from time import perf_counter

app = FastAPI()


@app.middleware("http")
async def log_request_response_time(request, call_next):
    start_time = perf_counter()
    response = await call_next(request)
    elapsed_time = perf_counter() - start_time
    print(
        f"{request.method} {request.url.path} -> "
        f"{response.status_code} ({elapsed_time:.4f}s)"
    )
    return response


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}