import docx
from pathlib import Path
from tqdm import tqdm
import spacy

nlp = spacy.load("en_core_web_sm")

p = Path('testsamples')  # make path object with samples

Path("testsamples_txt").mkdir(parents=True, exist_ok=True)  # create txt dir if not exist

for file in tqdm(p.iterdir()):
    doc = docx.Document(file)
    with open('testsamples_txt/' + file.stem + '.txt', 'w+') as w_file:
        for line in doc.paragraphs:
            d = nlp(line.text)
            for sent in d.sents:
                w_file.write(sent.text + '\n')
    with open('testsamples_txt/' + file.stem + '.ann', 'w+') as w_file:
        pass
