# API Test Results

The CRUD API was verified against the implementation in `main.py` using local HTTP requests.

| Test | Expected | Result |
|---|---:|---:|
| `GET /` | 200 | 200 |
| `GET /health` | 200 | 200 |
| `GET /tasks` | 200 | 200 |
| `GET /tasks/1` | 200 | 200 |
| `GET /tasks/99` | 404 | 404 |
| `POST /tasks` | 201 | 201 |
| Invalid `POST /tasks` | 400 | 400 |
| `PUT /tasks/1` | 200 | 200 |
| `PUT /tasks/99` | 404 | 404 |
| `DELETE /tasks/1` | 204 | 204 |
| `DELETE /tasks/99` | 404 | 404 |

The expected CRUD status-code behavior is implemented and verified. The Swagger UI screenshot required for the final assignment submission still needs to be captured from `http://localhost:8000/docs` in the user's local browser and added to the repository/README.
