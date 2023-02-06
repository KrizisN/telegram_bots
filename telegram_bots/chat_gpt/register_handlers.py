from telegram.ext import filters

from telegram_bots.base_register_handler import BaseRegisterHandler
from telegram_bots.chat_gpt.callbacks import start_bot, echo_message
from telegram_bots.handlers import CommandHandlerCreator, MessageHandlerCreator


class RegisterChatGPTHandlers(BaseRegisterHandler):
    handlers = [
        CommandHandlerCreator("start", start_bot),
        MessageHandlerCreator(filters.TEXT & (~filters.COMMAND), echo_message)
    ]
