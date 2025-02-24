from app.services import db_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.dal.models.episode_model import EpisodeModel
from app.models.episode import Episode

class EpisodeRepository:

    @staticmethod
    async def get_all():
        """Retrieve all campaign records asynchronously."""
        async with AsyncSession(db_engine.get_async_engine()) as session:
            result = await session.execute(
                select(EpisodeModel)
            )
            db_models = result.scalars().all()

            return [
                Episode.model_validate(db_model, from_attributes=True)
                for db_model in db_models
            ]