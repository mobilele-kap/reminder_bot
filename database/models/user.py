from ..base import Base
from ..standard_type import big_int_pk, created_at, updated_at, deleted, big_int_uc, code_name_uc
from sqlalchemy.orm import Mapped
from sqlalchemy import mapped_column, ForeignKey, VARCHAR
from sqlalchemy.dialects.postgresql import JSONB
import datetime


class UserOrm(Base):
    __tablename__ = 'user'

    id: Mapped[big_int_pk]
    telegram_id: Mapped[big_int_uc]
    deleted: Mapped[deleted]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class UserEventOrm(Base):
    __tablename__ = 'user_event'

    id: Mapped[big_int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user_event_type_id: Mapped[int] = mapped_column(ForeignKey("user_event_type.id", ondelete="CASCADE"))
    event_data: Mapped[JSONB] = mapped_column(comment='Информация для события')
    event_at: Mapped[datetime.datetime] = mapped_column(comment='Дата начала начала события')
    deleted: Mapped[deleted]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class UserEventTypeOrm(Base):
    __tablename__ = 'user_event_type'

    id: Mapped[big_int_pk]
    code_name: Mapped[code_name_uc]
    description: Mapped[str] = mapped_column(VARCHAR(4000), comment='Описание евента')
    created_at: Mapped[created_at]
