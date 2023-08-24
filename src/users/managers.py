import uuid
from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users import BaseUserManager, InvalidPasswordException, UUIDIDMixin
from fastapi_users.models import UP
from fastapi_users.exceptions import UserNotExists

from src.users.models import User, get_user_db
from src.users.schemas import UserCreate


SECRET = "SECRET123123"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> str:
        return f"User {user.id} has registered."

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(reason="Password should not contain e-mail")

    async def get_by_email(self, user_email: str) -> UP:

        user = await self.user_db.get_by_email(user_email)

        if user is None:
            raise UserNotExists()

        return user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
