from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base  # Убедись, что ты импортируешь свой базовый класс из правильного модуля

class User(Base):
    __tablename__ = "users"

    # id — это идентификатор пользователя. Типизация через Mapped.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # роль пользователя (по умолчанию 'user')
    role: Mapped[str] = mapped_column(String, default="user")

    # блокировка пользователя (по умолчанию False)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)
