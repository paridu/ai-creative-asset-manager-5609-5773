from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from pydantic import BaseModel
import uuid
import pika
import json

app = FastAPI(title="Archive-AI Asset Service")

# RabbitMQ Setup
def publish_to_queue(asset_id: str, file_path: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='ingestion_queue')
    
    message = {
        "asset_id": asset_id,
        "file_path": file_path,
        "action": "PROCESS_ASSET"
    }
    
    channel.basic_publish(exchange='', routing_key='ingestion_queue', body=json.dumps(message))
    connection.close()

@app.post("/assets/upload")
async def upload_asset(background_tasks: BackgroundTasks, file: File(...)):
    asset_id = str(uuid.uuid4())
    # 1. Save file to S3 (Simulated)
    file_path = f"s3://archive-ai-bucket/{asset_id}_{file.filename}"
    
    # 2. Save Initial Metadata to Postgres
    # db.save(asset_id, file_path, status="PENDING")
    
    # 3. Trigger AI Ingestion Pipeline
    background_tasks.add_task(publish_to_queue, asset_id, file_path)
    
    return {"asset_id": asset_id, "status": "processing"}

@app.get("/assets/{asset_id}")
async def get_asset(asset_id: str):
    return {"asset_id": asset_id, "metadata": {"tags": ["vibrant", "summer"], "colors": ["#FF5733", "#C70039"]}}