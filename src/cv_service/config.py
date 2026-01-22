# Design-centric labels for Zero-Shot Classification
DESIGN_CANDIDATE_LABELS = [
    "minimalist", "vibrant", "dark mode", "pastel", "flat design", 
    "3d render", "typography", "wireframe", "high fidelity",
    "branding", "illustration", "photography", "iconography",
    "web design", "mobile app design", "social media post",
    "geometric", "organic shapes", "corporate", "playful"
]

MODEL_ID = "openai/clip-vit-base-patch32"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"