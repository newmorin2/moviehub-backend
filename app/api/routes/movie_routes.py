from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate
from app.services.movie_service import (
    get_movies,
    add_movie,
    update_movie,
    delete_movie,
)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)


@router.get("/")
def movie_list(db: Session = Depends(get_db)):
    return get_movies(db)


@router.get("/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return movie


@router.post("/")
def create_movie(
    movie: MovieCreate,
    db: Session = Depends(get_db)
):
    return add_movie(db, movie)


@router.put("/{movie_id}")
def edit_movie(
    movie_id: int,
    movie: MovieUpdate,
    db: Session = Depends(get_db)
):
    updated_movie = update_movie(
        db,
        movie_id,
        movie
    )

    if not updated_movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return updated_movie


@router.delete("/{movie_id}")
def remove_movie(
    movie_id: int,
    db: Session = Depends(get_db)
):
    deleted_movie = delete_movie(
        db,
        movie_id
    )

    if not deleted_movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return deleted_movie