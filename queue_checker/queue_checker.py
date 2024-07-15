import json
from aws_utils.SQS import SQS

def invoke_step_functions(function_name):
    #Empty function for now as we are not deploying the step functions in the scope of this assignement right now
    #I will try to add step function deployment if I have more time
    # sfn = boto3.client('stepfunctions')

    # Start execution of the Step Function
    # response = sfn.start_execution(
    #     stateMachineArn=f'arn:aws:states:<region>:<account-id>:stateMachine:{step_function_name}',
    #     # You may need to customize the stateMachineArn based on your AWS setup
    #     input="{}")
    pass

def check_messages_and_call_step_functions(queue_name, step_functions_arn):
    if SQS(queue_name).check_queue_for_new_messages():
        invoke_step_functions(step_functions_arn)
    else:
        print("No new messages in the queue.")


if __name__ == "__main__":
    # To be extracted from ENV Variables
    QUEUE_NAME = "EonMessageQueue"
    STEP_FUNCTION_ARN = "arn:aws:states:<region>:<account-id>:stateMachine:{step_function_name}"
    check_messages_and_call_step_functions(QUEUE_NAME, STEP_FUNCTION_ARN)


# def lambda_handler(event, context):
#
#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "hello world",
#         }),
#     }
