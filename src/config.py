from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ARCHIVE-AI API"
    DATABASE_URL: str
    REDIS_URL: str
    S3_BUCKET_NAME: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    S3_ENDPOINT_URL: str
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str
    
    class Config:
        env_file = ".env"

settings = Settings()