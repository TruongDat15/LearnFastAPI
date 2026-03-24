from pydantic import BaseModel


class ProductBase(BaseModel):
    # Nhóm thuộc tính chung của sản phẩm để tái sử dụng.
    name: str
    barcode: str
    import_price: float
    sale_price: float


class ProductCreate(ProductBase):
    # Schema tạo mới kế thừa toàn bộ trường cơ bản.
    pass


class ProductUpdate(ProductBase):
    # Schema cập nhật giữ đơn giản: yêu cầu truyền đủ trường.
    pass


class ProductResponse(ProductBase):
    # Response trả thêm id của sản phẩm đã lưu.
    id: int
