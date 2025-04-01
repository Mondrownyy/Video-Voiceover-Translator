import os
import elevenlabs
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, VoiceSettings
import uuid


load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

input_translated_transcript_path = os.path.abspath("data/translations/translated_transcript.txt")

with open(input_translated_transcript_path, "r") as file:
    to_generate = file.read()

output_audio_dir = os.path.abspath("data/generated_audio/")
os.makedirs(output_audio_dir, exist_ok=True)

def text_to_speech(text):
    response = client.text_to_speech.convert(
        voice_id="CwhRBWXzGAHq8TQ4Fs17",
        text=text,
        model_id="eleven_multilingual_v2",
        output_format="mp3_22050_32",
    )

    save_file_path = os.path.join(output_audio_dir, f"{uuid.uuid4()}.mp3")
    print(save_file_path)

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {save_file_path}")