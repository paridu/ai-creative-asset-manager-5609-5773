import pinecone
from typing import List, Dict
import os

# ARCHIVE-AI Vector Database Implementation
# This module handles semantic embedding storage and retrieval

class VectorStore:
    def __init__(self, api_key: str, environment: str, index_name: str = "archive-ai-assets"):
        pinecone.init(api_key=api_key, environment=environment)
        self.index_name = index_name
        
        # CLIP model output is typically 512 or 768 dimensions
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(
                name=self.index_name, 
                dimension=768, # CLIP ViT-L/14 dimension
                metric="cosine"
            )
        self.index = pinecone.Index(self.index_name)

    def upsert_asset_embedding(self, asset_id: str, embedding: List[float], metadata: Dict):
        """
        Stores the high-dimensional vector of an asset.
        Metadata includes project_id and org_id for pre-filtering.
        """
        self.index.upsert(
            vectors=[(
                asset_id, 
                embedding, 
                {
                    "org_id": metadata.get("org_id"),
                    "project_id": metadata.get("project_id"),
                    "file_type": metadata.get("file_type")
                }
            )]
        )

    def semantic_search(self, query_vector: List[float], org_id: str, top_k: int = 20):
        """
        Retrieves asset IDs based on vector similarity.
        Filters by org_id to ensure data isolation.
        """
        results = self.index.query(
            vector=query_vector,
            filter={"org_id": {"$eq": org_id}},
            top_k=top_k,
            include_metadata=False
        )
        return [match['id'] for match in results['matches']]

    def delete_asset_vector(self, asset_id: str):
        self.index.delete(ids=[asset_id])