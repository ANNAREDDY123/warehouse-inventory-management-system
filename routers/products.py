from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.product import Product
from schemas.product import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Product).filter(
        Product.sku == product.sku
    ).first()

    if existing:
        raise HTTPException(
            400,
            "SKU already exists"
        )

    db_product = Product(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@router.get("")
def get_products(
    db: Session = Depends(get_db)
):
    return db.query(Product).all()


@router.get("/{id}")
def get_product(
    id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == id
    ).first()

    if not product:
        raise HTTPException(
            404,
            "Product not found"
        )

    return product


@router.put("/{id}")
def update_product(
    id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    db_product = db.query(Product).filter(
        Product.id == id
    ).first()

    if not db_product:
        raise HTTPException(
            404,
            "Product not found"
        )

    db_product.product_name = product.product_name
    db_product.sku = product.sku
    db_product.category = product.category
    db_product.price = product.price
    db_product.stock_quantity = product.stock_quantity

    db.commit()

    return {"message": "Product updated"}


@router.delete("/{id}")
def delete_product(
    id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == id
    ).first()

    if not product:
        raise HTTPException(
            404,
            "Product not found"
        )

    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}
