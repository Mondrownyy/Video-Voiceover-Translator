import os
from dotenv import load_dotenv
import deepl

load_dotenv()
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

auth_key=DEEPL_API_KEY
translator=deepl.Translator(auth_key)

def translation(transcript_path, translation_path, target_lang):
    with open(transcript_path, "r") as file:
        transcript = file.read()

    result=translator.translate_text(transcript, target_lang=target_lang)

    with open(translation_path, "x") as file:
        file.write(result.text)

    return result