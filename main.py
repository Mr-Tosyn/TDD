from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"id": item_id, "name": "Item One", "desscription": "This is item one"}