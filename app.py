from flask import Flask, request


app = Flask(__name__)

todos_list = []

# Get all todos
@app.get("/todos")
def read_todos():
    return todos_list

# Create a todo
@app.post("/todos")
def create_todo():
    todos = request.json
    todos = todos["todos"]
    for todo in todos:
        todos_list.append(todo)
    return todos_list

# Get a todo
@app.get("/todos/<int:todo_id>")
def read_todo_by_id(todo_id):
    for todo in todos_list:
        if todo["id"] == todo_id:
             return todo
    return "Todo not found", 404

# Create a subtodo for a todo
@app.post("/todos/<int:todo_id>/subtodos")
def create_subtodo_for_todo_id(todo_id):
    req = request.json
    for todo in todos_list:
         if todo["id"] == todo_id:
             todo["subtodos"].append(req)
             return todo
    return "Todo not found", 404

# Get subtodo for a todo
@app.get("/todos/<int:todo_id>/subtodos")
def get_subtodo(todo_id):
     print("List", todos_list)
     for todo in todos_list:
         print("Todo", todo)
         if todo["id"] == todo_id:
             return todo["subtodos"]
         return "Todo not found", 404