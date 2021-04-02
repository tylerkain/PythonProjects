from string import punctuation
import nltk
from nltk.collocations import *
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

text = 'Mary had a little lamb. Her fleece was white as snow'

sents = sent_tokenize(text)
print(sents)

words = [word_tokenize(sent) for sent in sents]
print(words)

StopWords = set(stopwords.words('english') + list(punctuation))
stopwords_amend = [word for word in word_tokenize(text) if word not in StopWords]
print(stopwords_amend)
print(StopWords)

bigrams = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(stopwords_amend)
word = sorted(finder.ngram_fd.items())
print(word)