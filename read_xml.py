import glob
import datetime


import xml.etree.ElementTree as ET
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
tokenizer = BertTokenizer.from_pretrained("daigo/bert-base-japanese-sentiment")
model = BertForSequenceClassification.from_pretrained(
    "daigo/bert-base-japanese-sentiment")
sentiment_analyzer = pipeline(
    "sentiment-analysis", model=model, tokenizer=tokenizer)


reference_date = datetime.datetime.strptime('2022-01-01', '%Y-%m-%d')


def hours_from_standard_time(filename, reference_date):
    """
    ファイル名を受け取り、基準となる時刻からの経過時間(hour)を返す関数
    """
    datestr = filename[5:18]
    current_date = datetime.datetime.strptime(datestr, '%Y-%m-%d-%H')
    dt = current_date - reference_date
    hours = int(dt.total_seconds() / 3600)
    return hours


def get_score(text):
    result = sentiment_analyzer(text)[0]
    score = result['score']
    if result['label'] == "ネガティブ":
        score = -score
    return score


def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    score = []
    for title in root.find('channel').iterfind('item/title'):
        title = title.text
        score.append(get_score(title))
    return sum(score) / len(score)


def topic_analysis(topic):
    outputfile = f"{topic}.dat"
    with open(outputfile, "w") as f:
        files = f"data/*-{topic}.xml"
        for filename in glob.glob(files):
            hours = hours_from_standard_time(filename, reference_date)
            score = read_xml(filename)
            f.write(f"{hours} {score}\n")
    print(f"generated {outputfile}")


def main():
    topics = ["top-picks", "domestic", "world", "it"]
    for topic in topics:
        topic_analysis(topic)


main()
