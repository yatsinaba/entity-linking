import docx
from pathlib import Path
import stanza
from tqdm import tqdm
import spacy

nlp = spacy.load("en_core_web_lg")

# stanza.download('en')
# nlp = stanza.Pipeline(lang='en', processors='tokenize')

p = Path('testsamples_txt')  # make path object with samples

for file in tqdm(p.iterdir()):
    with open(str(file)) as r_file:
        line_start_position = 0
        ent_counter = 1
        with open('testsamples_txt/' + file.stem + '.ann', 'w+') as w_file:
            for line in r_file:
                doc = nlp(line)
                ents = [(e.text, e.start_char + line_start_position, e.end_char + line_start_position, e.label_) for e
                        in doc.ents]
                for e in ents:
                    print("T{}\t{} {} {}\t{}".format(ent_counter, e[3], e[1], e[2],e[0].rstrip()), file=w_file)
                    ent_counter += 1
                line_start_position += len(line)
    break  # Убрать когд аотдебажишь запись ENT
