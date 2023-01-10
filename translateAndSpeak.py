import time
from gtts import gTTS
from pygame import mixer
from googletrans import Translator

mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') # Initialize it with the correct device
translator = Translator()

while True:
    sentence = input("Enter sentece: ")
    sentence = translator.translate(sentence, dest='en').text
    mixer.music.set_volume(0.70)
    tts = gTTS(sentence, lang='en', tld='com.au')
    tts.save('speak.mp3')
    mixer.music.load("speak.mp3") # Load the mp3
    try:
        mixer.music.play() # Play it
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(0.1)
        mixer.music.unload()
    except:
        pass