from fastapi import FastAPI

app = FastAPI(title="Task CRUD API")

@app.get("/")
def root():
    return {"message": "Hello, server is running"}
