import { test, expect } from '@playwright/test';

test.describe('Designer Workflow: Asset Discovery', () => {
  
  test('should allow a designer to search and filter assets', async ({ page }) => {
    // 1. Navigate to Dashboard
    await page.goto('http://localhost:3000/dashboard');
    
    // 2. Perform Semantic Search
    const searchInput = page.getByPlaceholder(/search your creative brain/i);
    await searchInput.fill('neon futuristic branding');
    await searchInput.press('Enter');
    
    // 3. Verify AI results appear
    await expect(page.locator('.asset-card')).toBeVisible();
    
    // 4. Test AI Tag Filtering
    const firstTag = page.locator('.tag-chip').first();
    const tagName = await firstTag.innerText();
    await firstTag.click();
    
    // 5. Verify URL updates with filter
    await expect(page).toHaveURL(new RegExp(`tag=${tagName}`));
  });

  test('should show empty state for nonsensical queries', async ({ page }) => {
    await page.goto('http://localhost:3000/dashboard');
    await page.getByPlaceholder(/search/i).fill('xyz123nothingmatchesrhis');
    await page.keyboard.press('Enter');
    
    await expect(page.getByText(/no assets found/i)).toBeVisible();
  });
});