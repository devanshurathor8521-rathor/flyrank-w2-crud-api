from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI(
    title="Task CRUD API",
    description="A simple in-memory To-Do CRUD API for the FlyRank Week 2 assignment.",
)


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build CRUD endpoints", "done": False},
    {"id": 3, "title": "Test the API", "done": True},
]


@app.get("/", summary="API information")
def root():
    return {
        "name": "Task API",
        "description": "A simple in-memory To-Do CRUD API",
        "endpoints": ["/tasks"],
    }


@app.get("/health", summary="Health check")
def health():
    return {"status": "ok"}


@app.get("/tasks", summary="List all tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", summary="Get one task")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.post("/tasks", status_code=201, summary="Create a new task")
def create_task(body: dict = Body(default={} )):
    title = body.get("title")
    if not isinstance(title, str) or not title.strip():
        raise HTTPException(status_code=400, detail="title is required")

    next_id = max((task["id"] for task in tasks), default=0) + 1
    task = {"id": next_id, "title": title.strip(), "done": False}
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, body: dict = Body(default={} )):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    if not body:
        raise HTTPException(status_code=400, detail="Request body cannot be empty")

    if "title" in body:
        if not isinstance(body["title"], str) or not body["title"].strip():
            raise HTTPException(status_code=400, detail="title must not be empty")
        task["title"] = body["title"].strip()

    if "done" in body:
        if not isinstance(body["done"], bool):
            raise HTTPException(status_code=400, detail="done must be a boolean")
        task["done"] = body["done"]

    return task


@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
