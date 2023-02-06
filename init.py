from telegram_bots.chat_gpt.chat_gpt import TelegramChatGPTBot


def init_all_telegram_bots(config):
    TelegramChatGPTBot(config).init()
