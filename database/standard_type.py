import datetime
from typing import Annotated
from sqlalchemy import text, BigInteger
from sqlalchemy.orm import mapped_column


big_int_pk = Annotated[int, mapped_column(BigInteger, primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("current_timestamp"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("current_timestamp"),
        onupdate=datetime.datetime.now,
    )]
