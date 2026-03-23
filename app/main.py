from fastapi import FastAPI

from app.api.v1.api import api_router
from app.db.base import Base
from app.db.session import engine
from app.models import user  # noqa: F401

app = FastAPI(title="FastAPI Learning Project")

# Gom toàn bộ router phiên bản v1 tại một nơi để dễ mở rộng.
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def health_check():
    # Endpoint kiểm tra nhanh trạng thái server.
    return {"message": "Server is running"}


@app.on_event("startup")
def on_startup():
    # Tạo bảng khi startup để tránh lỗi khi chỉ import module.
    Base.metadata.create_all(bind=engine)