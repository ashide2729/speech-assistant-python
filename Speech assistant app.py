'''
pip install speechrecognition
pip install pyttsx3
pip install pyaudio
pip install playsound
pip install PyObjC
'''

import speech_recognition as sr
import webbrowser
import time
import pyttsx3
from time import ctime

r = sr.Recognizer()

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 173)


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            sirina(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            sirina('Sorry, I did not get that')
        except sr.RequestError:
            sirina('Sorry, my speech service is down')
        return voice_data


def sirina(audio_string):
    print('Computer: ' + audio_string)
    speaker.say(audio_string)
    speaker.runAndWait()


def respond(voice_data):
    if 'what can you do or help with' in voice_data:
        sirina('I can search web, show locations, tell time and much more.')
    if 'what is your name' in voice_data:
        sirina('My name is Alexis')
    if 'what time is it' in voice_data:
        sirina(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        sirina('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        sirina('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
sirina('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)