import easyocr
from mlsubtopic.res_gen import get_text
from mlsubtopic.TextToSpeech import texttospeech

# Initialize the EasyOCR reader
# Pass the list of languages you want to recognize (e.g., ['en'] for English)
reader = easyocr.Reader(['en'])

# Perform OCR on an image file

def convert(path):
    print(path)
    result = reader.readtext(path)

    # Print the results (list of detected text)
    res = ""
    for detection in result:
        res = res + detection[1]
        # print(detection[1])  # detection[1] contains the recognized text

    # res = get_text(res)
    path1 = path.split("\\")
    path1 = path1[len(path1)-1].split(".")[0]+".mp3"

    return texttospeech(res,path1)


