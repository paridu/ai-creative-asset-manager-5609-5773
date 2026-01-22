from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class AssetBase(BaseModel):
    filename: str
    project_id: Optional[UUID] = None

class AssetCreate(AssetBase):
    pass

class AssetUpdate(BaseModel):
    tags: List[str]
    project_id: Optional[UUID]

class AssetResponse(AssetBase):
    id: UUID
    s3_key: str
    tags: List[str]
    color_palette: List[str]
    created_at: datetime

    class Config:
        from_attributes = True

class SearchQuery(BaseModel):
    query: str
    limit: int = 20