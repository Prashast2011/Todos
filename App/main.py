from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from . import db

app = FastAPI()
templates = Jinja2Templates("App/templates")
app.mount("/ui", StaticFiles(directory="ui"), name="ui")

@app.get("/todos")
def get_todos():
    return templates.TemplateResponse(
        "todos.html", {"todos": db.get_todos(), "add": False, "request": {}}
    )

@app.get("/todos/update/{todo_id}")
def update_todo(todo_id: int):
    db.update_todo(todo_id)
    return RedirectResponse("/todos")

@app.post("/todos/add")
def add_todo_task(todo: db.ToDo):
    return db.add_todos(todo)

@app.get("/todos/add")
def add_todo():
    return templates.TemplateResponse(
        "todos.html", {"todos.":db.get_todos(), "add": True, "request": {}}
    )

@app.get("/todos/delete/{todo_id}")
def delete_todo(todo_id:int):
    db.delete_todo(todo_id)
    return RedirectResponse ("/todos")