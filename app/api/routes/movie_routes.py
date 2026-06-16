from fastapi import APIRouter, HTTPException
from app.services.movie_service import (
    get_movies,
    get_movie,
    delete_movie,
    create_movie
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

@router.post("/")
async def add_movie(movie_data: dict):
    try:
        new_movie = create_movie(movie_data)
        return {"status": "success", "data": new_movie}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to add movie: {str(e)}")