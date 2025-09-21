# FastAPI REST API with JWT Auth


This is a small FastAPI service with three endpoints and JWT-based auth.


## Quickstart (SQLite)


```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload