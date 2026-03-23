from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Tạo engine từ cấu hình tập trung.
engine = create_engine(settings.DATABASE_URL)

# Tạo factory để cấp session cho mỗi request.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
