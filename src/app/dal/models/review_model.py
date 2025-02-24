import uuid
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

from app.dal.models.base import Base


class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campaign_id = Column(
        PG_UUID(as_uuid=True), ForeignKey("campaigns.id"), nullable=False
    )
    source = Column(String, nullable=False)
    url = Column(String, nullable=False)
    excerpt = Column(Text, nullable=True)
    rating = Column(Integer, nullable=True)

    # Relationship back to Campaign
    campaign = relationship("CampaignModel", back_populates="reviews")
