# Notionデータベース更新スクリプト

## 仕様

### Qiita記事一覧書き出しスクリプト

Qiitaの記事一覧をデータベースに追加します。

[update_database_qiita.py](update_database_qiita.py)

## 必須環境

- Python

## 利用方法

- スプレッドシートを作成します。
- サービスアカウントを取得し、スプレッドシータへの。Pythonのファイルに記載されているスプレッドシートのURLをかえ、また、トークンもサービスアカウントのトークンを貼り付けてください。
- 各自利用するプラットフォーム上では必要な形にデータを整形してください。

## ライブラリ

- ['requests'](https://pypi.org/project/requests/)

## ライセンス

このリポジトリはMITライセンスにより保護されています。詳しくは[LICENSE.md](LICENSE.md)をご覧ください。
