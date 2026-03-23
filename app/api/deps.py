from app.db.session import SessionLocal

def get_db():
    # Mỗi request dùng 1 session và luôn đóng sau khi xử lý.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()