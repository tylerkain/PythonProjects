from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import defaultdict
from heapq import nlargest
from nltk.probability import FreqDist

article = ""


def gettext(url):
    page = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, features='lxml')
    text = " ".join(map(lambda p: p.text, soup.find_all('article')))
    return text.encode('ascii', errors='replace').replace('?', " ")


def summarize(text, n):
    sents = sent_tokenize(text)

    assert n <= len(sents)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation))

    word_sent = [word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)

    ranking = defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    sents_idx = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]