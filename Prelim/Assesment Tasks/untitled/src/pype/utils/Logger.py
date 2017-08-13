from src.pype.utils.TextFormat import TextFormat


class Logger(object):
    """Logger"""
    def __init__(self):
        super(Logger, self).__init__()

    @staticmethod
    def log(message, prefix, color):
        print(TextFormat.to_ansi("[" + color + prefix + TextFormat.reset() + "] " + color + message + TextFormat.reset()))

    @staticmethod
    def info(message):
        Logger.log(message, "INFO", TextFormat.white())

    @staticmethod
    def warning(message):
        Logger.log(message, "WARNING", TextFormat.yellow())

    @staticmethod
    def error(message):
        Logger.log(message, "ERROR", TextFormat.red())

    @staticmethod
    def debug(message):
        Logger.log(message, "DEBUG", TextFormat.gray())

    @staticmethod
    def critical(message):
        Logger.log(message, "CRITICAL", TextFormat.red())

    @staticmethod
    def notice(message):
        Logger.log(message, "NOTICE", TextFormat.aqua())

Logger = Logger()
