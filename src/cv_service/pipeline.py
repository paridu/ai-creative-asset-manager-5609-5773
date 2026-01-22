from PIL import Image
import io
from .models import ArchiveCVModel
from .color_extractor import ColorAnalyzer

class AssetProcessor:
    def __init__(self):
        self.cv_model = ArchiveCVModel()
        self.color_engine = ColorAnalyzer()

    def process_new_asset(self, image_bytes: bytes) -> dict:
        """
        Main orchestration logic for asset ingestion.
        Returns metadata, tags, and embeddings.
        """
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # 1. Visual Embedding for Search
        embedding = self.cv_model.get_image_embedding(image)
        
        # 2. AI Auto-Tagging
        tags = self.cv_model.generate_tags(image)
        
        # 3. Color Extraction
        palette = self.color_engine.extract_palette(image)
        
        return {
            "embedding": embedding.tolist(),
            "tags": tags,
            "palette": palette,
            "metadata": {
                "width": image.width,
                "height": image.height,
                "aspect_ratio": round(image.width / image.height, 2)
            }
        }