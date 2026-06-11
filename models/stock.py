from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from database import Base

from datetime import datetime


class StockHistory(Base):
    __tablename__ = "stock_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    movement_type = Column(String)

    quantity = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
