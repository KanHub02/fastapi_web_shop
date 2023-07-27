from fastapi import FastAPI

from src.products.routers import router as product_router

app = FastAPI(title="WebShop API")

app.include_router(product_router)
