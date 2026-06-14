from fastapi import APIRouter, Depends
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/my-watchlist")
async def get_watchlist(user = Depends(get_current_user)):
   
    return {"message": f"Welcome back, user {user['uid']}"}