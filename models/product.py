from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String)

    sku = Column(
        String,
        unique=True
    )

    category = Column(String)

    price = Column(Float)

    stock_quantity = Column(
        Integer,
        default=0
    )
