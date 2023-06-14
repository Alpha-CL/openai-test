import os
from dotenv import load_dotenv
import opencc


def load_env():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.abspath(os.path.join(base_dir, '..'))
    load_dotenv(os.path.join(parent_dir, '.env'))


def traditional_to_simplified(traditional_chinese):
    converter = opencc.OpenCC("t2s.json")
    return converter.convert(traditional_chinese)
