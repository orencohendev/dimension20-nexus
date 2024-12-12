from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "Dimension 20 Nexus API"
    is_dev: bool = Field(default=False)
    service_port: int = Field(default=8000)

    class Config:
        env_file = ".env"


config = Settings()
