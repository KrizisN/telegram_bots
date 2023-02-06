from telegram.ext import ApplicationBuilder

from telegram_bots.chat_gpt.register_handlers import RegisterChatGPTHandlers


class TelegramChatGPTBot:
    def __init__(self, config):
        self.application = ApplicationBuilder().token(config.TELEGRAM_GPT_TOKEN).build()

    def init(self):
        RegisterChatGPTHandlers().register_handlers(self.application)
        self.application.run_polling()
