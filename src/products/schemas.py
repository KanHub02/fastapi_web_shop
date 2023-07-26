from pydantic import BaseModel

from datetime import date


class ProductCategorySchema(BaseModel):
    id: int
    title: str
    description: str
    created_at: date
    updated_at: date
    is_deleted: bool


class ProductCategoryCreateSchema(BaseModel):
    title: str
    description: str


class ProductShema(BaseModel):
    id: int
    title: str
    description: str
    price: float
    product_category_id: int
    created_at: date
    updated_at: date
    is_deleted: bool


class ProductCreateSchema(BaseModel):
    title: str
    description: str
    price: float
    category: int


class ProductDetailSchema(BaseModel):
    title: str
    description: str
    price: float
    category: int
    
    
