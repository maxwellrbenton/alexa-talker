import time
import sys
import importlib
import app.alexa_controls
from app.controller import Controller
import app.commands
import app.speech_to_text

# Alexa commands:
# 'animal'
# 'location'
# 'animal and location'
# 'define'
# 'time'
# 'weather'

def set_volume(volume):
  return "Alexa, set volume to " + str(volume)

def run():
  if len(sys.argv) == 3 and (str(sys.argv[2]) == '--silent' or str(sys.argv[2]) == '-s'):
    talker = Controller(app.commands, app.speech_to_text, str(sys.argv[1]))
    app.speech_to_text.speak(set_volume(0))
    time.sleep(5)
    talker.start()
    time.sleep(60)
    app.speech_to_text.speak(set_volume(4))
  else:
    if len(sys.argv) < 2:
      talker = Controller(app.commands, app.speech_to_text, 'weather')
      talker.start()
    else:
      talker = Controller(app.commands, app.speech_to_text, str(sys.argv[1]))
      talker.start()

run()