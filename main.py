import os
import dotenv
from src.video_processing import extract_audio
from src.speech_to_txt import transcribe_audio
from src.txt_to_speech import text_to_speech
from src.video_processing import replace_audio


def main():
    print("Running main function!")

audio_dir = "data/audio"
video_file = "data/input/Sample_MP4_1.mp4"
transcripts_dir = "data/transcripts"
audio_output = os.path.join(audio_dir, "output_audio.wav")
output_json_path = os.path.join(transcripts_dir, "output_json.json")
video_path = "data/input/Sample_MP4_1.mp4"
audio_path = "data/generated_audio/3041ddec-12de-4b7c-8654-b4dc1db1dbc5.mp3"
output_path = "data/output/output_video.mp4"
""""
success = extract_audio(video_file, audio_output)

if success:
    print("Audio extraction successful! Check:", audio_output)
else:
    print("Audio extraction failed.")
"""
"""
working = transcribe_audio(audio_output, output_json_path)

if working:
    print("Transcription successful! Check:", output_json_path)
else:
    print("Transcription failed.")
"""
""""
with open("data/translations/translated_transcript.txt", "r") as file:
    to_generate = file.read()

text_to_speech(to_generate)
"""

replace_audio(video_path, audio_path, output_path)

if __name__ == "__main__":
    main()
