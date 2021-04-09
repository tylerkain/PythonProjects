from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_all_posts(url, links):
    url_request = request(url)
    response = urlopen(url_request)
    soup = BeautifulSoup(response)
    for a in soup.find_all('a'):
        try:
            url = a['href']
            title = a['title']
            if title == "older Posts":
                print(title, url)
                links.append(url)
                get_all_posts(url,links)
        except:
            title = ''
    return
blogUrl = " "
