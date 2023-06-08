import os
import openai

from usages.utils import load_env

load_env()
CURRENT_DIR = os.getcwd()

# openai.organization = os.getenv("ORGANIZATION")
print(f'================> openai.organization : {openai.organization}')
openai.api_key = os.getenv("OPENAI_API_KEY")
print(f'================> openai.api_key : {openai.api_key}')

if __name__ == '__main__':
    audio_file = open(f"{CURRENT_DIR}/audio.mp3", "rb")
    print(f'================> audio_file: {audio_file}')
    transcript = openai.Audio.translate("whisper-1", audio_file)
    print(f'================> transcript: {transcript}')
