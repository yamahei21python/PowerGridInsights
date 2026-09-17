"use client";

import { motion } from "framer-motion";
import { Zap } from "lucide-react";

export default function Hero() {
  return (
    <section className="relative py-32 px-4 overflow-hidden">
      {/* Background Effects */}
      <div className="absolute inset-0 z-0 pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-[600px] h-[600px] bg-brand-emerald/5 blur-[150px] rounded-full opacity-40" />
        <div className="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-brand-emerald/3 blur-[100px] rounded-full opacity-30" />
      </div>

      <div className="max-w-7xl mx-auto text-center relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="flex flex-col items-center"
        >
          {/* Badge */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-brand-emerald/10 border border-brand-emerald/20 mb-8"
          >
            <Zap size={14} className="text-brand-emerald" />
            <span className="text-xs font-medium text-brand-emerald tracking-wide">
              AI-Powered Intelligence
            </span>
          </motion.div>

          {/* Main Title */}
          <h1 className="text-5xl md:text-7xl lg:text-8xl font-black tracking-tighter text-white mb-6 leading-none">
            <span className="inline-flex items-center justify-center px-8 md:px-12 py-3 md:py-4 bg-[#10b981] text-black rounded-2xl italic shadow-[0_0_40px_rgba(16,185,129,0.4)] transform -skew-x-6 mb-4">
              Power
            </span>
            <br />
            <span className="drop-shadow-[0_0_30px_rgba(16,185,129,0.7)]">
              Grid Insights
            </span>
          </h1>

          {/* Subtitle */}
          <p className="text-xl md:text-2xl text-ui-secondary font-light leading-relaxed max-w-2xl mx-auto mb-12">
            蓄電池・電力業界の本質を抽出。<br />
            構造化されたインサイトを提供。
          </p>

          {/* Stats */}
          <div className="flex flex-wrap justify-center gap-8 md:gap-16">
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-white mb-2">
                20+
              </div>
              <div className="text-xs text-ui-muted uppercase tracking-widest">
                ニュースソース
              </div>
            </div>
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-white mb-2">
                24h
              </div>
              <div className="text-xs text-ui-muted uppercase tracking-widest">
                自動更新
              </div>
            </div>
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-white mb-2">
                AI
              </div>
              <div className="text-xs text-ui-muted uppercase tracking-widest">
                分析・要約
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
