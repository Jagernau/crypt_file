import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_DIR: str = os.environ["DEFAULT_DIR"]
DEFAULT_NAME: str = os.environ["DEFAULT_NAME"]
ITERATION: int = int(os.environ["ITERATION"])
HASH_NAME: str = os.environ["HASH_NAME"]

