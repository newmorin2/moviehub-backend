from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    description = Column(String)
    release_year = Column(Integer)
    rating = Column(Float)