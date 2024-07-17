from datetime import datetime
from local_utils import local_files_utils as lfu
from aws_utils.s3_writer import upload_file
import json


DATE_TODAY = datetime.today()

def format_S3_key(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_contents_as_dict = json.load(file)

    product_name = file_contents_as_dict[0]['dataAsset'].strip()
    ingestion_timestamp = datetime.strptime(file_contents_as_dict[0]['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
    return (f"asset-name={product_name}/"
            f"yyyy={ingestion_timestamp.year}/"
            f"mm={ingestion_timestamp.month}/"
            f"dd={ingestion_timestamp.day}/"
            f"{ingestion_timestamp.date()}_15m.json")

def run():
    inputs = lfu.get_list_of_files_in_a_directory("sample_inputs")
    for input in inputs:
        upload_file(input, "eon-bronze-bucket", format_S3_key(input))
