from pydantic import BaseModel


class MovieCreate(BaseModel):
    title: str
    genre: str
    description: str
    release_year: int
    rating: float


class MovieUpdate(BaseModel):
    title: str | None = None
    genre: str | None = None
    description: str | None = None
    release_year: int | None = None
    rating: float | None = None


class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True