import uuid
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

from app.dal.models.base import Base


class EpisodeModel(Base):
    __tablename__ = "episodes"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campaign_id = Column(
        PG_UUID(as_uuid=True), ForeignKey("campaigns.id"), nullable=False
    )
    title = Column(String, nullable=False)
    episode_number = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    air_date = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    length = Column(Integer, nullable=True)

    # Relationship back to Campaign
    campaign = relationship("CampaignModel", back_populates="episodes")
