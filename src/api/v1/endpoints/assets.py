from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.asset import Asset
from src.schemas.asset import AssetResponse
import boto3
from src.config import settings
import uuid

router = APIRouter()

s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    endpoint_url=settings.S3_ENDPOINT_URL
)

@router.post("/upload", response_model=AssetResponse)
async def upload_asset(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1. Generate unique S3 Key
    file_extension = file.filename.split(".")[-1]
    s3_key = f"assets/{uuid.uuid4()}.{file_extension}"
    
    # 2. Upload to S3
    try:
        s3_client.upload_fileobj(file.file, settings.S3_BUCKET_NAME, s3_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to upload to S3")

    # 3. Create DB Record (Processing state)
    new_asset = Asset(
        filename=file.filename,
        file_type=file.content_type,
        s3_key=s3_key,
        org_id=uuid.uuid4() # Mock Org ID for now
    )
    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)

    # 4. Trigger AI Pipeline (Celery)
    # Reference to previously defined tasks
    from tasks import process_asset_pipeline
    background_tasks.add_task(process_asset_pipeline.delay, str(new_asset.id), s3_key)

    return new_asset

@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(asset_id: UUID, db: Session = Depends(get_db)):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset