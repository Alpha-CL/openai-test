import os
import openai

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, '../../'))
load_dotenv(os.path.join(PARENT_DIR, '.env'))

openai.api_key = os.getenv("OPENAI_API_KEY")


def prompt():
    pass


def flow():
    pass


if __name__ == "__main__":
    prompt = "Hello, how are you?"
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
        stream=True
    )
    # print(completions)
    # message = completions.choices[0].text.strip()
    # print(message)

    for i, result in enumerate(completions):
        message = result.choices[0].text.strip()
        print(f"Generated message {i + 1}: {message}")
