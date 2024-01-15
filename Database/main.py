from fastapi import FastAPI, Depends, HTTPException, Path, Request
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import models
from starlette import status
from models import Todos
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=50)
    priority: int = Field(gt=0, lt=6)
    completed: bool

@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    all_todos = db.query(Todos).all()
    return all_todos

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_one(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")


# Create a new todo
@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    
    todo_model = Todos(**todo_request.dict())
    print(todo_model)
    
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    
    return todo_model

# Update a todo
@app.put('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, 
                       todo_request: TodoRequest,
                       todo_id: int = Path(gt=0)):
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.completed = todo_request.completed
    
    db.add(todo_model)
    db.commit()
    
# Delete a todo
@app.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo_model)
    db.commit()
