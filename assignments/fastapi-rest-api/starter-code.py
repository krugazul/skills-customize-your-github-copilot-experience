
# Starter code for FastAPI REST API assignment
# You can use this file to begin your FastAPI project

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example data model
class Item(BaseModel):
    name: str
    description: str = None

# Example in-memory storage
items = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# TODO: Add CRUD endpoints for your resource below
# Example:
# @app.post("/items/")
# def create_item(item: Item):
#     ...
