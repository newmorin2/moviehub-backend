from fastapi import APIRouter, Depends
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/my-watchlist")
async def get_watchlist(user = Depends(get_current_user)):
    return {
        "status": "success",
        "message": f"Successfully authenticated as {user.get('email')}",
        "firebase_uid": user.get("uid")
    }