import React from 'react';
import Sidebar from '@/components/layout/Sidebar';
import SmartSearch from '@/components/search/SmartSearch';
import AssetCard from '@/components/assets/AssetCard';

// Mock Data representing items from the Vector DB & Postgres
const MOCK_ASSETS = [
  {
    id: '1',
    name: 'Abstract Gradient Background',
    thumbnail: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&q=80&w=400',
    tags: ['Gradient', 'Modern', 'Hero Section', 'Vibrant'],
    colors: ['#4F46E5', '#EC4899', '#8B5CF6'],
    type: 'PNG'
  },
  {
    id: '2',
    name: 'Minimalist Icon Set',
    thumbnail: 'https://images.unsplash.com/photo-1614113143851-691590477b3c?auto=format&fit=crop&q=80&w=400',
    tags: ['Iconography', 'Stroke', 'Web App'],
    colors: ['#18181B', '#FFFFFF', '#71717A'],
    type: 'SVG'
  },
  {
    id: '3',
    name: 'Brand Style Guide - Summer 24',
    thumbnail: 'https://images.unsplash.com/photo-1558655146-d09347e92766?auto=format&fit=crop&q=80&w=400',
    tags: ['Branding', 'Typography', 'Summer'],
    colors: ['#F59E0B', '#10B981', '#3B82F6'],
    type: 'PDF'
  }
];

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-surface-50">
      <Sidebar />
      
      <main className="pl-64">
        <header className="p-8 pb-4">
          <div className="flex justify-between items-center mb-8">
            <div>
              <h1 className="text-2xl font-bold text-brand-900">Your Creative Brain</h1>
              <p className="text-gray-500">Search 2,482 assets indexed by ARCHIVE-AI</p>
            </div>
            <div className="flex gap-3">
              <div className="flex items-center gap-2 px-3 py-1.5 bg-green-50 text-green-700 rounded-full text-xs font-semibold">
                <div className="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse" />
                AI Sync Active
              </div>
            </div>
          </div>
          
          <SmartSearch />
        </header>

        <section className="p-8">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-semibold text-gray-900">Recent Ingested Assets</h2>
            <div className="flex gap-4 text-sm font-medium text-gray-500">
              <button className="text-brand-600 border-b-2 border-brand-500 pb-1">All Assets</button>
              <button className="hover:text-brand-600 transition-colors">Images</button>
              <button className="hover:text-brand-600 transition-colors">Vectors</button>
              <button className="hover:text-brand-600 transition-colors">Components</button>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {MOCK_ASSETS.map((asset) => (
              <AssetCard key={asset.id} asset={asset} />
            ))}
            {/* Repeat for visual fill */}
            {MOCK_ASSETS.map((asset) => (
              <AssetCard key={`${asset.id}-dup`} asset={asset} />
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}