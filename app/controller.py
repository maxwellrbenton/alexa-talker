import random

class Controller:

  def __init__(self, commands, speech_to_text, type='time'):
    self.type = type
    self.speech_to_text = speech_to_text
    self.commands = commands
    self.options = {
            'animal': commands.ask_about_animal,
            'location': commands.ask_about_location,
            'animal and location': commands.ask_about_animal_and_location,
            'define': commands.ask_to_define,
            'time': commands.ask_about_time,
            'weather': commands.ask_about_weather
            }

  def start(self):
    command = self.options.get(self.type, self.commands.ask_about_time)()
    self.speech_to_text.speak(command)

