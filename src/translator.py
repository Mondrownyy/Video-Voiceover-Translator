import os
from dotenv import load_dotenv
import deepl

load_dotenv()
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

auth_key=DEEPL_API_KEY
translator=deepl.Translator(auth_key)

result=translator.translate_text("Hello, how are you?", target_lang="ES")
print(result.text)