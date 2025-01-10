# Text-to-Speech Converter with gTTS

This Python script allows you to convert any text into speech using the Google Text-to-Speech (gTTS) API. You can specify various options such as language, speech speed, and file name for the saved audio. The program also plays the generated audio automatically after saving it.

## Features
- **Text-to-Speech Conversion**: Converts the provided text into speech.
- **Language Support**: Supports multiple languages, configurable by the user.
- **Speech Speed**: Choose between slow or normal speech speed.
- **Customizable Output**: Users can specify the file name for the saved audio.
- **Cross-Platform Audio Playback**: Automatically detects the OS and plays the audio file using the appropriate command.
- **Error Handling**: Graceful error handling for common issues like missing input or playback failures.

## Requirements
- Python 3.x
- `gTTS` library

You can install the required libraries using pip: pip install gtts

## Follow the prompts to:
- Enter the text you want to convert to speech.
- Choose the speech speed (normal or slow).
- Select the language (default is English).
- Provide a file name to save the audio.
- The script will save the audio file and play it automatically.

## Acknowledgments
This project was inspired by the YouTube channel Techie Coder for the base code, with some additional modifications and enhancements made with some help from documentation and ChatGPT to provide a more interactive user experience.
