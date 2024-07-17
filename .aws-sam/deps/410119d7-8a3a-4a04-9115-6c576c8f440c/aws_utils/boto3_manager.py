import boto3

LOCAL_ENDPOINT_URL = "http://localhost.localstack.cloud:4566"
def get_s3_client():
    return boto3.client('s3', endpoint_url = LOCAL_ENDPOINT_URL)

def get_sqs_client():
    return boto3.client('sqs', endpoint_url = LOCAL_ENDPOINT_URL)