from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "Dimension 20 Nexus API"
    is_dev: bool = Field(default=False, env="IS_DEV")
    service_port: int = Field(default=8000, env="SERVICE_PORT")

    class Config:
        env_file = ".env"

config = Settings()