from fastapi import FastAPI

from database import engine, Base

from models.user import User
from models.product import Product
from models.supplier import Supplier
from models.stock import StockHistory

from routers.auth import router as auth_router
from routers.products import router as product_router
from routers.suppliers import router as supplier_router
from routers.stock import router as stock_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Warehouse Inventory Management System"
)

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(stock_router)
