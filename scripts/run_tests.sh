#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting ARCHIVE-AI Test Suite..."

# 1. Run Unit & Integration Tests
echo "--- Running Backend Tests ---"
pytest tests/test_api_endpoints.py --cov=src --cov-report=html

# 2. Run AI Accuracy Benchmarks
echo "--- Running AI Model Validation ---"
pytest tests/test_ai_accuracy.py -v

# 3. Run E2E Playwright Tests
echo "--- Running Frontend E2E Tests ---"
npx playwright test tests/e2e/

echo "✅ All tests passed successfully!"