from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.models.movie import Movie
from app.api.routes.movie_routes import router as movie_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MovieHub API",
    version="1.0.0"
)

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_router)

@app.get("/")
def root():
    return {
        "message": "MovieHub API is running"
    }