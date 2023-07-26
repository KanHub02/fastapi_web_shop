from src.products.schemas import ProductCreateSchema, ProductCategoryCreateSchema
from src.products.repositories import ProductSqlRepository, ProductCategoryRepository

from src.common.base_services import BaseService


class ProductService(BaseService):

    async def add_product(self, product_schema: ProductCreateSchema):
        data = product_schema.model_dump()
        commit = await self.repository.create(data)
        return commit


class ProductCategoryService(BaseService):

    async def create_category(self, category_schema: ProductCategoryCreateSchema):
        data = category_schema.model_dump()
        commit = await self.repository.create(data)
        return commit


def category_depends_execute():
    return ProductCategoryService(ProductCategoryRepository)

def product_depends_execute():
    return ProductService(ProductSqlRepository)