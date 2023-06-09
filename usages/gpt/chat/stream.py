import os
import openai

from usages.handler import openai_request
from usages.utils import load_env

load_env()

openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatSize:
    small = 1024
    middle = 2048
    large = 4096


# https://platform.openai.com/docs/api-reference/chat/create
def chat(prompt='', n=1):
    if type(prompt).__name__ != "string" and len(prompt) > 0:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            n=n,
            # max_tokens=1024 * 4 - len(prompt) * 2,
            stream=True
        )
        # print(f'================> response: {response}')
        # return response.choices[0].text.strip() if response else None

        content = ''
        for i, result in enumerate(response):
            fragment = result.choices[0].text.strip()
            content += fragment
            print(f"Generated message {i + 1}: {fragment}")
        return content


if __name__ == "__main__":
    message = openai_request(chat, timeout=60, prompt='书写一个100字的灵异小说')
    print(f'================> message: {message}')
    print(f'================> message.length: {len(message)}')
