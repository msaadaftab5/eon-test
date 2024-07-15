import os
from local_utils.LoggerGenerator import LoggerGenerator

def get_list_of_files_in_a_directory(directory):
    logger = LoggerGenerator().get_file_logger("file",logger_name="local_utils")
    logger.log_debug(f"Listing files in the directory {directory}")
    root, dirs, files = next(os.walk(directory, topdown=True))
    return [os.path.join(root, f) for f in files]
