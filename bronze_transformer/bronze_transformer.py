import json
import uuid
from aws_utils import s3_reader, s3_writer
from urllib.parse import unquote_plus
from aws_utils.SQS import SQS

def get_file_s3_uri(message):
    message = json.loads(message["Body"])
    s3_bucket = message["Records"][0]["s3"]["bucket"]["name"]
    prefix = unquote_plus(message["Records"][0]["s3"]["object"]["key"])
    return "/".join(["s3:/",s3_bucket,prefix])

def push_to_dlq(msg):
    #as we do not have a dead letter queue right now so leaving an empty body
    pass

def transform(df):
    df['dataAsset'] = df['dataAsset'].str.upper()
    return df

def save_to_silver_bucket(df, path_to_save):
    s3_writer.write_pandas_dataframe_as_parquet(df, path_to_save)

def transform_and_save(s3_uri, silver_bucket):
    df = s3_reader.read_json_array_file_as_pandas_df(s3_uri)
    df = transform(df)

    to_save_path_details = s3_uri.split("/")
    uuid_to_save = uuid.uuid4()
    source = to_save_path_details[2]
    asset_name = to_save_path_details[3]
    year = to_save_path_details[4]
    month = to_save_path_details[5]
    day = to_save_path_details[6]
    file_name = f"{uuid_to_save}.{to_save_path_details[7].replace('_15m.json','')}.snappy.parquet"
    path_to_save = f"s3://{silver_bucket}/source={source}/{asset_name}/{year}/{month}/{day}/{file_name}"
    save_to_silver_bucket(df, path_to_save)
def process_queue(queue_name, silver_bucket):
    sqs = SQS(queue_name)
    while sqs.check_queue_for_new_messages():
        to_delete = []
        for message in sqs.get_new_messages():
            try:
                s3_uri = get_file_s3_uri(message)
                transform_and_save(s3_uri, silver_bucket)
                to_delete.append({
                    'Id': message['MessageId'],
                    'ReceiptHandle': message['ReceiptHandle']
                })
            except KeyError:
                push_to_dlq(message)
                sqs.remove_message(message['ReceiptHandle'])
        if to_delete: sqs.remove_messages_batch(to_delete)

# if __name__ == "__main__":
#     # To be extracted from ENV Variables
#     QUEUE_NAME = "EonMessageQueue"
#     SILVER_BUCKET = "eon-silver-bucket"
#     sqs = SQS(QUEUE_NAME)
#     # sqs.delete_all_messages()
#     process_queue(QUEUE_NAME, SILVER_BUCKET)
#

def lambda_handler(event, context):
    QUEUE_NAME = "EonMessageQueue"
    SILVER_BUCKET = "eon-silver-bucket"
    sqs = SQS(QUEUE_NAME)
    # sqs.delete_all_messages()
    process_queue(QUEUE_NAME, SILVER_BUCKET)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
