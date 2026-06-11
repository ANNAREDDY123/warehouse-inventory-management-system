from pydantic import BaseModel, EmailStr


class SupplierCreate(BaseModel):
    supplier_name: str
    email: EmailStr
    phone: str


class SupplierResponse(SupplierCreate):
    id: int

    class Config:
        from_attributes = True
