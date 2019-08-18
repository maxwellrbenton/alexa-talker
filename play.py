from playsound import playsound
import pyttsx3
import time
import random

engine = pyttsx3.init()

# commonWordList = [line.rstrip('\n') for line in open('phrase-content/most-common-words.txt')]
placeList = [line.rstrip('\n') for line in open('phrase-content/places.txt')]
animalList = [line.rstrip('\n') for line in open('phrase-content/animals.txt')]

def speech_to_text(text):
  engine.say(text)
  engine.runAndWait()

def ask_animal_and_location():
  animal = animalList[random.randint(1,len(animalList))]
  place = placeList[random.randint(1,len(placeList))]
  query = "Alexa, how many " + animal + "s are there in " + place + "?"
  speechToText(query)

def ask_about_thing():
  flip = random.random()
  if flip < 0.5:
    thing = animalList[random.randint(1,len(animalList))]
  else:
    thing = placeList[random.randint(1,len(placeList))]
  query = "Alexa, tell me about " + thing
  speechToText(query)

def lower_volume():
  command = "Alexa, turn volume down to zero"
  speechToText(command)

def mid_volume():
  command = "Alexa, set the volume to five"
  speechToText(command)

def choose_phrase_type():
  flip = random.random()
  if flip < 0.5:
    ask_animal_and_location()
  else:
    ask_about_thing()

def run():
  lower_volume()
  time.sleep( 4 )
  choose_phrase_type()
  mid_volume()

run()
