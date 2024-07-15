from local_utils.FileLogger import FileLogger

class LoggerGenerator:

    def get_file_logger(self, logger_type, logger_name):
        if logger_type == "file":
            return FileLogger(logger_name)