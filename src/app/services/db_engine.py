from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from app.conf import settings


def get_engine():
    return create_engine(settings.database_url)


def get_async_engine():
    return create_async_engine(settings.async_database_url)
