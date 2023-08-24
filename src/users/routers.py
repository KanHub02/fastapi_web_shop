import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.users.models import User
from src.users.managers import get_user_manager
from src.users.authentication.transport import auth_backend


fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
)