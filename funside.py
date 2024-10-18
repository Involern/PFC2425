import requests as r
from pydub import AudioSegment

url = input("Enter url to download as .WAV")
response = r.get(url)