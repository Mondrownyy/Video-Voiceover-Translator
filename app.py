import os
import uuid
import json
from flask import Flask, request, jsonify, render_template, send_file
from werkzeug.utils import secure_filename

from src.av_processing import extract_audio, replace_audio, get_video_duration, get_audio_duration, adjust_audio_speed
from src.speech_to_txt import transcribe_audio
from src.translator import translation, AVAILABLE_LANGUAGES
from src.txt_to_speech import text_to_speech

app = Flask(__name__)

UPLOAD_FOLDER = 'data/input'
OUTPUT_FOLDER = 'data/output'
AUDIO_FOLDER = 'data/audio'
TRANSCRIPTS_FOLDER = 'data/transcripts'
TRANSLATIONS_FOLDER = 'data/translations'
GENERATED_AUDIO_FOLDER = 'data/generated_audio'
ADJUSTED_AUDIO_FOLDER = 'data/adjusted_audio'

for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER, AUDIO_FOLDER, TRANSCRIPTS_FOLDER, 
               TRANSLATIONS_FOLDER, GENERATED_AUDIO_FOLDER, ADJUSTED_AUDIO_FOLDER]:
    os.makedirs(folder, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024

@app.route('/')
def index():
    return render_template('index.html', languages=AVAILABLE_LANGUAGES)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['video']
    target_lang = request.form.get('language', 'Spanish (Spain)')
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    file_id = str(uuid.uuid4())
    original_extension = os.path.splitext(file.filename)[1]
    filename = file_id + original_extension
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    session_data = {
        'file_id': file_id,
        'original_name': secure_filename(file.filename),
        'video_path': file_path,
        'target_lang': target_lang
    }
    
    return jsonify({
        'message': 'File uploaded successfully',
        'session_id': file_id,
        'next_step': '/process/' + file_id
    })

@app.route('/process/<session_id>', methods=['POST'])
def process_video(session_id):
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], request.json.get('filename'))
    target_lang = request.json.get('target_lang', 'Spanish (Spain)')
    
    audio_output = os.path.join(AUDIO_FOLDER, f"{session_id}.wav")
    output_json_path = os.path.join(TRANSCRIPTS_FOLDER, f"{session_id}.json")
    transcript_path = os.path.join(TRANSCRIPTS_FOLDER, f"{session_id}.txt")
    translation_path = os.path.join(TRANSLATIONS_FOLDER, f"{session_id}.txt")
    
    success = extract_audio(video_path, audio_output)
    if not success:
        return jsonify({'error': 'Audio extraction failed'}), 500
    
    transcription_result = transcribe_audio(audio_output, output_json_path)
    if not transcription_result:
        return jsonify({'error': 'Transcription failed'}), 500
    
    try:
        with open(output_json_path, 'r', encoding='utf-8') as json_file:
            transcript_data = json.load(json_file)
            transcript = transcript_data.get('results', {}).get('channels', [{}])[0].get('alternatives', [{}])[0].get('transcript', '')
        
        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.write(transcript)
    except Exception as e:
        return jsonify({'error': f'Failed to extract transcript: {str(e)}'}), 500
    
    try:
        translation_result = translation(transcript_path, translation_path, target_lang)
    except Exception as e:
        return jsonify({'error': f'Translation failed: {str(e)}'}), 500
    
    try:
        with open(translation_path, "r", encoding='utf-8') as file:
            to_generate = file.read()
        
        text_to_speech(to_generate)
        
        generated_files = [f for f in os.listdir(GENERATED_AUDIO_FOLDER) if f.endswith('.mp3')]
        if not generated_files:
            return jsonify({'error': 'Text-to-speech failed to produce audio'}), 500
        
        latest_audio = max(generated_files, key=lambda f: os.path.getmtime(os.path.join(GENERATED_AUDIO_FOLDER, f)))
        audio_path = os.path.join(GENERATED_AUDIO_FOLDER, latest_audio)
        
        output_video_path = os.path.join(OUTPUT_FOLDER, f"{session_id}_output.mp4")
        adjusted_audio_path = os.path.join(ADJUSTED_AUDIO_FOLDER, f"{session_id}_adjusted.mp3")
        
        speed_factor = get_audio_duration(audio_path) / get_video_duration(video_path)
        adjust_audio_speed(audio_path, adjusted_audio_path, speed_factor)
        
        replace_audio(video_path, adjusted_audio_path, output_video_path)
        
        return jsonify({
            'message': 'Processing completed successfully',
            'output_video': f"/download/{session_id}_output.mp4",
            'original_name': request.json.get('original_name', 'translated_video.mp4')
        })
    
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(OUTPUT_FOLDER, filename),
                     as_attachment=True,
                     download_name=filename)

@app.route('/status/<session_id>', methods=['GET'])
def get_status(session_id):
    output_path = os.path.join(OUTPUT_FOLDER, f"{session_id}_output.mp4")
    if os.path.exists(output_path):
        return jsonify({'status': 'completed', 'output': f"/download/{session_id}_output.mp4"})
    
    steps_completed = 0
    total_steps = 6
    
    if os.path.exists(os.path.join(AUDIO_FOLDER, f"{session_id}.wav")):
        steps_completed += 1
    if os.path.exists(os.path.join(TRANSCRIPTS_FOLDER, f"{session_id}.json")):
        steps_completed += 1
    if os.path.exists(os.path.join(TRANSLATIONS_FOLDER, f"{session_id}.txt")):
        steps_completed += 1
    
    generated_files = [f for f in os.listdir(GENERATED_AUDIO_FOLDER) if f.endswith('.mp3')]
    if generated_files:
        steps_completed += 1
    
    if os.path.exists(os.path.join(ADJUSTED_AUDIO_FOLDER, f"{session_id}_adjusted.mp3")):
        steps_completed += 1
    
    progress = int((steps_completed / total_steps) * 100)
    return jsonify({'status': 'processing', 'progress': progress})

if __name__ == '__main__':
    app.run(debug=True)