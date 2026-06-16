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


def create_movie(movie_data: dict):
    db = SessionLocal()
    movie = Movie(
        title=movie_data.get("title"),
        genre=movie_data.get("genre"),
        duration=movie_data.get("duration"),
        poster=movie_data.get("poster"),
        description=movie_data.get("description"),
    )
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie