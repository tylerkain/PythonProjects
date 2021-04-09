import spacy
nlp = spacy.load('en')
doc = nlp(u'You flying to frisco')
print(doc)