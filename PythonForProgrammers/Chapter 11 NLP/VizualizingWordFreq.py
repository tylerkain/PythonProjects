

# Loading the Data
from pathlib2 import Path
from textblob import TextBlob
from nltk.corpus import stopwords
from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt

blob = TextBlob(Path('Plant Cells.txt').read_text())
stop_words = stopwords.words('english')

# Getting the Word Frequencies
items = blob.word_counts.items()

# Eliminating the Stop Words
items = [item for item in items if item[0] not in stop_words]

# Sorting the Words by Frequency


sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# Getting the Top 20 Words
top20 = sorted_items[1:21]

# Convert top20 to a DataFrame

df = pd.DataFrame(top20, columns=['word', 'count'])

print(df)

# Visualizing the DataFrame
axes = df.plot.bar(x='word', y='count', legend=False)
plt.gcf().tight_layout()
plt.show()


