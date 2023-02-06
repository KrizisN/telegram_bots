import openai


def init_openai(config):
    openai.api_key = config.CHAT_GPT_TOKEN
