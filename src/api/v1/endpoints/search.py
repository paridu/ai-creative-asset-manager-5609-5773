from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.asset import Asset
from src.schemas.asset import AssetResponse, SearchQuery
import pinecone
from src.config import settings
from sentence_transformers import SentenceTransformer

router = APIRouter()

# Load CLIP model for text-to-image encoding
model = SentenceTransformer('clip-ViT-B-32')

@router.post("/semantic", response_model=list[AssetResponse])
def semantic_search(search: SearchQuery, db: Session = Depends(get_db)):
    # 1. Generate Embedding from search query
    query_vector = model.encode(search.query).tolist()

    # 2. Query Vector DB (Pinecone)
    pc = pinecone.Index(settings.PINECONE_INDEX_NAME)
    search_results = pc.query(
        vector=query_vector,
        top_k=search.limit,
        include_metadata=False
    )

    # 3. Extract IDs and fetch metadata from PostgreSQL
    asset_ids = [match['id'] for match in search_results['matches']]
    assets = db.query(Asset).filter(Asset.id.in_(asset_ids)).all()

    # Sort results to match Pinecone's relevance order
    assets_sorted = sorted(assets, key=lambda x: asset_ids.index(str(x.id)))
    
    return assets_sorted