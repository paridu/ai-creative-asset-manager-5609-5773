import io
import PIL.Image
from typing import Tuple, List
import numpy as np

def generate_thumbnail(image_bytes: bytes, size=(300, 300)) -> bytes:
    """Generates a compressed thumbnail for the asset."""
    img = PIL.Image.open(io.BytesIO(image_bytes))
    img.thumbnail(size)
    output = io.BytesIO()
    img.save(output, format="JPEG", quality=85)
    return output.getvalue()

def extract_dominant_colors(image_bytes: bytes, num_colors=5) -> List[str]:
    """Extracts hex color codes using K-Means or simple sampling."""
    img = PIL.Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((50, 50))  # Resize to speed up processing
    pixels = np.array(img).reshape(-1, 3)
    
    # Simple logic to get top N colors (Simplified for brevity)
    # In production, use sklearn.cluster.KMeans
    colors = []
    for i in range(num_colors):
        color = pixels[np.random.choice(pixels.shape[0])]
        colors.append('#{:02x}{:02x}{:02x}'.format(*color))
    return list(set(colors))

def get_file_metadata(file_content: bytes, filename: str):
    """Extracts basic file metadata."""
    import magic
    mime = magic.Magic(mime=True)
    file_type = mime.from_buffer(file_content)
    size_bytes = len(file_content)
    
    return {
        "mime_type": file_type,
        "size_kb": round(size_bytes / 1024, 2),
        "extension": filename.split('.')[-1].lower()
    }