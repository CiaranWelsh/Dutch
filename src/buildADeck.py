import pandas as pd
import os
import genanki
from gtts import gTTS


SRC_DIR = os.path.join(os.path.dirname(__file__))
PROJ_DIR = os.path.dirname(SRC_DIR)
DECK_CSV = os.path.join(SRC_DIR, "chapters0-6.txt")
DECK_APKG = os.path.join(PROJ_DIR, "dutch.apkg")
MP3_DIR = os.path.join(SRC_DIR, "mp3")

assert os.path.isfile(DECK_CSV)


def genSound(id, dutchText, playSound=False, overwrite=True):
    fname = os.path.join(MP3_DIR, f"{id}.mp3")
    if not overwrite and os.path.isfile(fname):
        return fname
    myobj = gTTS(text=dutchText, lang="nl", slow=False)
    myobj.save(fname)
    if playSound:
        os.system(f"mpg321 {fname}")
    return fname


my_model = genanki.Model(
    1607392319,
    'LanguageModel',
    fields=[
        {'name': 'English'},
        {'name': 'Dutch'},
    ],
    templates=[
        {
            'name': 'Dutch',
            'qfmt': '{{English}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Dutch}}',
        },
    ])

# print(my_model)
my_deck = genanki.Deck(
    2059400110,
    'DutchDeck')

my_package = genanki.Package(my_deck)

df = pd.read_csv(DECK_CSV)

print(df)

def checkLines():
    with open(DECK_CSV) as f:
        txt = f.read()

    for line in txt.split("\n"):
        if "," not in line:
            print(line)

        import re
        match = re.findall("\..*\.", line)
        if match != []:
            print(match)




for idx, (nl, eng) in df.iterrows():
    fname = genSound(idx, nl, playSound=False, overwrite=True)
    print(fname)
    my_package.media_files.append(fname)
    my_deck.add_note(genanki.Note(my_model, [eng, f'"{nl}[sound:{idx}.mp3]"'], guid=idx))

genanki.Package(my_deck).write_to_file('Dutch.apkg')
