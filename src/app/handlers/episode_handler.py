from uuid import UUID
from fastapi.routing import APIRouter

from app.services.episode_manager import EpisodeManager


router = APIRouter()


@router.get("/episodes")
async def get_episodes():
    res = await EpisodeManager.get_all_episodes()

    return res

@router.get("/episodes/{episode_id}")
async def get_episode(episode_id: UUID):
    res = await EpisodeManager.get_episode_by_id(episode_id)

    return res
