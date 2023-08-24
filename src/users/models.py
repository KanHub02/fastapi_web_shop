from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.base_model import AbstractBase, Base
from src.database.database import get_async_session


class User(SQLAlchemyBaseUserTable, AbstractBase):
    pass


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
