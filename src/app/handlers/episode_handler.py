from fastapi.routing import APIRouter
from app.handlers.mock_data import mock_episodes

router = APIRouter()


@router.get("/episodes")
async def get_episodes():
    return mock_episodes  # type: ignore
