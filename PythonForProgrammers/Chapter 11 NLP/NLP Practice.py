from textblob import TextBlob, Word
from nltk.corpus import stopwords

text = "Cells are the fundamental structural and functional units that make up a plant body, and adjust the behavior of the plant " \
       "in response to external information.  A plant body consists of many different cell types,"
'however, most plant cells do have a fundamental organization that includes numerous compartments called organelles, which are separated from each other by selectively permeable membranes.' \
'The outermost structure of a plant cell is the cell wall.  The volume of space occupied by the cell wall is called the apoplast.  ' \
'We will discuss the structure and functions of the cell wall in a later lecture.' \
'this lecture we will take a brief tour ofthe general structure and functions of the cell compartments.'

blob = TextBlob(text)
spanish_text = blob.translate(to='es')
sentence = blob.sentences
words = blob.words
tags = blob.tags
nouns = blob.noun_phrases
sentiment = blob.sentiment
sentiment_polarity = blob.sentiment.polarity
language = blob.detect_language()
print(nouns)
print(sentiment)
