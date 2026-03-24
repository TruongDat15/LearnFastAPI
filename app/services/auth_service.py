import base64

from sqlalchemy.orm import Session

from app.crud.user import create_user, get_user_by_email
from app.models.user import User


def _build_basic_token(user_id: int, email: str) -> str:
    # Tạo token giả lập từ user id + email để demo luồng đăng nhập.
    raw_value = f"{user_id}:{email}"
    encoded = base64.urlsafe_b64encode(raw_value.encode("utf-8"))
    return encoded.decode("utf-8")


def login_user(db: Session, email: str, password: str):
    # B1: Lấy user theo email.
    user = get_user_by_email(db, email)
    if not user:
        return None

    # B2: So khớp password plain text (mức cơ bản để học).
    if user.password != password:
        return None

    # B3: Trả dữ liệu theo schema response.
    return {
        "access_token": _build_basic_token(user.id, user.email),
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
        },
    }


def register_user(db: Session, email: str, password: str):
    # B1: Kiểm tra email đã tồn tại chưa.
    existed_user = get_user_by_email(db, email)
    if existed_user:
        return None

    # B2: Tạo object user mới từ dữ liệu request.
    # Lưu ý: Password hiện đang lưu plain text theo cấu trúc hiện tại.
    new_user = User(email=email, password=password)

    # B3: Lưu vào DB qua tầng CRUD để đồng nhất cách thao tác dữ liệu.
    saved_user = create_user(db, new_user)

    # B4: Trả dữ liệu đúng với schema RegisterResponse.
    return {
        "user": {
            "id": saved_user.id,
            "email": saved_user.email,
        }
    }
