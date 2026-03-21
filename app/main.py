from fastapi import FastAPI
from app.database import Base, engine

from app.models import user

from app.api.auth import router as auth_router


# tạo tất cả các bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])