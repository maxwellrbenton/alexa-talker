from playsound import playsound
import pyttsx3
import time
import random

engine = pyttsx3.init()
# playsound('calls/call_1.m4a')

commonWordList = [line.rstrip('\n') for line in open('phrase-content/most-common-words.txt')]
placeList = [line.rstrip('\n') for line in open('phrase-content/places.txt')]
animalList = [line.rstrip('\n') for line in open('phrase-content/animals.txt')]

def appendAlexa():
  return "Alexa, "

def speechToText(text):
  engine.say(text)
  engine.runAndWait()

def askAnimalAndLocation():
  animal = animalList[random.randint(1,len(animalList))]
  place = placeList[random.randint(1,len(placeList))]
  query = appendAlexa() + "How many " + animal + "s are there in " + place + "?"
  speechToText(query)

def askAboutThing():
  flip = random.random()
  if flip < 0.5:
    thing = animalList[random.randint(1,len(animalList))]
  else:
    thing = placeList[random.randint(1,len(placeList))]
  query = appendAlexa() + "Tell me about " + thing
  speechToText(query)

def lowerVolume():
  command = appendAlexa() + "Turn volume down to zero"
  speechToText(command)

def midVolume():
  command = appendAlexa() + "Set the volume to five"
  speechToText(command)

def loop():
  max = random.randint(5,20)
  i = 1

  while i < max:
    flip = random.random()
    if flip < 0.5:
      askAnimalAndLocation()
    else:
      askAboutThing()
    i += 1
    wait = random.randint(20,300)
    time.sleep(wait)

def run():
  lowerVolume()
  time.sleep( 4 )
  loop()
  midVolume()
