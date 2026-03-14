from fastapi import APIRouter
from backend.main import app

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CookBot API working"}

app.include_router(router)
