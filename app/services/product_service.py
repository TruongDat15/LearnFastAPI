from sqlalchemy.orm import Session

from app.crud.product import (
    create_product,
    delete_product,
    get_product_by_barcode,
    get_product_by_id,
    get_products,
    update_product,
)
from app.models.product import Product


def _product_to_dict(product: Product):
    # Hàm dùng chung để chuẩn hóa dữ liệu trả về theo schema response.
    return {
        "id": product.id,
        "name": product.name,
        "barcode": product.barcode,
        "import_price": product.import_price,
        "sale_price": product.sale_price,
    }


def list_products(db: Session):
    # B1: Lấy danh sách từ tầng CRUD.
    products = get_products(db)

    # B2: Chuyển từng object ORM thành dict để route trả về dễ dàng.
    return [_product_to_dict(item) for item in products]


def get_product_detail(db: Session, product_id: int):
    # B1: Tìm sản phẩm theo id.
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    # B2: Trả dữ liệu nếu tìm thấy.
    return _product_to_dict(product)


def create_product_item(
    db: Session,
    name: str,
    barcode: str,
    import_price: float,
    sale_price: float,
):
    # B1: Kiểm tra barcode đã tồn tại để tránh trùng mã.
    existed_product = get_product_by_barcode(db, barcode)
    if existed_product:
        return None

    # B2: Tạo object Product mới từ dữ liệu đầu vào.
    new_product = Product(
        name=name,
        barcode=barcode,
        import_price=import_price,
        sale_price=sale_price,
    )

    # B3: Lưu dữ liệu xuống DB.
    saved_product = create_product(db, new_product)

    # B4: Trả dữ liệu chuẩn cho API response.
    return _product_to_dict(saved_product)


def update_product_item(
    db: Session,
    product_id: int,
    name: str,
    barcode: str,
    import_price: float,
    sale_price: float,
):
    # B1: Tìm sản phẩm cần cập nhật.
    product = get_product_by_id(db, product_id)
    if not product:
        return None

    # B2: Nếu đổi barcode, kiểm tra barcode mới có bị trùng không.
    barcode_owner = get_product_by_barcode(db, barcode)
    if barcode_owner and barcode_owner.id != product_id:
        return "barcode_exists"

    # B3: Gán lại từng trường dữ liệu.
    product.name = name
    product.barcode = barcode
    product.import_price = import_price
    product.sale_price = sale_price

    # B4: Lưu thay đổi và trả dữ liệu mới.
    updated_product = update_product(db, product)
    return _product_to_dict(updated_product)


def delete_product_item(db: Session, product_id: int):
    # B1: Kiểm tra sản phẩm có tồn tại không.
    product = get_product_by_id(db, product_id)
    if not product:
        return False

    # B2: Thực hiện xóa khỏi DB.
    delete_product(db, product)
    return True
