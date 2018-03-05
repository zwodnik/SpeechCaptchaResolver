import speech_recognition as sr
from pydub import AudioSegment

from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "payload"),
AUDIO_FILE2 = path.join(path.dirname(path.realpath(__file__)), "payload.vaw"),
print("Load audio: {}".format(AUDIO_FILE[0]))
print("Load audio: {}".format(AUDIO_FILE2[0]))

sound = AudioSegment.from_file(AUDIO_FILE[0])
sound.export(AUDIO_FILE2[0], format="wav")


r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE2[0]) as source:
	audio = r.record(source)

try:
	print("Google SR: {}".format(r.recognize_google(audio)))
except sr.UnknownValueError:
    	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))
