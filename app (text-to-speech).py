from gtts import gTTS
import os
from pathlib import Path


BASE_DOWNLOAD_PATH = Path(__file__).resolve().parent.parent
DOWNLOAD_PATH = os.path.join(BASE_DOWNLOAD_PATH, 'audio.mp3')

text = input("Enter any thing to convert to speech: ")
language = 'en'
converted_audio = gTTS(text=text, lang=language, slow=False)
converted_audio.save(DOWNLOAD_PATH)
os.system(DOWNLOAD_PATH)

print("Conversion Successful")
print(f"File Path: {DOWNLOAD_PATH}")
