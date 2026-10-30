# gembally.com ホームページ

## ページ構成

| ファイル | 公開URL | 内容 |
|---|---|---|
| index.html | / | トップ |
| philosophy.html | /philosophy | 考え方 |
| services.html | /services | できること |
| pricing.html | /pricing | 料金 |
| about.html | /about | 代表について |
| faq.html | /faq | よくある質問 |
| contact.html | /contact | お問い合わせ（無料初回対話） |
| privacy.html | /privacy | プライバシーポリシー（下書き） |

## 編集のしかた

各ページの本文は `_src/pages/` にあります。共通のヘッダー・フッター・申込ボタンは `_src/build.py`、デザインは `_src/base.css` と `_src/pages.css` です。
編集したら `python3 _src/build.py` を実行すると、サイト直下のHTMLと `assets/style.css` が作り直されます（直下のHTMLは直接編集しないでください）。

## その他のファイル

- `CNAME` … GitHub Pagesで独自ドメインを使うための設定
- `assets/` … ロゴ（B案・横組み、ライト用とダーク用）とスタイルシート
- `favicon.ico` `favicon.svg` `apple-touch-icon.png` `icon-192/512.png` `site.webmanifest` … ブラウザやスマホのアイコン
- `ogp.png` … SNSでリンクを共有したときの画像（元ファイルは gembally-logo/final/）

## 公開前に埋める項目（ページ内で「要確認」と表示される箇所）

1. 代表者のお名前（漢字表記）と写真
2. ~~料金が税別か税込か~~ → 税込表示に決定（金額は据え置き）
3. ~~面談の時間帯の表記~~ → 「平日の夜と土日」で確定
4. ~~予約ページのURL~~ → 設定済み（Googleカレンダーの予約スケジュール：https://calendar.app.google/KJyGgtW9s8NWhhgC6）
5. ~~問い合わせ用メールアドレス~~ → contact@gembally.com（Workspaceのエイリアス）で受信確認済み。お問い合わせページとプライバシーポリシーに掲載済み
6. noteのURL
7. ~~プライバシーポリシーの下書きの確認と制定日~~ → 2026年10月30日制定で確定
8. 代表ページの経歴・想いの文章（下書き）と写真

## 公開手順（静的サイト＋GitHub Pagesを選んだ場合）

1. GitHubで空のリポジトリを作成（例：`gembally-site`、Public）
2. このフォルダの中身をpushし、Settings → Pages で main ブランチを公開元に設定
3. Custom domain に `gembally.com` を設定し、Enforce HTTPS をオン
4. Squarespace Domains の DNS設定で以下を追加（既存のMX・TXTなどメール用のレコードは消さない）

| 種類 | ホスト | 値 |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | yaaansho.github.io |

DNSの反映には数分〜最大48時間かかります。
