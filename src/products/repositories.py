from src.common.base_repositories import SqlQueryRepository

from src.products.models import Product, ProductCategory


class ProductSqlRepository(SqlQueryRepository):
    model = Product


class ProductCategoryRepository(SqlQueryRepository):
    model = ProductCategory
