from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.supplier import Supplier
from schemas.supplier import SupplierCreate

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.post("")
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):

    db_supplier = Supplier(
        supplier_name=supplier.supplier_name,
        email=supplier.email,
        phone=supplier.phone
    )

    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)

    return db_supplier


@router.get("")
def get_suppliers(
    db: Session = Depends(get_db)
):
    return db.query(Supplier).all()
