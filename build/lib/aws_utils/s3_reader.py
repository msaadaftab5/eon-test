import awswrangler as wr
from aws_utils.boto3_manager import LOCAL_ENDPOINT_URL

def read_json_array_file_as_pandas_df(s3_uri):
    wr.config.s3_endpoint_url = LOCAL_ENDPOINT_URL
    return wr.s3.read_json(s3_uri, orient='records')