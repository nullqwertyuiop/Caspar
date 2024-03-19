import logging

from dotenv import load_dotenv


def init_env():
    load_dotenv(override=True)
    logging.basicConfig(level=logging.DEBUG)
