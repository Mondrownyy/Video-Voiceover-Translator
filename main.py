import os
import dotenv
from src.video_processing import extract_audio
from src.speech_to_txt import transcribe_audio

def main():
    print("Running main function!")

audio_dir = "data/audio"
video_file = "data/input/Sample_MP4_1.mp4"
audio_output = os.path.join(audio_dir, "output_audio.wav")

success = extract_audio(video_file, audio_output)

if success:
    print("Audio extraction successful! Check:", audio_output)
else:
    print("Audio extraction failed.")

if __name__ == "__main__":
    main()
