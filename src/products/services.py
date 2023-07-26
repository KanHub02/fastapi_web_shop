from typing import Union

from src.products.schemas import ProductCreateSchema, ProductCategoryCreateSchema, ProductDetailSchema
from src.products.repositories import ProductSqlRepository, ProductCategoryRepository

from src.common.base_services import BaseService


class ProductService(BaseService):

    async def add_product(self, product_schema: ProductCreateSchema):
        data = product_schema.model_dump()
        commit = await self.repository.create(data)
        return commit
    
    async def get_retrieve(self, pk: Union[str, int]):
        result = await self.repository.get_retrieve(pk=pk)
        return result
    
    async def get_list(self):
        result = await self.repository.get_list()
        return result



class ProductCategoryService(BaseService):

    async def create_category(self, category_schema: ProductCategoryCreateSchema):
        data = category_schema.model_dump()
        commit = await self.repository.create(data)
        return commit


def category_depends_execute():
    return ProductCategoryService(ProductCategoryRepository)

def product_depends_execute():
    return ProductService(ProductSqlRepository)