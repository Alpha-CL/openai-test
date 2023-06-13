import os
import openai

from usages.handler import openai_request
from usages.utils import load_env, traditional_to_simplified

load_env()
CURRENT_DIR = os.getcwd()

openai.organization = os.getenv('ORGANIZATION')
openai.api_key = os.getenv('OPENAI_API_KEY')

audio = open(f'{CURRENT_DIR}/audio.mp3', 'rb')


def validate_file(file):
    file_name = os.path.basename(file.name)
    file_ext = os.path.splitext(file_name)[1]
    ext_list = ['.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav', '.webm']
    print(f'================> filename: {file_name}')
    print(f'================> file_ext: {file_ext}')


# language 参数对应的 code
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

def audio_to_text(audio_file):
    validate_file(audio_file)
    transcript = openai.Audio.transcribe(
        model='whisper-1',
        file=audio_file,
        # temperature=0,  # [0,1]
        # response_format='json',  # json, text, srt
        # language='zh',  # zh, en, ...
    )
    if hasattr(transcript, 'text'):
        return traditional_to_simplified(transcript.text)


if __name__ == '__main__':
    response = openai_request(audio_to_text, audio)
    print(f'================> response: {response}')
