import cowsay
import pyttsx3

engine = pyttsx3.init()
msg = input('Write something? ')
cowsay.cow(msg)
engine.say(msg)
engine.runAndWait()
