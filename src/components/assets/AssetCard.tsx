import React from 'react';
import { ExternalLink, Tag, MoreHorizontal } from 'lucide-react';

interface AssetProps {
  id: string;
  thumbnail: string;
  name: string;
  tags: string[];
  colors: string[];
  type: string;
}

const AssetCard = ({ asset }: { asset: AssetProps }) => {
  return (
    <div className="group bg-white border border-surface-200 rounded-2xl overflow-hidden hover:shadow-xl hover:border-brand-200 transition-all duration-300">
      <div className="relative aspect-square bg-surface-100 overflow-hidden">
        <img 
          src={asset.thumbnail} 
          alt={asset.name}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
        />
        <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-all flex items-center justify-center opacity-0 group-hover:opacity-100">
          <button className="p-2 bg-white rounded-full shadow-lg hover:scale-110 transition-transform">
            <ExternalLink size={20} className="text-brand-900" />
          </button>
        </div>
        <div className="absolute top-2 right-2">
          <span className="px-2 py-1 bg-white/90 backdrop-blur-sm text-[10px] font-bold rounded-md shadow-sm uppercase">
            {asset.type}
          </span>
        </div>
      </div>

      <div className="p-4">
        <div className="flex justify-between items-start mb-2">
          <h3 className="font-semibold text-gray-900 truncate flex-1">{asset.name}</h3>
          <button className="text-gray-400 hover:text-gray-600">
            <MoreHorizontal size={18} />
          </button>
        </div>

        <div className="flex flex-wrap gap-1 mb-3">
          {asset.tags.slice(0, 3).map((tag) => (
            <span key={tag} className="flex items-center gap-1 px-2 py-0.5 bg-surface-100 text-gray-500 text-[10px] rounded-full">
              <Tag size={10} />
              {tag}
            </span>
          ))}
          {asset.tags.length > 3 && (
            <span className="text-[10px] text-gray-400 py-0.5">+{asset.tags.length - 3}</span>
          )}
        </div>

        <div className="flex items-center gap-1.5 border-t border-surface-100 pt-3">
          <div className="flex -space-x-1">
            {asset.colors.map((color, i) => (
              <div 
                key={i}
                className="w-4 h-4 rounded-full border border-white shadow-sm"
                style={{ backgroundColor: color }}
              />
            ))}
          </div>
          <span className="text-[10px] text-gray-400 ml-auto">AI Processed</span>
        </div>
      </div>
    </div>
  );
};

export default AssetCard;