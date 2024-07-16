from local_utils.FileLogger import FileLogger
from local_utils.ConsoleLogger import ConsoleLogger

class LoggerGenerator:

    def get_logger(self, logger_type, logger_name):
        if logger_type == "file":
            return FileLogger(logger_name)
        elif logger_type == "console":
            return ConsoleLogger(logger_name)
