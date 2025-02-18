from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Extra


class PostgreSQL(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore', env_file=".env")

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def dsn_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class Telegram(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore', env_file=".env")

    TOKEN: str


database = PostgreSQL()
bot = Telegram()
