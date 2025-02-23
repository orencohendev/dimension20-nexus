from pydantic import PostgresDsn, Field, ValidationInfo, field_validator
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "postgres"
    database_url: Optional[PostgresDsn] = None
    async_database_url: Optional[PostgresDsn] = None
    is_dev: bool = False
    service_port: int = 8000

    @field_validator("db_port")
    def check_db_port(cls, v: str) -> int:
        return int(v)

    @field_validator("database_url")
    def check_db_url(cls, v: Optional[str], values: ValidationInfo) -> Optional[str]:
        if v is None:
            if (
                values.data.get("DB_USER")
                and values.data.get("DB_PASSWORD")
                and values.data.get("DB_HOST")
                and values.data.get("DB_PORT")
                and values.data.get("DB_NAME")
            ):
                return str(
                    PostgresDsn.build(
                        scheme="postgresql",
                        username=values.data["DB_USER"],
                        password=values.data["DB_PASSWORD"],
                        host=values.data["DB_HOST"],
                        port=int(values.data["DB_PORT"]),
                        path=f"{values.data['DB_NAME']}",
                    )
                )
        return str(v)

    @field_validator("async_database_url")
    def check_async_db_url(
        cls, v: Optional[str], values: ValidationInfo
    ) -> Optional[str]:
        if v is None:
            if (
                values.data.get("db_user")
                and values.data.get("db_password")
                and values.data.get("db_host")
                and values.data.get("db_port")
                and values.data.get("db_name")
            ):
                return str(
                    PostgresDsn.build(
                        scheme="postgresql+asyncpg",
                        username=values.data["db_user"],
                        password=values.data["db_password"],
                        host=values.data["db_host"],
                        port=values.data["db_port"],
                        path=f"{values.data['db_name']}",
                    )
                )
        return str(v)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Usage
settings = Settings()
