from fastapi import APIRouter, HTTPException
from app.services.movie_service import (
    get_movies,
    get_movie,
    delete_movie
)

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/")
def fetch_movies():
    return get_movies()


@router.get("/{movie_id}")
def fetch_movie(movie_id: int):
    movie = get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.delete("/{movie_id}")
def remove_movie(movie_id: int):
    deleted = delete_movie(movie_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")

    return {"message": "Movie deleted successfully"}