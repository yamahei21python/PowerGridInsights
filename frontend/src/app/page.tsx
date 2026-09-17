import { Zap, Target, TrendingUp, Calendar as CalendarIcon } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen px-6 py-6 lg:px-24">
      {/* Header */}
      <header className="mb-16 flex flex-col xl:flex-row xl:items-center justify-between gap-12">
        <div className="flex-1">
          <h1 className="text-5xl md:text-6xl font-black tracking-tighter text-white mb-6 flex flex-wrap items-center gap-4">
            <span className="inline-flex items-center justify-center px-6 md:px-10 py-2 md:py-3.5 bg-[#10b981] text-black rounded-xl italic shadow-[0_0_30px_rgba(16,185,129,0.3)] transform -skew-x-6">
              Power
            </span>
            <span className="drop-shadow-[0_0_20px_rgba(16,185,129,0.6)]">Grid Insights</span>
          </h1>
          <p className="text-ui-secondary text-lg max-w-xl font-light leading-relaxed">
            蓄電池・電力業界の本質を抽出。<br className="hidden md:block" />
            構造化されたインサイトを提供。
          </p>
        </div>
      </header>

      {/* Content */}
      <div className="grid grid-cols-1 gap-6">
        <section className="intelligence-card p-8 md:p-10 relative overflow-hidden group">
          <div className="flex flex-col lg:flex-row gap-12 relative z-10">
            <div className="flex-1">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-brand-emerald/10 text-brand-emerald text-[10px] font-bold mb-8 border border-brand-emerald/20 uppercase tracking-widest">
                <Target size={12} strokeWidth={1.5} />
                <span>Power Grid Insights</span>
              </div>
              
              <h2 className="text-3xl font-medium text-white mb-8 leading-tight tracking-tight">
                蓄電池・電力業界ニュース
              </h2>

              <div className="space-y-5">
                <div className="flex gap-4">
                  <div className="mt-2.5 w-1.5 h-1.5 rounded-full bg-brand-emerald shrink-0 shadow-[0_0_8px_rgba(62,207,142,0.6)]" />
                  <p className="text-ui-secondary leading-relaxed font-light">
                    系統用蓄電池、需給調整市場、容量市場の最新動向
                  </p>
                </div>
                <div className="flex gap-4">
                  <div className="mt-2.5 w-1.5 h-1.5 rounded-full bg-brand-emerald shrink-0 shadow-[0_0_8px_rgba(62,207,142,0.6)]" />
                  <p className="text-ui-secondary leading-relaxed font-light">
                    VPP、DR、EV充電に関する業界ニュース
                  </p>
                </div>
                <div className="flex gap-4">
                  <div className="mt-2.5 w-1.5 h-1.5 rounded-full bg-brand-emerald shrink-0 shadow-[0_0_8px_rgba(62,207,142,0.6)]" />
                  <p className="text-ui-secondary leading-relaxed font-light">
                    補助金、制度改正の自動情報収集
                  </p>
                </div>
              </div>
            </div>

            <div className="lg:w-1/3 flex flex-col">
              <div className="h-full bg-white/[0.02] border border-white/5 rounded-lg p-8 relative">
                <div className="flex items-center gap-2 mb-6 text-brand-emerald/80 font-bold text-[10px] uppercase tracking-[0.2em]">
                  <TrendingUp size={16} strokeWidth={1.5} />
                  <span>Industry Insight</span>
                </div>
                <div className="text-ui-secondary leading-relaxed italic text-sm md:text-base font-light">
                  &ldquo;AIによる自動分析で、膨大な業界ニュースから本質的なインサイトを抽出します。&rdquo;
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>

      {/* Footer */}
      <footer className="mt-32 pb-12 border-t border-white/5 pt-12 flex flex-col md:flex-row justify-between items-center gap-8 text-ui-muted">
        <div className="flex items-center gap-6">
          <span className="font-mono text-[10px] tracking-[0.3em] uppercase">© 2026 Power Grid Insights</span>
        </div>
      </footer>
    </div>
  );
}
