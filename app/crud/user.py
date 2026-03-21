from sqlalchemy.orm import Session
from app.models.user import User

def get_userByUsername(db: Session, username: str):
    return db.query(User).filter(User.email == username).first()

def create_user(db: Session, user):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user