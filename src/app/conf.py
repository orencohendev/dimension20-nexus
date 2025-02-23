from pydantic import PostgresDsn, Field, field_validator
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: str = Field(..., env="DB_PORT")
    DB_NAME: str = Field(..., env="DB_NAME")
    DATABASE_URL: Optional[PostgresDsn] = None
    ASYNC_DATABASE_URL: Optional[PostgresDsn] = None
    is_dev: bool = False
    service_port: int = 8000

    @field_validator("DB_PORT")
    def check_db_port(cls, v: str) -> int:
        return int(v)


    @field_validator("DATABASE_URL")
    def check_db_url(cls, v: Optional[str], values: dict) -> Optional[str]:
        if v is None:
            if (
                values.data.get("DB_USER")
                and values.data.get("DB_PASSWORD")
                and values.data.get("DB_HOST")
                and values.data.get("DB_PORT")
                and values.data.get("DB_NAME")
            ):
                return PostgresDsn.build(
                    scheme="postgresql",
                    username=values.data["DB_USER"],
                    password=values.data["DB_PASSWORD"],
                    host=values.data["DB_HOST"],
                    port=int(values.data["DB_PORT"]),
                    path=f"{values.data['DB_NAME']}",
                )
        return v

    @field_validator("ASYNC_DATABASE_URL")
    def check_async_db_url(cls, v: Optional[str], values: dict) -> Optional[str]:
        if v is None:
            if (
                values.data.get("DB_USER")
                and values.data.get("DB_PASSWORD")
                and values.data.get("DB_HOST")
                and values.data.get("DB_PORT")
                and values.data.get("DB_NAME")
            ):
                return PostgresDsn.build(
                    scheme="postgresql+asyncpg",
                    username=values.data["DB_USER"],
                    password=values.data["DB_PASSWORD"],
                    host=values.data["DB_HOST"],
                    port=int(values.data["DB_PORT"]),
                    path=f"{values.data['DB_NAME']}",
                )
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Usage
settings = Settings()
