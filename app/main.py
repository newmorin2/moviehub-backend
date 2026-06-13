from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.movie import Movie
from app.api.routes.movie_routes import router as movie_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MovieHub API",
    version="1.0.0"
)

app.include_router(movie_router)


@app.get("/")
def root():
    return {
        "message": "MovieHub API is running"
    }