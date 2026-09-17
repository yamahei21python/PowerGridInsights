"use client";

import { motion } from "framer-motion";
import { Target, TrendingUp, Zap } from "lucide-react";

export default function DashboardPreview() {
  return (
    <section className="py-24 px-4">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-3xl md:text-4xl font-medium text-white mb-4 tracking-tight">
            ダッシュボードプレビュー
          </h2>
          <p className="text-ui-secondary font-light">
            構造化されたインサイトをすぐに確認
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="intelligence-card p-8 md:p-12 relative overflow-hidden"
        >
          {/* Background Glow */}
          <div className="absolute top-0 right-0 w-[400px] h-[400px] bg-brand-emerald/5 blur-[100px] rounded-full opacity-40 pointer-events-none" />

          <div className="relative z-10">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-brand-emerald/10 text-brand-emerald text-[10px] font-bold mb-8 border border-brand-emerald/20 uppercase tracking-widest">
              <Target size={12} strokeWidth={1.5} />
              <span>Topic #1</span>
            </div>

            <h3 className="text-2xl md:text-3xl font-medium text-white mb-6 leading-tight">
              系統用蓄電池の容量市場落札
            </h3>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="space-y-4">
                <div className="flex gap-4">
                  <div className="mt-2.5 w-1.5 h-1.5 rounded-full bg-brand-emerald shrink-0 shadow-[0_0_8px_rgba(62,207,142,0.6)]" />
                  <p className="text-ui-secondary leading-relaxed font-light">
                    2027年度対象の容量市場で、蓄電池約13.8万kWが全量落札
                  </p>
                </div>
                <div className="flex gap-4">
                  <div className="mt-2.5 w-1.5 h-1.5 rounded-full bg-brand-emerald shrink-0 shadow-[0_0_8px_rgba(62,207,142,0.6)]" />
                  <p className="text-ui-secondary leading-relaxed font-light">
                    約定価格は10,361円/kWで全エリア統一
                  </p>
                </div>
                <div className="flex gap-4">
                  <div className="mt-2.5 w-1.5 h-1.5 rounded-full bg-brand-emerald shrink-0 shadow-[0_0_8px_rgba(62,207,142,0.6)]" />
                  <p className="text-ui-secondary leading-relaxed font-light">
                    安定電源としての登録が必須条件
                  </p>
                </div>
              </div>

              <div className="bg-white/[0.02] border border-white/5 rounded-lg p-6">
                <div className="flex items-center gap-2 mb-4 text-brand-emerald/80 font-bold text-[10px] uppercase tracking-[0.2em]">
                  <TrendingUp size={14} strokeWidth={1.5} />
                  <span>Industry Insight</span>
                </div>
                <div className="text-ui-secondary leading-relaxed italic text-sm font-light">
                  &ldquo;容量市場は蓄電池事業の収益基盤を安定させる重要な制度。全量落札は市場の信頼性を示す。&rdquo;
                </div>
              </div>
            </div>

            <div className="mt-8 pt-8 border-t border-white/5">
              <div className="flex flex-wrap gap-3">
                <a
                  href="#"
                  className="group/link flex items-center justify-between gap-4 text-[11px] text-ui-muted hover:text-brand-emerald transition-all bg-white/[0.01] hover:bg-white/[0.03] p-3 rounded-md border border-white/5 active:scale-[0.98] max-w-md"
                >
                  <span className="truncate flex-1 font-medium italic">
                    蓄電所ネット - 容量市場落札結果
                  </span>
                  <Zap size={12} strokeWidth={1.5} className="shrink-0 text-brand-emerald/30 group-hover/link:text-brand-emerald" />
                </a>
                <a
                  href="#"
                  className="group/link flex items-center justify-between gap-4 text-[11px] text-ui-muted hover:text-brand-emerald transition-all bg-white/[0.01] hover:bg-white/[0.03] p-3 rounded-md border border-white/5 active:scale-[0.98] max-w-md"
                >
                  <span className="truncate flex-1 font-medium italic">
                    BESS NEWS - 市場動向分析
                  </span>
                  <Zap size={12} strokeWidth={1.5} className="shrink-0 text-brand-emerald/30 group-hover/link:text-brand-emerald" />
                </a>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
