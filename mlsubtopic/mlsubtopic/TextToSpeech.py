from gtts import gTTS
import os
from django.conf import settings
from audio.models import DemoMCall


def texttospeech(text,path):
    # Text to convert to speech
    # text = "Hello, Vishwas! This is a text-to-speech conversion using Google."

    # Language (en for English)
    tts = gTTS(text=text, lang='en')

    # Save the speech as an mp3 file
    file_path = os.path.join(settings.MEDIA_ROOT, 'audio', path)
    # Save the file manually
    # with open(file_path, 'wb+') as destination:
    #     for chunk in image_file.chunks():
    #         destination.write(chunk)

    audio_instance = DemoMCall(audio='audio/' + path)
    # audio_instance.save()

    tts.save(file_path)

    return audio_instance

    # Play the speech file (you can use os.startfile on Windows)
    # os.system("start output.mp3")  # For Windows, adjust for other OSes
