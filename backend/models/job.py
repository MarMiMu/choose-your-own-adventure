from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True, unique=True)
    session_id = Column(String, index=True)
    story_id = Column(String, nullable=True)
    theme = Column(String)
    error = Column(String, nullable=True)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)