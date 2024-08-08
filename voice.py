
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
def playsong(txt):
    # The text that you want to convert to audio
    mytext = txt

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome1.mp3")


    # Playing the converted file
    # os.system("mpg321 welcome.mp3")


    # from pygame import mixer  # Load the popular external library
    #
    # mixer.init()
    # mixer.music.load('welcome.mp3')
    # mixer.music.play()


    import playsound
    playsound.playsound('welcome1.mp3', True)
    os.remove("welcome1.mp3")