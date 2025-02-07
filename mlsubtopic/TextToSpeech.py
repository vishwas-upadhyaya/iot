from gtts import gTTS
import os
from django.conf import settings
from audio.models import DemoMCall
from mlsubtopic.res_gen import get_text

import boto3
from gtts import gTTS
from django.conf import settings
from io import BytesIO

import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# SECRET_KEY = env("SECRET_KEY")
# aws_access_key_id = env("AWS_ACCESS_KEY_ID")
# aws_secret_access_key = env("AWS_SECRET_ACCESS_KEY")

# aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
# aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
# region_name = os.environ.get("AWS_REGION_S3")
bucket_name = "imagetopic"
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=os.environ.get("AWS_REGION_S3"),
)

def upload_to_s3(file_obj, file_path):

    try:
        s3_client.upload_fileobj(file_obj, bucket_name, file_path)
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_path}"
        return s3_url
    except Exception as e:
        print(f"Error uploading to S3: {e}")
        return None






def texttospeech(text, path):
    # Text to convert to speech
    # text = "Hello, Vishwas! This is a text-to-speech conversion using Google."
    text = get_text(text)
    # Language (en for English)
    tts = gTTS(text=text, lang='en')

    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)  # Reset file pointer to the start

    # Define the S3 path for the file
    file_path = f"audio/{path}.mp3"

    # Upload to S3 and get the URL
    s3_url = upload_to_s3(audio_file, file_path)







    # # Save the speech as an mp3 file
    # file_path = os.path.join(settings.MEDIA_ROOT, 'audio', path)
    # # Save the file manually
    # # with open(file_path, 'wb+') as destination:
    # #     for chunk in image_file.chunks():
    # #         destination.write(chunk)
    #
    # audio_instance = DemoMCall(audio='audio/' + path)
    # # audio_instance.save()
    #
    # tts.save(path)

    # del tts

    print()

    return s3_url

    # Play the speech file (you can use os.startfile on Windows)
    # os.system("start output.mp3")  # For Windows, adjust for other OSes
