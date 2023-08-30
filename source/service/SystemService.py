import os
from dotenv import main
main.load_dotenv()


def getEnv(key: str):
    return os.getenv(key)
