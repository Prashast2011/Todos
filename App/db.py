from pydantic.main import BaseModel

class ToDo(BaseModel):
    id: int
    todo: str
    is_completed: bool = False

TODOS = [
    ToDo(id=1, todo="First Sample Task"),
    ToDo(id=2, todo="Second Sample Task"),
    ToDo(id=3, todo="Third Sample Task"),
    ToDo(id=4, todo="Fourth Sample Task"),
]
EMPTY_TODO = ToDo(id=-1, todo="")

def get_todos():
    return TODOS

def get_todo(todo_id: int):
    for todo in TODOS:
        if todo.id == todo_id:
            return todo
    return EMPTY_TODO

def get_next_id(todos:list):
    if todos:
        return todos[-1].id + 1
    else:
        return 1

def add_todos(todo:ToDo):
    todo.id = get_next_id(TODOS)
    TODOS.append(todo)

def update_todo(todo_id: int):
    db_todo = get_todo(todo_id)
    if db_todo != EMPTY_TODO:
        db_todo.is_completed =  not db_todo.is_completed
        return True

def delete_todos(todo:ToDo):
    todo.id = get_next_id(TODOS)
    TODOS.append(todo)

def delete_todo(todo_id: int):
    db_todo = get_todo(todo_id)
    if db_todo != EMPTY_TODO:
        TODOS.remove(db_todo)
        return True
    else:
        return False

