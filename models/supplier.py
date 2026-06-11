from sqlalchemy import Column, Integer, String
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    supplier_name = Column(String)

    email = Column(
        String,
        unique=True
    )

    phone = Column(String)
