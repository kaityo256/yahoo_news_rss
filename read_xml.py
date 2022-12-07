import glob

import xml.etree.ElementTree as ET
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
tokenizer = BertTokenizer.from_pretrained("daigo/bert-base-japanese-sentiment")
model = BertForSequenceClassification.from_pretrained("daigo/bert-base-japanese-sentiment")
sentiment_analyzer = pipeline("sentiment-analysis",model=model, tokenizer=tokenizer)

def get_score(text):
  result = sentiment_analyzer(text)[0]
  score = result['score']
  if result['label'] == "ネガティブ":
    score = -score
  return score

def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for title in root.find('channel').iterfind('item/title'):
      title = title.text
      score = get_score(title)
      print(f"{title} {score}")


read_xml("data/2022-12-07-19-world.xml")
