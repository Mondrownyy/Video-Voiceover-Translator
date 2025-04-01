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


def get_video_duration(video_path):
    try:
        video = VideoFileClip(video_path)
        video_duration = video.duration
        video.close()
        print(video_duration)
        return video_duration
    except Exception as e:
        print(f"Error getting video duration: {e}")
        return None

def get_audio_duration(audio_path):
    try:
        command = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_path]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        duration = float(result.stdout)
        print(duration)
        return duration
    except subprocess.CalledProcessError as e:
        print(f"Error getting audio duration: {e}")
        return None


def adjust_audio_speed(input_audio_path, output_adjusted_audio_path, speed_factor):
    try:
        command = [
            "ffmpeg", "-i", input_audio_path, "-filter:a", f"atempo={speed_factor}", "-vn", "-codec:a", "libmp3lame" ,output_adjusted_audio_path
        ]
        subprocess.run(command, check=True)
        print(f"Audio speed adjusted and saved to {output_adjusted_audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error adjusting audio speed: {e}")
