from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.movie_routes import router as movie_router

app = FastAPI(title="MovieHub API", version="1.0.0")

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_router)

@app.get("/")
def root():
    return {"message": "MovieHub API is running"}