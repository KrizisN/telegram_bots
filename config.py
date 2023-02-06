import os


class Config:
    def __init__(self):
        self.TELEGRAM_GPT_TOKEN = os.getenv("TELEGRAM_GPT_TOKEN")
        self.CHAT_GPT_TOKEN = os.getenv("CHAT_GPT_TOKEN")
