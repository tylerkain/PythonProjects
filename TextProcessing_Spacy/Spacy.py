import spacy
from pathlib import Path

nlp = spacy.load("en_core_web_sm")

doc1 = nlp(Path('Cell_Behavior_Similarities.txt').read_text())
doc2 = nlp(Path("Plant_Cells_Silimarites.txt").read_text())

print(doc1.text)
