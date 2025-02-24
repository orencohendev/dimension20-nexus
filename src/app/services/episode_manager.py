from uuid import UUID
from app.dal.repositories.episode_repository import EpisodeRepository

class EpisodeManager:

    @staticmethod
    async def get_all_episodes():
        episodes = await EpisodeRepository.get_all()
        return episodes
    
    @staticmethod
    async def get_episode_by_id(episode_id: UUID):
        ...
    