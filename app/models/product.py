from sqlalchemy import Column, Float, Integer, String

from app.db.base import Base


class Product(Base):
    # Khai báo tên bảng sản phẩm trong database.
    __tablename__ = "products"

    # Khóa chính tự tăng để định danh mỗi sản phẩm.
    id = Column(Integer, primary_key=True, index=True)

    # Tên sản phẩm để hiển thị cho người dùng.
    name = Column(String(150), nullable=False)

    # Barcode dùng để tra cứu nhanh, đặt unique để tránh trùng mã.
    barcode = Column(String(100), unique=True, index=True, nullable=False)

    # Giá nhập và giá bán dùng kiểu số thực cho dễ học tập.
    import_price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)

