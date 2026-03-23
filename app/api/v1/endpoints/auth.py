from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth_service import login_user

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    # Gọi service để tách business logic khỏi router.
    result = login_user(db, payload.email, payload.password)

    # Trả lỗi rõ ràng khi thông tin đăng nhập không hợp lệ.
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email hoặc mat khau khong dung",
        )

    return result
