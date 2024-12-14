from typing import List
from fastapi.routing import APIRouter
from app.handlers.api_models.campaigns import Campaign
from app.handlers.mock_data import mock_campaigns

router = APIRouter()


@router.get("/campaigns")
async def get_campaigns() -> List[Campaign]:
    return mock_campaigns  # type: ignore
