import awswrangler as wr
from aws_utils.boto3_manager import LOCAL_ENDPOINT_URL
# from local_utils.LoggerGenerator import LoggerGenerator

# logger = LoggerGenerator().get_logger("console", "s3_reader")

def read_json_array_file_as_pandas_df(s3_uri):
    #This should be ideally done base on the basis of a environment variable
    # logger.log_debug(f"Reading Dataframe from: {s3_uri}")
    wr.config.s3_endpoint_url = LOCAL_ENDPOINT_URL
    return wr.s3.read_json(s3_uri, orient='records')