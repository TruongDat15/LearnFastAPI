from sqlalchemy.orm import Session
from app.crud import user as user_crud

def login_user(db: Session, username: str, password: str):
    user = user_crud.get_userByUsername(db, username)
    if user and user.password == password:
        return user
    return None