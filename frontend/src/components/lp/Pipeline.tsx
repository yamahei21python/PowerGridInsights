"use client";

import { motion } from "framer-motion";
import { Database, Brain, FileText, BarChart3 } from "lucide-react";

const steps = [
  {
    icon: Database,
    title: "収集",
    description: "20以上のソースから自動でニュースを収集",
    color: "text-blue-400",
  },
  {
    icon: Brain,
    title: "分析",
    description: "AIが重要度を判定し、関連ニュースをグループ化",
    color: "text-purple-400",
  },
  {
    icon: FileText,
    title: "要約",
    description: "業界インサイトを自動で生成",
    color: "text-brand-emerald",
  },
  {
    icon: BarChart3,
    title: "可視化",
    description: "カレンダー形式で直感的に表示",
    color: "text-orange-400",
  },
];

export default function Pipeline() {
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
            パイプライン
          </h2>
          <p className="text-ui-secondary font-light">
            収集から分析まで、全自動で実行
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          {steps.map((step, index) => (
            <motion.div
              key={step.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="intelligence-card p-8 text-center"
            >
              <div className={`inline-flex p-4 rounded-xl bg-white/5 mb-6 ${step.color}`}>
                <step.icon size={24} strokeWidth={1.5} />
              </div>
              <h3 className="text-lg font-medium text-white mb-3">
                {step.title}
              </h3>
              <p className="text-sm text-ui-secondary font-light">
                {step.description}
              </p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
