import os
from dotenv import load_dotenv


def load_env():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
    load_dotenv(os.path.join(PARENT_DIR, '.env'))
