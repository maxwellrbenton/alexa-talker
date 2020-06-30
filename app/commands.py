from random import randint
from linereader import dopen

placeList = [line.rstrip('\n') for line in open('phrase-content/places.txt')]
animalList = [line.rstrip('\n') for line in open('phrase-content/animals.txt')]

def ask_about_animal():
  return "Alexa, tell me about " + animalList[randint(1,len(animalList))] + "s"

def ask_about_location():
  return "Alexa, tell me about " + placeList[randint(1,len(placeList))]

def ask_about_animal_and_location():
  return "Alexa, how many " + animalList[randint(1,len(animalList))] + "s are there in " + placeList[randint(1,len(placeList))] + "?"

def ask_to_define():
  file = dopen('words.txt')
  random_line = file.getline(randint(1, 400000))
  return "Alexa, define " + random_line

def ask_about_weather():
  return "Alexa, what is the weather like today?"

def ask_about_time():
  return "Alexa, what time is it?"