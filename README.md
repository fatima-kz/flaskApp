# flaskApp# Flask Lab Project

## Team roles (simulated)
- Member 1 (Backend Lead): implemented Flask routes (`/`, `/health`, `/data`) — Fatima (you)
- Member 2 (Frontend/API Integration): templates/static (placeholder)
- Member 3 (DevOps): Dockerfile, tests, GitHub Actions pipeline

## How to build & run locally
1. Clone repo
2. `cd main`
3. Create venv: `python -m venv .venv && source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python app.py`
6. Open http://localhost:5000

## How to run tests
```bash
cd main
pytest -q
