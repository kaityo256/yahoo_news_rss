# Yahoo NEWSのRSSを読み込むスクリプト

## 概要

Yahoo! NewsのRSSをウェブスクレイピングにより取得するスクリプト。実行すると`YYYY-MM-DD-HH-topic.xml`という形式で`data`ディレクトリにXMLを保存する。

## 注意

ウェブスクレイピングについては、サーバの著作権や負荷、`robots.txt`に注意して実行してください。

## 必要ライブラリ

`request`が必要なので、なければインストールする。仮想環境を構築すると良い。

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install requests
python3 -m pip install tensorflow
python3 -m pip install torch
python3 -m pip install transformers
```

## 実行方法

```sh
python3 yahoo_news_rss.py
```

## 実行結果

```txt
主要 => data/2022-05-04-12-top-pics.xml
国内 => data/2022-05-04-12-domestic.xml
国際 => data/2022-05-04-12-world.xml
IT => data/2022-05-04-12-it.xml
```

## LICENSE

MIT
