import logging
from dotenv import load_dotenv

from config import Config
from init import init_all_telegram_bots
from openai_manager import init_openai

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    load_dotenv()
    config = Config()
    init_openai(config)
    init_all_telegram_bots(config)
