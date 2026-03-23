from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_email(db: Session, email: str):
    # Truy vấn user theo email để phục vụ đăng nhập.
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user):
    # Lưu user mới và trả lại object sau khi refresh.
    db.add(user)
    db.commit()
    db.refresh(user)
    return user