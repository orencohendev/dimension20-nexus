

from uuid import UUID
from app.dal.repositories.campaign_repository import CampaignRepository
from app.models.campaign import Campaign


class CampaignManager:

    @staticmethod
    async def get_campaigns():
        campaigns = await CampaignRepository.get_all()

        return campaigns

    @staticmethod
    async def get_campaign_by_id(campaign_id: UUID):
        campaign = await CampaignRepository.get_by_id(campaign_id)

        return campaign