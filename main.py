from fastapi import FastAPI

app = FastAPI(title="mini API")

@app.get("/")
def home():
    return {
        "massage": "Mini API by orvexaa Is running!",
        "version" : "1.0.0",
        "status" : "success"
    }

tasks = [
    {'id': 1 , "title": "Belajar Python", "completed": False},
    {'id': 2 , "title": "Membuat Mini API", "completed": False}
]

@app.get("/tasks")
def get_tasks():
    return {
        "total": len(tasks),
        "data": tasks
    }