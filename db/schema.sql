-- PostgreSQL Schema for ARCHIVE-AI
-- Purpose: Store structured metadata, user relationships, and asset hierarchies.

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Users & Organizations
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    org_id UUID REFERENCES organizations(id),
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255),
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Asset Management
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    org_id UUID REFERENCES organizations(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE assets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(id),
    uploader_id UUID REFERENCES users(id),
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL, -- S3 URL or MinIO path
    file_type VARCHAR(50), -- e.g., 'figma', 'psd', 'png', 'svg'
    file_size BIGINT,
    mime_type VARCHAR(100),
    thumbnail_url TEXT,
    version INT DEFAULT 1,
    is_deleted BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. AI-Extracted Metadata
CREATE TABLE asset_tags (
    id SERIAL PRIMARY KEY,
    asset_id UUID REFERENCES assets(id) ON DELETE CASCADE,
    tag_name VARCHAR(100) NOT NULL,
    confidence_score FLOAT, -- Provided by AI model (0.0 to 1.0)
    source VARCHAR(50) DEFAULT 'ai', -- 'ai' or 'manual'
    UNIQUE(asset_id, tag_name)
);

CREATE TABLE asset_colors (
    id SERIAL PRIMARY KEY,
    asset_id UUID REFERENCES assets(id) ON DELETE CASCADE,
    hex_code CHAR(7) NOT NULL, -- e.g., #FFFFFF
    percentage FLOAT, -- Area of image covered by this color
    is_dominant BOOLEAN DEFAULT FALSE
);

CREATE TABLE asset_fonts (
    id SERIAL PRIMARY KEY,
    asset_id UUID REFERENCES assets(id) ON DELETE CASCADE,
    font_family VARCHAR(100) NOT NULL,
    font_weight VARCHAR(50)
);

-- 4. Search & Indexing
-- Vector Database ID mapping (Pinecone/Milvus ID to Postgres ID)
CREATE TABLE vector_index_map (
    vector_id UUID PRIMARY KEY, -- Matches the ID used in Vector DB
    asset_id UUID REFERENCES assets(id) ON DELETE CASCADE,
    model_version VARCHAR(50), -- e.g., 'clip-vit-b-32'
    indexed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indices for performance
CREATE INDEX idx_assets_project ON assets(project_id);
CREATE INDEX idx_asset_tags_name ON asset_tags(tag_name);
CREATE INDEX idx_assets_type ON assets(file_type);