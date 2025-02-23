import uuid
from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship

from app.dal.models.episode_model import EpisodeModel
from app.dal.models.review_model import ReviewModel

from app.dal.models.base import Base

class CampaignModel(Base):
    __tablename__ = "campaigns"
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    year = Column(Integer, nullable=True)
    is_sequel = Column(Boolean, default=False)
    
    # Allows referencing a previous campaign if it's a sequel
    previous_campaign_id = Column(
        PG_UUID(as_uuid=True), 
        ForeignKey("campaigns.id"),
        nullable=True
    )
    
    # Relationship fields
    reviews = relationship(
        "ReviewModel",
        back_populates="campaign",
        cascade="all, delete-orphan"
    )
    episodes = relationship(
        "EpisodeModel",
        back_populates="campaign",
        cascade="all, delete-orphan"
    )



