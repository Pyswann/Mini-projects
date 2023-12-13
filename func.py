import requests
from bs4 import BeautifulSoup


def title_gen(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    get_title = soup.find('title')
    for title in get_title:
        item = title.text
    return item

def get_h2s(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    h2_tags = soup.findAll("h2")
    h2_texts = []
    for h2_tag in h2_tags:
        h2_texts.append(h2_tag.get_text())
    return h2_texts


def get_h3s(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    h3_tags = soup.findAll("h3")
    h3_texts = []
    for h3_tag in h3_tags:
        h3_texts.append(h3_tag.get_text())
    return h3_texts

def get_p(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    para = soup.findAll("p")
    p = []
    for pa in para:
        p.append(pa.get_text())
    return p