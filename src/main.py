from fastapi import FastAPI

from src.products.routers import router as product_router
from src.users.routers import fastapi_users
from src.users.schemas import UserCreate, UserRead
from src.users.authentication.transport import auth_backend
    
app = FastAPI(title="WebShop API")

app.include_router(product_router)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)
app.include_router(
    fastapi_users.get_auth_router(requires_verification=False, backend=auth_backend)
)
