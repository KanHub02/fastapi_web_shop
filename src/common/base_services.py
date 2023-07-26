
from src.common.base_repositories import DatabaseRepositoryInterface


class BaseService:
    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.repository: DatabaseRepositoryInterface = repository()