import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

class ColorAnalyzer:
    @staticmethod
    def extract_palette(image: Image.Image, num_colors: int = 5) -> List[str]:
        """Extracts dominant colors from an image using K-Means clustering."""
        # Resize for faster processing
        img = image.copy().resize((100, 100))
        img_data = np.array(img)
        
        # Flatten and remove alpha channel if exists
        pixels = img_data[:, :, :3].reshape(-1, 3)
        
        # Fit K-Means
        kmeans = KMeans(n_clusters=num_colors, n_init=10)
        kmeans.fit(pixels)
        
        colors = kmeans.cluster_centers_.astype(int)
        
        # Convert to Hex
        return [f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}".upper() for c in colors]