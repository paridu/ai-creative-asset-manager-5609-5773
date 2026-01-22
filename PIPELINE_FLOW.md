# ARCHIVE-AI Data Pipeline Documentation

## Pipeline Overview
The ingestion pipeline is designed as an asynchronous, event-driven ETL process. It ensures that heavy computational tasks (Image processing, AI inference) do not block the main user interface.

## Flow of Data
1.  **Ingestion Trigger:** User uploads a file via the Next.js frontend to an S3 Presigned URL.
2.  **Event Notification:** The API Backend (FastAPI) receives a callback and pushes a message `process_asset` to **RabbitMQ**.
3.  **Extraction:** The **Celery Worker** picks up the task, downloads the raw bytes from S3.
4.  **Transformation:**
    *   **Worker** extracts technical metadata (MIME, size).
    *   **Worker** generates a 300x300 JPEG thumbnail and re-uploads it to a public S3 bucket.
    *   **AI Inference:** The worker sends the image to the CV Model (CLIP) to generate a 512-dimension vector embedding and auto-tags.
    *   **Color Lab:** Extracts dominant brand colors for palette searching.
5.  **Loading:**
    *   Structured metadata is saved to **PostgreSQL**.
    *   The vector embedding is upserted to **Pinecone** for semantic search.
6.  **Notification:** The worker emits a "Task Complete" event via Redis Pub/Sub to notify the frontend via WebSockets.

## Scaling Strategy
*   **Vertical Scaling:** Increase Celery concurrency for CPU-bound tasks (thumbnailing).
*   **Horizontal Scaling:** Deploy multiple worker containers.
*   **Specialized Workers:** Separate queues for "Standard Files" vs "Heavy Files" (e.g., large PSD/Video files).