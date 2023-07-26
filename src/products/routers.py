from typing import Annotated

from fastapi import APIRouter, Depends

from src.products.schemas import ProductCreateSchema, ProductCategoryCreateSchema
from src.products.services import (ProductService, product_depends_execute, ProductCategoryService, category_depends_execute)


router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]   
)

@router.post("/category/create/")
async def create_product_category(
    category: ProductCategoryCreateSchema,
    service: Annotated[ProductCategoryService, Depends(category_depends_execute)]
):
    data = await service.create_category(category)
    return {"data": data}


@router.post("/create/")
async def create_product(
    product: ProductCreateSchema,
    service: Annotated[ProductService, Depends(product_depends_execute)]
):
    data = await service.add_product(product)
    return {"data": data}


@router.get("/product/{product_id}")
async def retrieve_product(
    product_id: int,
    service: Annotated[ProductService, Depends(product_depends_execute)]
):
    data = await service.get_retrieve(product_id)
    return data