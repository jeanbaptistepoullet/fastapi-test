from .main import get_app

# DB_HOST=localhost DB_DATABASE=dbname DB_USER=jeanbaptistepoullet DB_PASSWORD=pbj poetry run uvicorn fastapi_test.main:app --reload

app = get_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}
 
 
# @app.post("/items/")
# async def create_item(item: Item):
#     return item
# 
# 
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item": item_id}
# 
# 
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}