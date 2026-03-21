from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔹 tách config DB
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "usersdb"

# 🔹 build lại URL
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 🔹 tạo engine
engine = create_engine(DATABASE_URL)

# 🔹 tạo session
SessionLocal = sessionmaker(bind=engine)

# 🔹 base cho models
Base = declarative_base()