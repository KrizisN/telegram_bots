from abc import ABC, abstractmethod
from typing import Callable

from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import BaseFilter


class HandlerCreator(ABC):
    @abstractmethod
    def create_handler(self):
        pass


class CommandHandlerCreator(HandlerCreator):
    def __init__(self, command: str, callback: Callable):
        self.command = command
        self.callback = callback

    def create_handler(self):
        return CommandHandler(self.command, self.callback)


class MessageHandlerCreator(HandlerCreator):
    def __init__(self, filters: BaseFilter, callback: Callable):
        self.filters = filters
        self.callback = callback

    def create_handler(self):
        return MessageHandler(self.filters, self.callback)
