# Cloud Infrastructure Strategy: ARCHIVE-AI

## 1. Architecture Overview
The ARCHIVE-AI infrastructure is designed for high availability, massive scalability, and low-latency asset delivery. We utilize AWS as the primary cloud provider, managed via Terraform (IaC).

## 2. Key Components
*   **Storage (S3):** Multi-tier storage for raw assets, thumbnails, and optimized web-versions. Includes lifecycle policies to transition cold assets to S3 Glacier.
*   **Compute (EKS):** Elastic Kubernetes Service to host microservices and AI inference workers. GPU-enabled node groups are used for CLIP model processing.
*   **Database (RDS & OpenSearch):**
    *   **RDS PostgreSQL:** Transactional data and metadata.
    *   **Amazon OpenSearch (Vector Engine):** Stores CLIP embeddings for semantic "vibe-based" search.
*   **Content Delivery (CloudFront):** Global edge caching for designer assets to ensure instant loading in any region.
*   **Async Processing (SQS/Lambda):** Event-driven triggers for file ingestion and thumbnail generation.

## 3. Security
*   **IAM Roles for Service Accounts (IRSA):** Minimal privilege access for pods.
*   **KMS Encryption:** All assets at rest and in transit are encrypted.
*   **VPC Private Subnets:** Databases and AI workers are not exposed to the public internet.