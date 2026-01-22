from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.endpoints import assets, search
from src.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend API for ARCHIVE-AI Asset Management and Semantic Search",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(assets.router, prefix="/api/v1/assets", tags=["Assets"])
app.include_router(search.router, prefix="/api/v1/search", tags=["AI Search"])

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ARCHIVE-AI Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)