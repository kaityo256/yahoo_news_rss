import xml.etree.ElementTree as ET


def read_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for title in root.find('channel').iterfind('item/title'):
        print(title.text)


read_xml("data/2022-09-22-17-top-picks.xml")
