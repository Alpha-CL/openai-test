import os
import openai

from usages.handler import openai_request
from usages.utils import load_env

load_env()
CURRENT_DIR = os.getcwd()

openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")


class ImageSize:
    small = '256x256'
    middle = '512x512'
    large = '1024x1024'


def image_creator(
        prompt="柯基狗",
        n=1,
        size=ImageSize.small,
        response_format='url'
):
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size=size,
        response_format=response_format
    )
    return [item.url for item in response.data if response.data] if response else None


if __name__ == '__main__':
    content = openai_request(image_creator, prompt="柯基狗")
    print(f'================> content: {content}')
