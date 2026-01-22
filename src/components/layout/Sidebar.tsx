import React from 'react';
import { 
  LayoutDashboard, 
  Search, 
  FolderCanvas, 
  Tag, 
  Clock, 
  Settings, 
  PlusCircle,
  CloudUpload
} from 'lucide-react';

const Sidebar = () => {
  const navItems = [
    { icon: LayoutDashboard, label: 'Dashboard', active: true },
    { icon: FolderCanvas, label: 'Projects', active: false },
    { icon: Tag, label: 'AI Collections', active: false },
    { icon: Clock, label: 'Recent', active: false },
  ];

  return (
    <aside className="w-64 h-screen bg-white border-r border-surface-200 flex flex-col fixed left-0 top-0">
      <div className="p-6 flex items-center gap-2">
        <div className="w-8 h-8 bg-brand-500 rounded-lg flex items-center justify-center">
          <div className="w-4 h-4 bg-white rounded-full animate-pulse" />
        </div>
        <span className="font-bold text-xl tracking-tight text-brand-900">ARCHIVE-AI</span>
      </div>

      <nav className="flex-1 px-4 space-y-2 mt-4">
        <button className="w-full flex items-center gap-3 px-4 py-3 bg-brand-500 text-white rounded-xl shadow-lg shadow-brand-100 hover:bg-brand-600 transition-all mb-8">
          <CloudUpload size={20} />
          <span className="font-medium">Ingest Assets</span>
        </button>

        {navItems.map((item) => (
          <a
            key={item.label}
            href="#"
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-colors ${
              item.active 
              ? 'bg-brand-50 text-brand-600 font-semibold' 
              : 'text-gray-500 hover:bg-surface-100'
            }`}
          >
            <item.icon size={20} />
            {item.label}
          </a>
        ))}
      </nav>

      <div className="p-4 border-t border-surface-100">
        <button className="flex items-center gap-3 px-4 py-3 text-gray-500 hover:bg-surface-100 rounded-xl w-full">
          <Settings size={20} />
          <span>Settings</span>
        </button>
      </div>
    </aside>
  );
};

export default Sidebar;