from aws_utils import boto3_manager
from aws_utils.boto3_manager import LOCAL_ENDPOINT_URL
# from local_utils import LoggerGenerator
import awswrangler as wr

wr.config.s3_endpoint_url = LOCAL_ENDPOINT_URL
def upload_file(file_path, bucket_name, key):
    s3_client = boto3_manager.get_s3_client()
    s3_client.upload_file(file_path, bucket_name, key)

def write_pandas_dataframe_as_parquet(df, path):
    wr.s3.to_parquet(df=df, path=path)