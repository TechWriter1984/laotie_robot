from datetime import datetime
import pyttsx3, io, sys

now = datetime.now()

time = now.strftime("现在是%H点%M分")
# print(type(time))

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('voice', 'zh')

engine.say(time)
engine.runAndWait()

# engine.save_to_file(time, 'text2speech.wav')
# engine.runAndWait()