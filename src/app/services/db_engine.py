from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from app.conf import settings


def get_engine():
    return create_engine(str(settings.DATABASE_URL))

def get_async_engine():
    return create_async_engine(str(settings.ASYNC_DATABASE_URL))