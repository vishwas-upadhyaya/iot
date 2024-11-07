# import whisper
#
# def transcribe_audio(audio_file):
#     # Load the Whisper model. You can use different model sizes: 'tiny', 'base', 'small', 'medium', 'large'
#     model = whisper.load_model("base")  # Base model balances speed and accuracy.
#
#     # Transcribe the audio
#     print("Transcribing audio...")
#     result = model.transcribe("F:\Web Developement\PycharmProjects\mlsubtopic\mlsubtopic\mlsubtopic\sample_audio.wav")
#
#     # Output the transcribed text
#     return result['text']
#     # print(f"Transcribed text: {result['text']}")
#
#
# if __name__ == "__main__":
#     # Provide the path to your audio file
#     audio_file = "./sample_audio.wav"
#     transcribe_audio(audio_file)
