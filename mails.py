import requests
import bs4
import re

prefix = "https://www.google.ca/search?q=clothes+store+vancouver+online&newwindow=1&ei=QqkJZNiuMqKy2roP4tmVoA4&start="
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


def get_weblink(page, weblink):
    url = prefix + str((page-1)*10)
    html = requests.request(url=url, method='GET')
    soup = bs4.BeautifulSoup(html.text, 'lxml')
    weblink = []
    for item in soup.find_all("a"):
        if item['href'][:4] == '/url':
            weblink.append(item['href'][7:])
    weblink = weblink[:-2]
    return weblink


def get_mail(weblink):
    for l in weblink:
        html = requests.request(url=l, method='GET', timeout=5)
        match = re.search(pattern, html.text)
        if match:
            f = open('mails.txt', 'w')
            f.write(match.group()+'\n')


for i in range(2, 1000):
    webs = []
    webs = get_weblink(i, webs)
    get_mail(webs)
