import React, { useState } from 'react';
import { Search, Sparkles, Filter, X } from 'lucide-react';

const SmartSearch = () => {
  const [query, setQuery] = useState('');

  return (
    <div className="relative w-full max-w-3xl mx-auto">
      <div className="relative group">
        <div className="absolute inset-y-0 left-4 flex items-center pointer-events-none">
          <Sparkles className="text-brand-500 group-focus-within:animate-bounce" size={20} />
        </div>
        <input
          type="text"
          className="w-full pl-12 pr-24 py-4 bg-white border-2 border-surface-200 rounded-2xl focus:border-brand-500 outline-none shadow-sm transition-all text-lg placeholder:text-gray-400"
          placeholder="Try 'Vibrant summer vibes with blue gradients'..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <div className="absolute inset-y-0 right-4 flex items-center gap-2">
          {query && (
            <button onClick={() => setQuery('')} className="p-1 hover:bg-surface-100 rounded-full">
              <X size={16} className="text-gray-400" />
            </button>
          )}
          <div className="h-6 w-[1px] bg-surface-200 mx-1" />
          <button className="flex items-center gap-1 px-3 py-1.5 bg-surface-100 text-gray-600 rounded-lg hover:bg-surface-200 transition-colors">
            <Filter size={16} />
            <span className="text-sm font-medium">Filters</span>
          </button>
        </div>
      </div>
      
      {/* Search Suggestions (AI Intent) */}
      {query.length > 2 && (
        <div className="absolute top-full mt-2 w-full bg-white border border-surface-200 rounded-xl shadow-xl p-2 z-50">
          <div className="p-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">Semantic Suggestions</div>
          <button className="w-full text-left px-4 py-2 hover:bg-brand-50 rounded-lg text-sm text-gray-700 flex items-center gap-2">
             <Search size={14} className="text-brand-500" /> Search for visual style: <span className="font-semibold">"{query}"</span>
          </button>
        </div>
      )}
    </div>
  );
};

export default SmartSearch;