# Xで他人のいいねを見るやつ

## ファイル一覧
- main.py
  - 実行ファイル
- sample_config.json
  - 各項目を埋めたのち、config.jsonにリネーム

## 実行環境
- Python3
  - requests

# 各項目の参照方法
- Bearer
  - AAAAAAAAAAAAAAAAAAAAAFQODgEAAAAAVHTp76lzh3rFzcHbmHVvQxYYpTw%3DckAlMINMjmCwxUcaXbAN4XqJVdgMJaHqNOFgPMK0zN1qLqLQCF
  - ネットで拾った
- auth_token
  - Chromeで𝕏を開く
  - デベロッパーツールを開く
  - Applicationタブ -> Storageを展開 -> Cookiesを展開
  - https://x.comを選択
  - auth_tokenのValueを選択してコピペ
- ct0
  - 同上の手順でct0のValueを選択してコピペ

- user_id
  - 空でOK
- screen_name
  - ユーザー名の@example
  - @は入れない

- count
  - 取得する個数
  - 任意

# メモ
- いつ使えなくなるかは知らん

# 偉大なる参照元
https://x.com/uikota/status/1801092079508135951
https://x.com/aruta2525/status/1617353011050975232
