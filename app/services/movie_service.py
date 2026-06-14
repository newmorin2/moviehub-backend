from app.models.movie import Movie
from app.core.database import SessionLocal

def get_movies():
    db = SessionLocal()
    return db.query(Movie).all()

def get_movie(movie_id: int):
    db = SessionLocal()
    return db.query(Movie).filter(Movie.id == movie_id).first()

def delete_movie(movie_id: int):
    db = SessionLocal()

    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        return False

    db.delete(movie)
    db.commit()

    return True