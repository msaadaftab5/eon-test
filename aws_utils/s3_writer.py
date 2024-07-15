from aws_utils import boto3_manager
from local_utils import LoggerGenerator

logger = LoggerGenerator.LoggerGenerator().get_file_logger("file", "s3_writer")
def upload_file(file_path, bucket_name, key):
    s3_client = boto3_manager.get_s3_client()
    logger.log_debug(f"Upload file from {file_path} to s3://{bucket_name}/{key}")
    s3_client.upload_file(file_path, bucket_name, key)