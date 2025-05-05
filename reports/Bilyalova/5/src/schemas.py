from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class SupplierBase(BaseModel):
    name: str
    contact: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierOut(SupplierBase):
    id: int
    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: float
    supplier_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    name: str
    email: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int
    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemOut(OrderItemBase):
    id: int
    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    customer_id: int

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderOut(OrderBase):
    id: int
    order_date: datetime
    items: List[OrderItemOut]

    class Config:
        orm_mode = True
