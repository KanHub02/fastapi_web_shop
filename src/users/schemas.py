import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser):
    hashed_password: str


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
