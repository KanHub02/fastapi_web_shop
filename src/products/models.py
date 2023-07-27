from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, ForeignKey

from src.database.base_model import AbstractBase, Base
from src.products.schemas import ProductShema, ProductCategorySchema


class ProductCategory(AbstractBase):
    __tablename__ = "product_category"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)

    def to_read_model(self):
        return ProductCategorySchema(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
        )


class Product(AbstractBase):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    price: Mapped[float] = mapped_column(Float, default=0.0)
    category: Mapped[int] = mapped_column(ForeignKey("product_category.id"))

    def to_read_model(self):
        return ProductShema(
            id=self.id,
            title=self.title,
            description=self.description,
            price=self.price,
            product_category_id=self.category.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted,
        )
