from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from typing import List, Optional

from app.dal.models.campaign_model import CampaignModel
from app.models.campaign import Campaign
from app.services import db_engine


# Assuming Campaign is already defined as a SQLAlchemy model
class CampaignRepository:

    @staticmethod
    async def get_all() -> List[Campaign]:
        """Retrieve all campaign records asynchronously."""
        async with AsyncSession(db_engine.get_async_engine()) as session:
            result = await session.execute(
                select(CampaignModel).options(
                    selectinload(CampaignModel.reviews)  # EAGER LOAD
                )
            )
            db_models = result.scalars().all()

            return [
                Campaign.model_validate(db_model, from_attributes=True)
                for db_model in db_models
            ]

    @staticmethod
    async def get_by_id(campaign_id: UUID) -> Optional[Campaign]:
        """Retrieve a single campaign record by its ID asynchronously."""
        async with AsyncSession(db_engine.get_async_engine()) as session:
            result = await session.execute(
                select(CampaignModel)
                .options(selectinload(CampaignModel.reviews))  # EAGER LOAD
                .filter(CampaignModel.id == campaign_id)
            )
            db_model = result.scalars().first()

            return (
                Campaign.model_validate(db_model, from_attributes=True)
                if db_model
                else None
            )
