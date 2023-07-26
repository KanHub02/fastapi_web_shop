from abc import ABC, abstractmethod
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AbstractBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)

    @abstractmethod
    def to_read_model(self):
        raise NotImplementedError
