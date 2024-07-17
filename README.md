This project needs Python 3.9, SAMLOCAL and Localstack container preconfigured

This is the implementation of the case study.  



1- Spin up localstack container

```
docker run \
  --rm -it \
  -p 127.0.0.1:4566:4566 \
  -p 127.0.0.1:4510-4559:4510-4559 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  localstack/localstack
```

2- Build, package and deploy the SAM Project with the following commands

```
samlocal build
samlocal package --output-template-file packaged.yaml
samlocal deploy --template-file packaged.yaml --stack-name first-layer-stack
```

To Test the code locally:

1- Create a Virtual Env
```
python -m venv .venv
```

2- Activate the Virtual Env
```
source .venv/bin/activate
```

3- Install the dependencies
```
pip install -r reqs.txt
```
Note: This installs the packaged backend as Wheel file in dist/eon_case_study_dependencies-1.0.0-py3-none-any.whl

AWS Wrangler and pytest are installed separately. The thought process is to emulate the lambda function as the AWS 
Wrangler is attached as Lambda Layer.

4- Upload files to Bronze Bucket by the following command
```
raw_data_files_s3_uploader.py
```
You can validate the 5 uploads by looking into the S3 buckets and their corresponding events in the Queue from the localstack WEB UI or using the AWS CLI

5- Run the Bronze transformer by the following command
```
python local_s3_bronze_transformer.py
```
Ideally this should have been tested by invocation of the lambda function but we weren't able to run the Lambda function
as we deployed it Lambda Layers and Localstack only supports Layer with Pro subscription. Invocation of the Lambda function
gives error for Module Not found for now. Further details are attached in the Findings Section.

6- Ideally all the test cases should have been written inside each package but for the sake of case study and shortage of 
time, only 3 of them related to the Bronze Transformation Lambda have been written. You can run them by the following command:

```
pytest test/test_eon_data_lake.py
```


****Findings:****

***Module Not Found Error 'awswrangler' was faced however, a lambda layer for AWS Wrangler is already created and attached.
Since the development was done using Localstack which only supports Layers in the Pro mode, we weren't able to conduct 
further investigation. Also, due to the limited time, it wasn't possible to perform analysis and fix.***

To support the hypothesis: The current virtual env is also setup the same way i.e. the backend was installed as wheel file
and aws wrangler as a part of reqs.txt. If you open the Python Console by typing python and write 
``` 
from aws_utils.SQS import SQS
```
No error was faced which means that the wheel is installed separately and correctly