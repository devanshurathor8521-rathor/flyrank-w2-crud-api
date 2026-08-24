from fastapi import FastAPI

app = FastAPI(
    title="Task CRUD API",
    description="A simple in-memory To-Do CRUD API for the FlyRank Week 2 assignment.",
)


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
