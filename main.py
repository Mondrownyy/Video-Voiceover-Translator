import os
import dotenv
from src.video_processing import extract_audio
from src.speech_to_txt import transcribe_audio


def main():
    print("Running main function!")

audio_dir = "data/audio"
video_file = "data/input/Sample_MP4_1.mp4"
transcripts_dir = "data/transcripts"
audio_output = os.path.join(audio_dir, "output_audio.wav")
output_json_path = os.path.join(transcripts_dir, "output_json.json")

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


if __name__ == "__main__":
    main()
