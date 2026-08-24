# FlyRank W2 - Task CRUD API

A small in-memory To-Do CRUD API built with Python and FastAPI for the FlyRank Week 2 Backend AI Engineering assignment.

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- In-memory Python list (no database)

## Project Structure

```text
flyrank-w2-crud-api/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

Clone the repository and open the project folder:

```bash
git clone https://github.com/devanshurathor8521-rathor/flyrank-w2-crud-api.git
cd flyrank-w2-crud-api
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

The API will be available at:

- http://localhost:8000/
- http://localhost:8000/health
- http://localhost:8000/tasks
- http://localhost:8000/docs

## API Endpoints

| CRUD operation | Method | Endpoint | Success status |
|---|---|---|---|
| Root | GET | `/` | 200 |
| Health | GET | `/health` | 200 |
| Read all | GET | `/tasks` | 200 |
| Read one | GET | `/tasks/{id}` | 200 |
| Create | POST | `/tasks` | 201 |
| Update | PUT | `/tasks/{id}` | 200 |
| Delete | DELETE | `/tasks/{id}` | 204 |

Unknown task IDs return `404`. Invalid POST/PUT bodies return `400` with a JSON error message.

## Example Requests

Create a task:

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{\"title\":\"Buy milk\"}"
```

Expected response shape:

```text
HTTP/1.1 201 Created

{"id":4,"title":"Buy milk","done":false}
```

Get all tasks:

```bash
curl -i http://localhost:8000/tasks
```

Update a task:

```bash
curl -i -X PUT http://localhost:8000/tasks/1 -H "Content-Type: application/json" -d "{\"done\":true}"
```

Delete a task:

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

## Swagger UI

FastAPI automatically generates interactive API documentation at:

`http://localhost:8000/docs`

For the assignment submission, test the complete CRUD cycle in Swagger and add a screenshot of the `/docs` page to this README.

## CRUD Cycle

Create → Read → Update → Delete → Read again.

## Notes

- Data is stored only in memory and resets whenever the server restarts.
- No database or external storage is used.
- The API follows the status-code requirements from the assignment.
