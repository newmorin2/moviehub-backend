from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    duration = Column(String)
    poster = Column(String)
    description = Column(String)