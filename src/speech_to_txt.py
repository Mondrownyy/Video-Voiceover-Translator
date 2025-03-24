import os
from moviepy import VideoFileClip
import subprocess
import requests
from dotenv import load_dotenv
import json

load_dotenv()
DEEP_API_KEY = os.getenv("DEEPGRAM_API_KEY")

def transcribe_audio(audio_path, output_json_path):
    url = "https://api.deepgram.com/v1/listen"
    headers = {"Authorization": f"Token {DEEP_API_KEY}", "Content-Type": "audio/wav"}

    with open(audio_path, "rb") as audio_file:
        response = requests.post(url, headers=headers, data=audio_file)

    response_json = response.json()

    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(response_json, json_file, indent=4)

    return response_json

