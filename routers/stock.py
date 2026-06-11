from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.product import Product
from models.stock import StockHistory
from schemas.stock import (
    StockInward,
    StockOutward
)

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)


@router.post("/inward")
def stock_inward(
    stock: StockInward,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == stock.product_id
    ).first()

    if not product:
        raise HTTPException(
            404,
            "Product not found"
        )

    product.stock_quantity += stock.quantity

    history = StockHistory(
        product_id=stock.product_id,
        movement_type="INWARD",
        quantity=stock.quantity
    )

    db.add(history)
    db.commit()

    return {"message": "Stock added"}


@router.post("/outward")
def stock_outward(
    stock: StockOutward,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == stock.product_id
    ).first()

    if not product:
        raise HTTPException(
            404,
            "Product not found"
        )

    if product.stock_quantity < stock.quantity:
        raise HTTPException(
            400,
            "Insufficient stock"
        )

    product.stock_quantity -= stock.quantity

    history = StockHistory(
        product_id=stock.product_id,
        movement_type="OUTWARD",
        quantity=stock.quantity
    )

    db.add(history)
    db.commit()

    return {"message": "Stock removed"}


@router.get("/history")
def stock_history(
    db: Session = Depends(get_db)
):
    return db.query(StockHistory).all()
