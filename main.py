
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mini Task API")

# Model untuk validasi data task
class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


# Database sementara (disimpan di RAM)
tasks = []
next_id = 1


# GET: Halaman utama
@app.get("/")
def home():
    return {"message": "Welcome to Mini Task API"}


# GET: Mengambil semua task
@app.get("/tasks")
def get_tasks():
    return tasks


# GET: Mengambil satu task berdasarkan ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# POST: Membuat task baru
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task_data.title,
        "completed": task_data.completed
    }

    tasks.append(new_task)
    next_id += 1

    return new_task


# PUT: Memperbarui task berdasarkan ID
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            update_data = task_data.model_dump(exclude_unset=True)
            task.update(update_data)
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# DELETE: Menghapus task berdasarkan ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(index)
            return {
                "message": "Task deleted successfully",
                "task": deleted_task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
