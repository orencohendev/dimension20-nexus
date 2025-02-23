import os
import json
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import your SQLAlchemy Base and models
from app.dal.models.campaign_model import CampaignModel
from app.dal.models.episode_model import EpisodeModel
from app.dal.models.review_model import ReviewModel

# Import your Pydantic schemas
from app.models.campaign import Campaign
from app.models.episode import Episode

# Import your SQLAlchemy Base
from app.dal.models.base import Base
from app.services.db_engine import get_engine



def seed_data():
    engine = get_engine()  # A function that returns create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        Base.metadata.create_all(engine)

        # 2. Load JSON data
        with open("app/data/campaigns.json") as f:
            campaigns_raw = json.load(f)
        with open("app/data/episodes.json") as f:
            episodes_raw = json.load(f)

        # 3. Validate using Pydantic
        campaigns = [Campaign(**c) for c in campaigns_raw]
        episodes = [Episode(**e) for e in episodes_raw]

        # 4. Upsert in DB
        for c in campaigns:
            # Convert Pydantic to SQLAlchemy
            campaign_obj = CampaignModel(
                id=c.id,
                title=c.title,
                url=c.url,
                description=c.description,
                year=c.year,
                is_sequel=c.is_sequel,
                previous_campaign_id=c.previous_campaign_id  # or None
            )
            # Merge will insert if the primary key doesn’t exist, or update if it does
            session.merge(campaign_obj)
            
            # Reviews
            review_json_ids = []
            for r in c.reviews:
                review_json_ids.append(r.id)
                review_obj = ReviewModel(
                    id=r.id,  # or autoincrement if you prefer
                    campaign_id=c.id,
                    source=r.source,
                    url=r.url,
                    excerpt=r.excerpt,
                    rating=r.rating
                )
                session.merge(review_obj)
            
            # Delete reviews that are not in the JSON
            session.query(ReviewModel).filter(ReviewModel.campaign_id == c.id).filter(~ReviewModel.id.in_(review_json_ids)).delete(synchronize_session=False)

        for e in episodes:
            episode_obj = EpisodeModel(
                id=e.id,
                campaign_id=e.campaign_id,
                title=e.title,
                episode_number=e.episode_number,
                url=e.url,
                air_date=e.air_date,
                description=e.description,
                length=e.length
            )
            session.merge(episode_obj)

        session.commit()
        print("Seeding completed successfully!")
    except Exception as ex:
        session.rollback()
        print(f"Error during seeding: {ex}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_data()
