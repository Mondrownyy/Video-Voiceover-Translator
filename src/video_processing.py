from moviepy import VideoFileClip
import subprocess


def extract_audio(video_path, audio_path):
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path, "-ac", "1", "-ar", "16000", "-sample_fmt", "s16", audio_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return False