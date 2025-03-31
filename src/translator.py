import os
from dotenv import load_dotenv
import deepl

load_dotenv()
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

auth_key=DEEPL_API_KEY
translator=deepl.Translator(auth_key)

with open("../data/transcripts/transcript.txt", "r") as file:
    transcript = file.read()

result=translator.translate_text(transcript, target_lang="ES")

with open("../data/translations/translated_transcript.txt", "x") as file:
    file.write(result.text)