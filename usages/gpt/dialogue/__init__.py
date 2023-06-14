import os
import openai

from usages.handler import openai_request
from usages.utils import load_env

load_env()

openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")


def dialogue(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    msgs = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    content = openai_request(dialogue, messages=msgs)
    print(f'================> content: {content}')
