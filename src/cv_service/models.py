import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from typing import List, Dict
import numpy as np
from .config import MODEL_ID, DEVICE, DESIGN_CANDIDATE_LABELS

class ArchiveCVModel:
    def __init__(self):
        self.model = CLIPModel.from_pretrained(MODEL_ID).to(DEVICE)
        self.processor = CLIPProcessor.from_pretrained(MODEL_ID)
        self.labels = DESIGN_CANDIDATE_LABELS

    def get_image_embedding(self, image: Image.Image) -> np.ndarray:
        """Generates a normalized vector embedding for visual search."""
        inputs = self.processor(images=image, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            image_features = self.model.get_image_features(**inputs)
        
        # Normalize the embedding
        image_features /= image_features.norm(dim=-1, keepdim=True)
        return image_features.cpu().numpy().flatten()

    def generate_tags(self, image: Image.Image, threshold: float = 0.25) -> List[str]:
        """Performs zero-shot classification to generate design-specific tags."""
        inputs = self.processor(
            text=self.labels, 
            images=image, 
            return_tensors="pt", 
            padding=True
        ).to(DEVICE)

        with torch.no_grad():
            outputs = self.model(**inputs)
            # Retrieve probabilities via softmax
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1).cpu().numpy()[0]

        # Filter tags by threshold
        detected_tags = [
            self.labels[i] for i, prob in enumerate(probs) if prob > threshold
        ]
        return detected_tags

    def get_text_embedding(self, query: str) -> np.ndarray:
        """Converts search text into a vector for semantic lookup."""
        inputs = self.processor(text=[query], return_tensors="pt", padding=True).to(DEVICE)
        with torch.no_grad():
            text_features = self.model.get_text_features(**inputs)
        
        text_features /= text_features.norm(dim=-1, keepdim=True)
        return text_features.cpu().numpy().flatten()