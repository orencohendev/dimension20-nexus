from pydantic import BaseModel
from pydantic.types import UUID4

class Episode(BaseModel):
    id: UUID4
    campaign_id: UUID4
    title: str
    episode_number: int
    url: str
    air_date: str | None = None
    description: str | None = None
    length: int | None = None