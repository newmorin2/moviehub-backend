from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate


def get_movies(db: Session):
    return db.query(Movie).all()


def add_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(**movie.model_dump())

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie


def update_movie(db: Session, movie_id: int, movie: MovieUpdate):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not db_movie:
        return None

    for key, value in movie.model_dump(exclude_unset=True).items():
        setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)

    return db_movie


def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not db_movie:
        return None

    db.delete(db_movie)
    db.commit()

    return {"message": "Movie deleted successfully"}