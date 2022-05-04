import requests
import datetime


def savexml(topic):
    URL = f"https://news.yahoo.co.jp/rss/topics/{topic}.xml"
    now = datetime.datetime.now()
    filename = f"{now:%Y-%m-%d-%H}-{topic}.xml"
    r = requests.get(URL)
    with open(filename, "a") as f:
        f.write(r.text)


savexml("it")
