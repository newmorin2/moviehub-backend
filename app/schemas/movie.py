from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    genre: str
    duration: str
    poster: str
    description: str

class MovieCreate(MovieBase):
    pass

class MovieOut(MovieBase):
    id: int

    class Config:
        from_attributes = True