from sqlalchemy.orm import Session

from app.models.product import Product


def get_product_by_id(db: Session, product_id: int):
    # Lấy một sản phẩm theo id để phục vụ xem chi tiết/cập nhật/xóa.
    return db.query(Product).filter(Product.id == product_id).first()


def get_product_by_barcode(db: Session, barcode: str):
    # Lấy sản phẩm theo barcode để kiểm tra trùng dữ liệu.
    return db.query(Product).filter(Product.barcode == barcode).first()


def get_products(db: Session):
    # Lấy toàn bộ danh sách sản phẩm.
    return db.query(Product).all()


def create_product(db: Session, product: Product):
    # Lưu sản phẩm mới và refresh để lấy dữ liệu mới nhất từ DB.
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product: Product):
    # Commit thay đổi trên object sản phẩm hiện có.
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: Product):
    # Xóa sản phẩm khỏi DB và commit ngay.
    db.delete(product)
    db.commit()
