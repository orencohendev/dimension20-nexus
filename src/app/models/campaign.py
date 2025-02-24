from typing import List
from pydantic import UUID4, BaseModel, ConfigDict

from app.handlers.api_models.review import Review


class Campaign(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID4
    title: str
    url: str
    description: str | None = None
    year: int | None = None
    reviews: List[Review] = []
    is_sequel: bool = False
    previous_campaign_id: UUID4 | None = None
