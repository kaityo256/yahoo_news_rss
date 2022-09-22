import requests
import datetime
import os

# データを保存するためのディレクトリ
# cronで実行する場合は絶対パスにすること
DATA_DIR = 'data'

# RSSのトピック名とRSSファイルの対応
topics = {"主要": "top-picks", "国内": "domestic", "国際": "world", "IT": "it"}


def savexml(topic):
    """
    RSSのトピックに対応する名前を受け取り、YYYY-MM-DD-HH-topic.xmlという名前で
    DATA_DIRに保存する
    """
    URL = f"https://news.yahoo.co.jp/rss/topics/{topic}.xml"
    now = datetime.datetime.now()
    filename = f"{DATA_DIR}/{now:%Y-%m-%d-%H}-{topic}.xml"
    r = requests.get(URL)
    with open(filename, "a") as f:
        f.write(r.text)
    return filename


if __name__ == '__main__':
    # DATA_DIRがなければ作る
    os.makedirs(DATA_DIR, exist_ok=True)
    # 各トピックごとにファイルに保存
    for key, topic in topics.items():
        filename = savexml(topic)
        print(f"{key} => {filename}")
