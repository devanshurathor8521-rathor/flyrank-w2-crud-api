from fastapi import Body, FastAPI, HTTPException

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
