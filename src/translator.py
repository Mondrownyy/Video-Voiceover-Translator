import os
from dotenv import load_dotenv
import deepl

load_dotenv()
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

auth_key=DEEPL_API_KEY
translator=deepl.Translator(auth_key)

AVAILABLE_LANGUAGES = {
    "English (United States)": "EN-US",
    "English (United Kingdom)": "EN-GB",
    "English (Australia)": "EN-AU", 
    "English (Canada)": "EN-CA",
    "Japanese (Japan)": "JA",
    "Chinese (Simplified, China)": "ZH",
    "German (Germany)": "DE",
    "Hindi (India)": "HI",
    "French (France)": "FR",
    "French (Canada)": "FR-CA",
    "Korean (South Korea)": "KO",
    "Portuguese (Brazil)": "PT-BR",
    "Portuguese (Portugal)": "PT-PT",
    "Italian (Italy)": "IT",
    "Spanish (Spain)": "ES",
    "Spanish (Mexico)": "ES-MX",
    "Indonesian (Indonesia)": "ID",
    "Dutch (Netherlands)": "NL",
    "Turkish (Turkey)": "TR",
    "Filipino (Philippines)": "TL",
    "Polish (Poland)": "PL",
    "Swedish (Sweden)": "SV",
    "Bulgarian (Bulgaria)": "BG",
    "Romanian (Romania)": "RO",
    "Arabic (Saudi Arabia)": "AR",
    "Arabic (United Arab Emirates)": "AR",
    "Czech (Czech Republic)": "CS",
    "Greek (Greece)": "EL",
    "Finnish (Finland)": "FI",
    "Croatian (Croatia)": "HR",
    "Malay (Malaysia)": "MS",
    "Slovak (Slovakia)": "SK",
    "Danish (Denmark)": "DA",
    "Tamil (India)": "TA",
    "Ukrainian (Ukraine)": "UK",
    "Russian (Russia)": "RU"
}

def translation(transcript_path, translation_path, target_lang):
    with open(transcript_path, "r", encoding="utf-8") as file:
        transcript = file.read()
    
    if target_lang in AVAILABLE_LANGUAGES:
        api_lang_code = AVAILABLE_LANGUAGES[target_lang]
    else:
        api_lang_code = target_lang

    result = translator.translate_text(transcript, target_lang=api_lang_code)

    with open(translation_path, "x", encoding="utf-8") as file:
        file.write(result.text)

    return result