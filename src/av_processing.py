from moviepy import VideoFileClip, AudioFileClip
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


def replace_audio(video_path, audio_path, output_path):
    try:
        command = ["ffmpeg", "-i", video_path, "-i", audio_path, "-c:v", "copy", "-map", "0:v:0", "-map", "1:a:0", "-shortest", output_path]

        subprocess.run(command, check=True)

        print(f"Audio replaced in {output_path}")
        return True
    except Exception as e:
        print(f"Error replacing audio: {e}")
        return False



