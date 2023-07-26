from typing import Dict, Union

from abc import ABC, abstractmethod

from sqlalchemy import select, insert, delete, update

from database.database import get_async_session


class DatabaseRepositoryInterface(ABC):
    @abstractmethod
    async def get_retrieve():
        raise NotImplementedError

    @abstractmethod
    async def get_list():
        raise NotImplementedError

    @abstractmethod
    async def create():
        raise NotImplementedError

    @abstractmethod
    async def delete():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError


class SqlQueryRepository(DatabaseRepositoryInterface):

    model = None

    async def get_retrieve(self, id: Union[str, int]) -> Dict:
        async with get_async_session() as session:
            statement = select(self.model).where(self.model.id == id)
            result = await session.execute(statement)
            result_data = [i[0].to_read_model() for i in result.all()]
            return result_data

    async def get_list(self) -> Dict:
        async with get_async_session() as session:
            statement = select(self.model)
            result = await session.execute(statement)
            result_data = [i[0].to_read_model() for i in result.all()]
            return result_data

    async def create(self, data: Dict) -> int:
        async with get_async_session() as session:
            statement = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(statement)
            await session.commit()
            return result.scalar_one()
