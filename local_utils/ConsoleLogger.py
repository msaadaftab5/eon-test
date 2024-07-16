import logging

class ConsoleLogger:
    def __init__(self, loggerName):
        self.__name = loggerName
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(logging.DEBUG)
        self.__formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.__console_handler = logging.StreamHandler()
        self.__console_handler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__console_handler)

    @property
    def formatter(self):
        return self.__formatter

    def log_debug(self, message):
        self.__logger.debug(message)

    def log_warn(self, message):
        self.__logger.warning(message)

    def log_error(self, message):
        self.__logger.error(message)
