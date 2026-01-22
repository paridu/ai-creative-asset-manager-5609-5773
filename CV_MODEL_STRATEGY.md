# Computer Vision Strategy: ARCHIVE-AI

## 1. Overview
To achieve "Semantic Intelligence" and "Zero-Effort Organization," we utilize a dual-model approach:
*   **Feature Extraction (CLIP):** OpenAI's CLIP (Contrastive Language-Image Pre-training) is used to map images and text into a shared latent space. This enables both visual similarity search (image-to-image) and semantic search (text-to-image).
*   **Design-Specific Tagging:** A zero-shot classification layer on top of CLIP, combined with a specialized color extractor to identify brand palettes.

## 2. Pipeline Workflow
1.  **Ingestion:** Asset is uploaded to S3.
2.  **Preprocessing:** Image resizing, normalization, and transparency handling (converting RGBA to RGB with white background for design assets).
3.  **Embedding Generation:** Generate a 512 or 768-dimensional vector using the CLIP ViT-L/14 backbone.
4.  **Auto-Tagging:** 
    *   **Generic Tags:** Objects, scenes, and moods.
    *   **Design Tags:** Illustration style (Flat, 3D, Skeuomorphic), Layout type (Mobile, Web, Print), and UI Components.
5.  **Color Analysis:** K-Means clustering in Lab color space to extract dominant Hex codes.
6.  **Indexing:** Push metadata to PostgreSQL and Vectors to Pinecone/Milvus.

## 3. Visual Search Mechanism
We use **Cosine Similarity** to compare the embedding of a search query (either a text string or a reference image) against the indexed library.