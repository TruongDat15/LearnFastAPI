from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import (
    create_product_item,
    delete_product_item,
    get_product_detail,
    list_products,
    update_product_item,
)

router = APIRouter()


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product_api(payload: ProductCreate, db: Session = Depends(get_db)):
    # B1: Gọi service để tạo sản phẩm mới.
    result = create_product_item(
        db=db,
        name=payload.name,
        barcode=payload.barcode,
        import_price=payload.import_price,
        sale_price=payload.sale_price,
    )

    # B2: Báo lỗi nếu barcode đã tồn tại.
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Barcode da ton tai",
        )

    # B3: Trả thông tin sản phẩm vừa tạo.
    return result


@router.get("", response_model=List[ProductResponse])
def list_products_api(db: Session = Depends(get_db)):
    # Lấy toàn bộ danh sách sản phẩm.
    return list_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_api(product_id: int, db: Session = Depends(get_db)):
    # B1: Lấy thông tin chi tiết sản phẩm theo id.
    result = get_product_detail(db, product_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Khong tim thay san pham",
        )

    # B2: Trả dữ liệu khi tìm thấy.
    return result


@router.put("/{product_id}", response_model=ProductResponse)
def update_product_api(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
):
    # B1: Gọi service để cập nhật dữ liệu sản phẩm.
    result = update_product_item(
        db=db,
        product_id=product_id,
        name=payload.name,
        barcode=payload.barcode,
        import_price=payload.import_price,
        sale_price=payload.sale_price,
    )

    # B2: Xử lý trường hợp barcode bị trùng.
    if result == "barcode_exists":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Barcode da ton tai",
        )

    # B3: Xử lý trường hợp không tìm thấy sản phẩm.
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Khong tim thay san pham",
        )

    # B4: Trả dữ liệu sau khi cập nhật thành công.
    return result


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_api(product_id: int, db: Session = Depends(get_db)):
    # B1: Thực hiện xóa sản phẩm theo id.
    deleted = delete_product_item(db, product_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Khong tim thay san pham",
        )

    # B2: Trả 204 khi xóa thành công.
    return Response(status_code=status.HTTP_204_NO_CONTENT)
