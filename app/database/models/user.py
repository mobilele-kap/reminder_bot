from ..base import Base
from ..standard_type import big_int_pk, created_at, updated_at, deleted, big_int_uc, code_name_uc
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey, VARCHAR, Index
from sqlalchemy.dialects.postgresql import JSONB
from typing import Optional
import datetime


class UserOrm(Base):
    __tablename__ = 'user'

    id: Mapped[big_int_pk]
    telegram_id: Mapped[big_int_uc]
    telegram_login: Mapped[Optional[str]] = mapped_column(VARCHAR(256), comment='Логин telegram')
    deleted: Mapped[deleted]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user_event: Mapped[list["UserEventOrm"]] = relationship(
        back_populates='user',
    )


class UserEventOrm(Base):
    __tablename__ = 'user_event'

    id: Mapped[big_int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user_event_type_id: Mapped[int] = mapped_column(ForeignKey("user_event_type.id", ondelete="CASCADE"))
    event_data: Mapped[dict] = mapped_column(JSONB, comment='Информация для события')
    event_at: Mapped[datetime.datetime] = mapped_column(comment='Дата начала начала события')
    user_event_status_id: Mapped[int] = mapped_column(ForeignKey("user_event_status.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user: Mapped["UserOrm"] = relationship(back_populates='user_event')
    user_event_status: Mapped["UserEventStatusOrm"] = relationship(back_populates='user_event')
    user_event_type: Mapped["UserEventTypeOrm"] = relationship(back_populates='user_event')

    __table_args__ = (
        Index("user_event_event_at_idx", "event_at"),
    )


class UserEventStatusOrm(Base):
    __tablename__ = 'user_event_status'

    id: Mapped[big_int_pk]
    code_name: Mapped[code_name_uc]
    description: Mapped[str] = mapped_column(VARCHAR(4000), comment='Описание статуса')
    visible: Mapped[bool] = mapped_column(comment='Показывать ли пользователям')
    process: Mapped[bool] = mapped_column(comment='Обрабытавать ли данный статус')
    created_at: Mapped[created_at]

    user_event: Mapped[list["UserEventOrm"]] = relationship(back_populates='user_event_status')

    __table_args__ = (
        Index("user_event_status_code_name_idx", "code_name"),
    )


class UserEventTypeOrm(Base):
    __tablename__ = 'user_event_type'

    id: Mapped[big_int_pk]
    code_name: Mapped[code_name_uc]
    description: Mapped[str] = mapped_column(VARCHAR(4000), comment='Описание евента')
    created_at: Mapped[created_at]

    user_event: Mapped[list["UserEventOrm"]] = relationship(back_populates='user_event_type')

    __table_args__ = (
        Index("user_event_type_code_name_idx", "code_name"),
    )


