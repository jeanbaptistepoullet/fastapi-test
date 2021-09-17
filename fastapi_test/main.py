# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from .models import db

import logging
from importlib.metadata import entry_points

logger = logging.getLogger(__name__)

def load_modules(app=None):
    for ep in entry_points()["fastapi_test.modules"]:
        logger.info("Loading module: %s", ep.name)
        mod = ep.load()
        if app:
            init_app = getattr(mod, "init_app", None)
            if init_app:
                init_app(app)


def get_app():
    app = FastAPI(title='My app')
    db.init_app(app)
    load_modules(app)
    return app

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
# 
# 
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