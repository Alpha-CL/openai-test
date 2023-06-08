import os
import openai

from usages.utils import load_env

load_env()
CURRENT_DIR = os.getcwd()

openai.organization = os.getenv("ORGANIZATION")
print(f'================> openai.organization : {openai.organization}')
openai.api_key = os.getenv("OPENAI_API_KEY")
print(f'================> openai.api_key : {openai.api_key}')


class ImageSize:
    small = '256x256'
    middle = '512x512'
    large = '1024x1024'


if __name__ == '__main__':
    response = openai.Image.create(
        prompt="柯基狗",
        n=1,
        size=ImageSize.small
    )
    print(f'================> response: {response}')
