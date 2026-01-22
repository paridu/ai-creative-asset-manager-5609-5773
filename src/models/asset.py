from sqlalchemy import Column, String, JSON, ForeignKey, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from .base import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(UUID(as_uuid=True), index=True)
    project_id = Column(UUID(as_uuid=True), index=True, nullable=True)
    
    filename = Column(String(255), nullable=False)
    file_type = Column(String(50))
    s3_key = Column(String(512), nullable=False)
    
    # AI Generated Metadata
    tags = Column(JSON, default=[])  # ["nature", "blue", "minimalist"]
    color_palette = Column(JSON, default=[]) # ["#FFFFFF", "#000000"]
    embedding_id = Column(String(255)) # ID reference in Pinecone
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())