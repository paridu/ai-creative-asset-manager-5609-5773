import pytest

@pytest.mark.asyncio
async def test_asset_upload_flow(client):
    """Tests the full cycle from upload to metadata retrieval."""
    # 1. Simulate file upload
    files = {'file': ('test_design.png', b'fake-image-content', 'image/png')}
    response = await client.post("/api/v1/assets/upload", files=files)
    
    assert response.status_code == 202 # Accepted for processing
    asset_id = response.json()["asset_id"]
    
    # 2. Check processing status
    status_resp = await client.get(f"/api/v1/assets/{asset_id}/status")
    assert status_resp.status_code == 200
    assert status_resp.json()["status"] in ["processing", "completed"]

@pytest.mark.asyncio
async def test_search_endpoint(client):
    """Tests the semantic search API."""
    params = {"q": "modern website header", "limit": 10}
    response = await client.get("/api/v1/search", params=params)
    
    assert response.status_code == 200
    assert isinstance(response.json()["results"], list)
    assert "score" in response.json()["results"][0] # Ensure similarity score is returned