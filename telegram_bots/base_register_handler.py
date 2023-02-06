class BaseRegisterHandler:
    handlers = []

    def register_handlers(self, application):
        for handler in self.handlers:
            application.add_handler(handler.create_handler())
