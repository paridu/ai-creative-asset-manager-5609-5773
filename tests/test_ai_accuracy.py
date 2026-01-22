import pytest
import torch
import numpy as np
from sklearn.metrics import precision_score, recall_score
from src.ai.models import ClipInferenceEngine # Hypothetical model wrapper

def calculate_cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

class TestAIAccuracy:
    """
    Validation suite for the CLIP-based semantic engine.
    Uses a 'Ground Truth' set of images and expected search terms.
    """
    
    @pytest.fixture
    def ground_truth_data(self):
        return [
            {"query": "vibrant sunset", "asset_id": "asset_001", "path": "tests/data/sunset.jpg"},
            {"query": "minimalist typography", "asset_id": "asset_002", "path": "tests/data/font.png"},
            {"query": "dark mode dashboard", "asset_id": "asset_003", "path": "tests/data/ui.png"}
        ]

    def test_semantic_search_recall(self, ground_truth_data):
        model = ClipInferenceEngine()
        correct_retrievals = 0
        
        for item in ground_truth_data:
            # 1. Generate embedding for query
            query_vector = model.encode_text(item["query"])
            # 2. Generate embedding for actual image
            image_vector = model.encode_image(item["path"])
            
            similarity = calculate_cosine_similarity(query_vector, image_vector)
            
            # Threshold check: AI should recognize the correlation
            if similarity > 0.25: # CLIP thresholds are typically lower
                correct_retrievals += 1
        
        recall = correct_retrievals / len(ground_truth_data)
        assert recall >= 0.80, f"AI Search Recall dropped to {recall}"

    def test_tagging_precision(self):
        """Validates that auto-generated tags match human-labeled data."""
        model = ClipInferenceEngine()
        sample_img = "tests/data/nature_stock.jpg"
        expected_tags = {"tree", "green", "outdoor"}
        
        generated_tags = set(model.generate_tags(sample_img))
        
        intersection = expected_tags.intersection(generated_tags)
        precision = len(intersection) / len(generated_tags) if generated_tags else 0
        
        assert precision > 0.6, f"Auto-tagging precision too low: {precision}"