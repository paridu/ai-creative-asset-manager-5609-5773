-- Main Metadata Table
CREATE TABLE assets (
    id UUID PRIMARY KEY,
    owner_id UUID NOT NULL,
    filename TEXT NOT NULL,
    s3_path TEXT NOT NULL,
    mime_type VARCHAR(50),
    file_size BIGINT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    processing_status VARCHAR(20) DEFAULT 'PENDING'
);

-- AI Extracted Metadata
CREATE TABLE asset_metadata (
    asset_id UUID REFERENCES assets(id),
    tags TEXT[],
    dominant_colors TEXT[],
    ocr_content TEXT,
    ai_description TEXT,
    PRIMARY KEY (asset_id)
);

-- User/Workspace Table
CREATE TABLE workspaces (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    owner_id UUID NOT NULL
);