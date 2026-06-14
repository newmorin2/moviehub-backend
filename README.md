
#  MovieHub Backend


FastAPI backend for a movie booking platform providing movie data, authentication, and booking management.

---

##  Features

- User authentication 
- Admin CRUD operations
- Database integration 
- CORS enabled for frontend
- Docker support

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite / PostgreSQL
- Uvicorn
- Pydantic

---

##  Installation
- pip install -r requirements.txt

## Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Running the server
- uvicorn app.main:app --reload