from pathlib import Path
import imageio
from wordcloud import WordCloud

text = Path('Cell Behaviors.txt').read_text()
mask_image = imageio.imread('mask_leaf.png')

word_cloud = WordCloud(colormap='prism', mask=mask_image, background_color='white')
word_cloud = word_cloud.generate(text)
word_cloud = word_cloud.to_file('CellBehavior.png')
