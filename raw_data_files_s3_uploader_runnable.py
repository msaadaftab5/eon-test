from datetime import datetime
from local_utils import local_files_utils as lfu
from local_utils.LoggerGenerator import LoggerGenerator
from aws_utils.s3_writer import upload_file
from aws_utils.SQS import SQS

DATE_TODAY = datetime.today().strftime('%Y-%m-%d')
BRONZE_FILES_PREFIX = 'bronze'

def format_S3_key(file_name):
    return f"{BRONZE_FILES_PREFIX}/{DATE_TODAY}/{file_name.split('/')[-1]}"

def run():
    inputs = lfu.get_list_of_files_in_a_directory("sample_inputs")
    for input in inputs:
        upload_file(input, "eon-bronze-bucket", format_S3_key(input))
