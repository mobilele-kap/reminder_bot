import datetime
from typing import Annotated
from sqlalchemy import text, BigInteger, String, VARCHAR
from sqlalchemy.orm import mapped_column

# Ключи:
big_int_pk = Annotated[int, mapped_column(BigInteger, primary_key=True, comment='Перыичный идентификатор')]
big_int_uc = Annotated[int, mapped_column(BigInteger, unique=True, comment='Уникальный идентификатор')]
code_name_uc = Annotated[str, mapped_column(VARCHAR(256), unique=True, comment='Кодовое название (идентификатор)')]

# Даты:
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("current_timestamp"),
    comment='Дата создания записи')]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("current_timestamp"),
    onupdate=datetime.datetime.now,
    comment='Дата обновленея записи')]
deleted = Annotated[int, mapped_column(bool, comment='Является ли запись удаленной')]
