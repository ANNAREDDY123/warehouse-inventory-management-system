from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    product_name: str
    sku: str
    category: str

    price: float = Field(
        gt=0
    )

    stock_quantity: int = Field(
        ge=0
    )


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True
