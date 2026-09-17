import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Power Grid Insights",
  description: "蓄電池・電力業界のニュース収集・分析アプリケーション",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
