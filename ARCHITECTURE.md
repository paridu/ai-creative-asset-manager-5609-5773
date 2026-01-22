# ARCHIVE-AI System Architecture Document

## 1. System Overview
ARCHIVE-AI is built on a distributed microservices architecture to handle high-throughput file processing, AI inference, and complex metadata indexing. The system follows an event-driven pattern for asset ingestion and a specialized search architecture for semantic retrieval.

## 2. Technology Stack
*   **API Gateway:** Kong or Nginx
*   **Backend Framework:** FastAPI (Python) for AI/ML compatibility
*   **Frontend:** Next.js (React) with Tailwind CSS
*   **Primary Database:** PostgreSQL (Metadata, User Data, Relations)
*   **Vector Database:** Pinecone or Milvus (Semantic Search Embeddings)
*   **Caching/Message Broker:** Redis & RabbitMQ
*   **Storage:** AWS S3 or MinIO (Object Storage)
*   **AI Models:** 
    *   CLIP (OpenAI) for visual embeddings
    *   BLIP-2 for captioning and tagging
    *   Custom OpenCV/Pillow scripts for color palette extraction

## 3. High-Level Diagram (Mermaid)