from typing import List
from pydantic import UUID4, BaseModel

from app.handlers.api_models.review import Review

class Campaign(BaseModel):
    id: UUID4
    title: str
    url: str
    description: str | None = None
    year: int | None = None
    reviews: List[Review] = []
    is_sequel: bool = False
    previous_campaign_id: UUID4 | None = None