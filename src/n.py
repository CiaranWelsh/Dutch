import anki


print(anki)
print(dir(anki))
from anki import ankidroid_pb2


import genanki
my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', 'Buenos Aires'])



my_deck = genanki.Deck(
  2059400110,
  'Country Capitals')

my_deck.add_note(my_note)



# genanki.Package(my_deck).write_to_file('output.apkg')


# Import the required module for text
# to speech conversion
from gtts import gTTS, lang, langs

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'gaan'

# Language in which you want to convert
language = 'nl'

print(lang.tts_langs())

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")












