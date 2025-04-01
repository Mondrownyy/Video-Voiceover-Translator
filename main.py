import os
import dotenv
from src.av_processing import extract_audio, replace_audio, get_video_duration, get_audio_duration, adjust_audio_speed
from src.speech_to_txt import transcribe_audio
from src.txt_to_speech import text_to_speech


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
adjusted_audio_path = "data/adjusted_audio/adjusted_audio.mp3"

success = extract_audio(video_file, audio_output)

if success:
    print("Audio extraction successful! Check:", audio_output)
else:
    print("Audio extraction failed.")

working = transcribe_audio(audio_output, output_json_path)

if working:
    print("Transcription successful! Check:", output_json_path)
else:
    print("Transcription failed.")

with open("data/translations/translated_transcript.txt", "r") as file:
    to_generate = file.read()

text_to_speech(to_generate)

speeed_factor = get_video_duration(video_path) / get_audio_duration(audio_path)

adjust_audio_speed(audio_path, adjusted_audio_path,speeed_factor)

replace_audio(video_path, adjusted_audio_path, output_path)


if __name__ == "__main__":
    main()
