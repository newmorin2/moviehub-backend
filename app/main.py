from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.movie_routes import router as movie_router
from app.api.endpoints import router as api_router
from app.core.auth import initialize_firebase
from contextlib import asynccontextmanager

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_firebase()
    yield

app = FastAPI(title="MovieHub API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_router)
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the MovieHub API backend!"}
