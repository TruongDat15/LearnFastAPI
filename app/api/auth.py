from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.services.user_service import login_user
from app.api.deps import get_db

router = APIRouter()

@router.get("/test")
async def test(db: Session = Depends(get_db)):
    return {"message": "Hello World"}

@router.post("/login")
def login(username: UserLogin, db: Session = Depends(get_db)):
    result = login_user(db, username.username, username.password)
    if not result:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful", "user": result}