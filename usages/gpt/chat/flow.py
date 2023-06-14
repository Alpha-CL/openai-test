import os
import openai

from usages.utils import load_env

load_env()

openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    prompt = "Hello, how are you?"
    completions = openai.Completion.create(
        # engine="davinci",
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
        stream=True
    )
    print(completions)
    # message = completions.choices[0].text.strip()
    # print(message)

    for i, result in enumerate(completions):
        message = result.choices[0].text.strip()
        print(f"Generated message {i + 1}: {message}")
