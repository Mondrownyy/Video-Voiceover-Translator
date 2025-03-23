import os
from moviepy import VideoFileClip


def extract_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio:
            audio = audio.set_channels(1)
            audio.write_audiofile(audio_path, codec="pcm_s16le", fps=16000, verbose=False, logger=None)
            video.close()
            return True
        else:
            print("Error: No audio track found in the video.")
            return False
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return False
