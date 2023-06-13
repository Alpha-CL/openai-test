import json
import os
import openai

from usages.utils import load_env

load_env()

openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    response = openai.api_resources.Engine.list()
    # print(f'================> response: {response}')
    if response.data:

        model_list = response.data
        print(f'================> model_list: {model_list}')
        model_id_list = []

        for model in model_list:
            model_id_list.append(model.id)

    # print(f'================> model_id_list: {model_id_list}')
    with open('engine_list.json', 'w') as f:
        json.dump(response.data, f)
