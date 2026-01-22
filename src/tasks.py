import os
import uuid
from celery import Celery
import boto3
from pipeline_utils import generate_thumbnail, extract_dominant_colors, get_file_metadata
import requests

# Celery Configuration
app = Celery('ingestion_tasks', broker=os.getenv('RABBITMQ_URL'), backend=os.getenv('REDIS_URL'))

# AWS S3 Client
s3 = boto3.client('s3')
BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

@app.task(name="pipeline.process_asset")
def process_asset_pipeline(asset_id: str, s3_key: str, original_filename: str):
    """
    ETL Pipeline Stage:
    1. Extract: Pull raw file from S3.
    2. Transform: Generate thumbnails, extract colors, call AI models for tags/embeddings.
    3. Load: Update PostgreSQL metadata and Pinecone Vector index.
    """
    print(f"[*] Starting processing for Asset: {asset_id}")

    # 1. DOWNLOAD FROM S3
    response = s3.get_object(Bucket=BUCKET_NAME, Key=s3_key)
    file_content = response['Body'].read()

    # 2. METADATA EXTRACTION
    meta = get_file_metadata(file_content, original_filename)
    
    # 3. VISUAL PROCESSING (If Image)
    if meta['mime_type'].startswith('image/'):
        # Generate Thumbnail
        thumb_bytes = generate_thumbnail(file_content)
        thumb_key = f"thumbnails/{asset_id}.jpg"
        s3.put_object(Bucket=BUCKET_NAME, Key=thumb_key, Body=thumb_bytes, ContentType='image/jpeg')
        
        # Color Extraction
        colors = extract_dominant_colors(file_content)
        
        # AI EMBEDDINGS (Mocking call to CV Model Microservice)
        # In production: requests.post("http://cv-service/embed", data=file_content)
        mock_embedding = [0.12] * 512 
        mock_tags = ["modern", "minimalist", "ui-component"]
    else:
        colors, mock_embedding, mock_tags, thumb_key = [], [], [], None

    # 4. DATA PERSISTENCE (Update DB via API or Direct DB connection)
    # This payload matches the schema.sql defined in previous steps
    update_payload = {
        "id": asset_id,
        "file_size": meta['size_kb'],
        "file_type": meta['extension'],
        "thumbnail_url": thumb_key,
        "tags": mock_tags,
        "colors": colors,
        "embedding": mock_embedding,
        "status": "processed"
    }

    # Signal completion (e.g., via internal API or Webhook)
    print(f"[+] Asset {asset_id} processed successfully. Meta: {meta['mime_type']}")
    return update_payload