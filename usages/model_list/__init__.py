import os
import openai

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, '../..'))
load_dotenv(os.path.join(PARENT_DIR, '.env'))

# openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    response = openai.Model.list()
    if response.data:

        model_list = response.data
        model_id_list = []

        for model in model_list:
            # 是否允许创建模型引擎
            allow_create_engine = model.permission[0].allow_create_engine
            print(f'================> model: {model.pd}, {allow_create_engine}')
            model_id_list.append(model.id)
            if allow_create_engine:
                print(f'================> model: {model.permission[0]}')

        # print(f'================> model_id_list: {model_id_list}')
