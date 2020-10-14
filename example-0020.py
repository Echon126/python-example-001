import pyttsx3
import time

str = "Come on, Catherine"
engine = pyttsx3.init()
num = 0
while num < 3:
    engine.say(str)
    engine.runAndWait()
    num += 1
    time.sleep(10)
