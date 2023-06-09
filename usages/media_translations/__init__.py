import os
import openai

from usages.handler import openai_request
from usages.utils import load_env

load_env()
CURRENT_DIR = os.getcwd()

openai.organization = os.getenv('ORGANIZATION')
openai.api_key = os.getenv('OPENAI_API_KEY')

audio = open(f'{CURRENT_DIR}/audio.mp3', 'rb')


def audio_translate(file):
    response = openai.Audio.translate(
        model='whisper-1',
        file=file,
        # prompt='',  #
        # temperature=0,  # [0,1]
        # response_format='json',  # json, text, srt
        # language='en',  # zh, en, ...
    )
    return response['text'] if response else None


if __name__ == '__main__':
    content = openai_request(audio_translate, file=audio)
    print(f'================> content: {content}')
