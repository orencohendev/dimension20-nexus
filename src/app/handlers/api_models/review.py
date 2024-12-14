from pydantic import BaseModel


class Review(BaseModel):
    source: str
    url: str
    excerpt: str | None = None
    rating: int | None = None
