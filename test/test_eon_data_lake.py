#Ideally all the modules should have their own tests and folder with a
# parent command at main level to execute them sequentially
import re
#Since the project has not yet been built CI/CD compliant, we are adding some smaple
# test cases for the purpose of the completion of case study


import sys
import os
import pandas as pd
import json
from unittest import TestCase
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bronze_transformer')))
from bronze_transformer import transform, get_file_s3_uri, get_path_to_save_to_silver_bucket

def test_bronze_transformation():
    df = pd.DataFrame({'dataAsset': ["mercury", "mars", "jupiter"]}, index=[1,2,3])
    expected_df = pd.DataFrame({'dataAsset': ["MERCURY", "MARS", "JUPITER"]}, index=[1, 2, 3])
    result = transform(df)
    assert expected_df.equals(result)

def test_get_file_s3_uri():
    mock_message = {
        "Body": json.dumps({
            "Records": [
                {
                    "s3": {
                        "bucket": {
                            "name": "bronze-bucket"
                        },
                        "object": {
                            "key": "test/path/to/file.txt"
                        }
                    }
                }
            ]
        })
    }

    # Expected output
    expected_uri = "s3://bronze-bucket/test/path/to/file.txt"
    assert get_file_s3_uri(mock_message) == expected_uri


def test_get_path_to_save_to_silver_bucket():
    s3_uri = "s3://bronze-bucket/dataAsset=mercury/year=2023/month=07/date=17/file_15m.json"
    silver_bucket_name = "my-silver-bucket"
    result = get_path_to_save_to_silver_bucket(s3_uri, silver_bucket_name)

    prefix = "s3://my-silver-bucket/source=bronze-bucket/dataAsset=mercury/year=2023/month=07/date=17/file."
    suffix = ".snappy.parquet"

    assert result.startswith(prefix) and result.endswith(suffix)
