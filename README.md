# Power Grid Insights

蓄電池・電力業界のニュース収集・分析アプリケーション

## 概要

Daigas Energyの電力関連商材（蓄電池、VPP、DR、EV充電等）に関連する業界ニュースを自動収集し、AIによる分析・インサイトを提供する情報ポータル。

## 技術スタック

- **Frontend**: Next.js 15 + Tailwind CSS 4
- **Backend**: Python 3.11
- **AI**: Gemini API (Google)
- **CI/CD**: GitHub Actions
- **Hosting**: Vercel
- **Storage**: GitHubリポジトリ内JSON

## 機能

### 1. ニュース収集（12時間自動）
- 国内ニュースソース: 13サイト
- 制度情報: 3サイト（経済産業省、OCCTO、資源エネルギー庁）
- 海外ニュースソース: 3サイト
- 自社情報: Daigas Energy公式

### 2. AI分析（12時間自動）
- トピック抽出・名寄せ
- 業界インサイト生成
- 関連記事のグループ化

### 3. フロントエンド
- カレンダー形式のニュース表示
- トピック別のインサイト表示
- 関連リンク集

## 収集領域

### 対象キーワード
- 蓄電池、系統用蓄電池、BESS
- 需給調整市場、容量市場
- VPP（仮想発電所）、DR（需給応答）
- EV充電、再エネ、PPA
- 補助金、制度改正

### ニュースソース

#### 国内（13サイト）
1. 蓄電所ネット (bess-net.jp)
2. BESS NEWS (bessnews.jp)
3. AI電気速報 (ai-denki-sokuho.com)
4. スマートグリッドフォーラム
5. 日経BP メガソーラービジネス
6. SOLAR JOURNAL
7. 新エネルギー新聞
8. PV Magazine Japan
9. エネルギーフォーラム
10. 電気新聞
11. 環境ビジネスオンライン
12. PR TIMES
13. 時事通信

#### 制度情報（3サイト）
14. 経済産業省
15. OCCTO
16. 資源エネルギー庁

#### 海外（3サイト）
17. Energy Storage News
18. PV Magazine
19. Utility Dive

## フォルダ構造

```
PowerGridInsights/
├── frontend/              # Next.js 15 フロントエンド
│   ├── src/
│   │   ├── app/           # App Router
│   │   ├── components/    # Reactコンポーネント
│   │   └── lib/           # ユーティリティ
│   ├── public/
│   ├── package.json
│   └── next.config.ts
├── src/                   # Python バックエンド
│   ├── config.py          # 設定
│   ├── types.py           # 型定義
│   ├── fetch/             # ニュース収集
│   ├── process/           # AI分析
│   ├── pipeline/          # パイプライン
│   └── utils/             # 共通ツール
├── .github/workflows/     # GitHub Actions
│   ├── fetch-12h.yml      # 12時間ごとニュース収集
│   └── analyze-24h.yml    # 24時間ごと分析
├── archive/               # アーカイブ
├── requirements.txt       # Python依存関係
└── README.md
```

## 開発手順

1. Python環境構築
2. ニュース収集モジュール開発
3. AI分析モジュール開発
4. Next.jsフロントエンド開発
5. GitHub Actions設定
6. Vercelデプロイ

## 参考

- EV News.Intelligence（既存プロジェクト）
- Daigas Energy公式サイト
