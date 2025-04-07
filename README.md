# Video-Voiceover-Translator

A powerful application that automatically translates video content into different languages by extracting audio, transcribing speech, translating text, generating voiceovers, and creating a new video with the translated audio.
![Movie-transl](https://github.com/user-attachments/assets/b7ae2f3d-21c7-45fb-b141-636624c095e6)

## Features ✨

- **Video Upload**: Support for MP4 video formats
- **Audio Extraction**: Automatically extracts audio from uploaded videos
- **Transcription**: Uses Deepgram's AI to convert speech to text
- **Translation**: Supports 35+ languages through DeepL translation API
- **Voice Generation**: Creates natural-sounding voiceovers with ElevenLabs
- **Video Reconstruction**: Combines translated audio with original video
- **Web Interface**: User-friendly interface for easy interaction

## Technologies Used 🛠

- **Backend**: Python, Flask
- **Speech-to-Text**: Deepgram API
- **Translation**: DeepL API
- **Text-to-Speech**: ElevenLabs API
- **Audio/Video Processing**: FFmpeg, MoviePy, PyDub
- **Environment Management**: python-dotenv
- **Frontend**: HTML, CSS (Bootstrap)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- FFmpeg installed on your system
- API keys for Deepgram, DeepL, and ElevenLabs

### Getting Started 🚀

1. Clone the repository
   ```
   git clone https://github.com/Mondrownyy/Video-Voiceover-Translator.git
   cd Video-Voiceover-Translator
   ```

2. Install required packages
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API keys
   ```
   DEEPGRAM_API_KEY=your_deepgram_api_key
   DEEPL_API_KEY=your_deepl_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- [Deepgram](https://deepgram.com/) for speech-to-text API
- [DeepL](https://www.deepl.com/) for translation API
- [ElevenLabs](https://elevenlabs.io/) for text-to-speech API
