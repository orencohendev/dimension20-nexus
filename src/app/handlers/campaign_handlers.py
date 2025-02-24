from typing import List
from uuid import UUID
from fastapi.routing import APIRouter
from app.models.campaign import Campaign
from app.handlers.mock_data import mock_campaigns
from app.models.episode import Episode
from app.services.campaign_manager import CampaignManager

router = APIRouter()


@router.get("/campaigns")
async def get_campaigns() -> List[Campaign]:
    return await CampaignManager.get_campaigns()


@router.get("/campaigns/{campaign_id}")
async def get_campaign_by_id(campaign_id: UUID) -> Campaign:
    return await CampaignManager.get_campaign_by_id(campaign_id)


@router.get("/campaigns/{campaign_id}/episodes")
async def get_campaign_episodes(campaign_id: UUID) -> List[Episode]:
    return await CampaignManager.get_campaign_episodes(campaign_id)
