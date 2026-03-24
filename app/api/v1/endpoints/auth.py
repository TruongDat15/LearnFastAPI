from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.auth import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
)
from app.services.auth_service import login_user, register_user

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


@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    # B1: Gọi service đăng ký để tách business logic khỏi router.
    result = register_user(db, payload.email, payload.password)

    # B2: Báo lỗi rõ ràng khi email đã được sử dụng.
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email da ton tai",
        )

    # B3: Trả response khi tạo tài khoản thành công.
    return result
