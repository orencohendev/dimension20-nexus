from typing import List
from fastapi.routing import APIRouter
from app.models.campaign import Campaign
from app.handlers.mock_data import mock_campaigns
from app.services.campaign_manager import CampaignManager

router = APIRouter()


@router.get("/campaigns")
async def get_campaigns() -> List[Campaign]:
    return await CampaignManager.get_campaigns()

@router.get("/campaigns/{campaign_id}")
async def get_campaign_by_id(campaign_id: str) -> Campaign:
    return await CampaignManager.get_campaign_by_id(campaign_id)