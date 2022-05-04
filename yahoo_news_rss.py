import requests
import datetime


def savexml(topic):
    URL = f"https://news.yahoo.co.jp/rss/topics/{topic}.xml"
    now = datetime.datetime.now()
    filename = f"{now:%Y-%m-%d-%H}-{topic}.xml"
    r = requests.get(URL)
    with open(filename, "a") as f:
        f.write(r.text)
    return filename


topics = {"主要": "top-pics", "国内": "domestic", "国際": "world", "IT": "it"}

for key, topic in topics.items():
    filename = savexml(topic)
    print(f"{key} => {filename}")

# savexml("it")
