from gtts import gTTS
import os
import sys


def save_audio(text, language='en', slow=False, file_name='test.mp3'):
    try:
        # Create a gTTS object and convert text to speech
        tts = gTTS(text=text, lang=language, slow=slow)

        # Save the converted speech to a file
        tts.save(file_name)
        print(f"Audio saved as {file_name}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def play_audio(file_name):
    try:
        # Play the audio file
        os.system(f"start {file_name}" if sys.platform == "win32" else f"mpg321 {file_name}")
    except Exception as e:
        print(f"Error while playing audio: {e}")
        sys.exit(1)


def get_user_input():
    # Get text input from the user
    print("Enter the text you want to convert to speech:")
    user_input = input("Text: ")

    if not user_input:
        print("No text provided! Using default text.")
        user_input = "Hey guys, how is the weather today?"

    return user_input


def main():
    # Get user input text
    text = get_user_input()

    # Ask user if they want slow or fast speech
    slow = input("Do you want slow speech? (y/n): ").strip().lower()
    slow = True if slow == 'y' else False

    # Ask for the language code
    language = input("Enter language code (default 'en'): ").strip() or "en"

    # Ask for file name
    file_name = input("Enter the file name to save (default 'test.mp3'): ").strip() or "test.mp3"

    # Save the speech audio
    save_audio(text, language, slow, file_name)

    # Play the saved audio
    play_audio(file_name)


if __name__ == "__main__":
    main()
