from aws_utils.boto3_manager import get_sqs_client


class SQS:
    def __init__(self, name):
        self.__name = name
        self.__boto3_client = get_sqs_client()
        self.__queue_url = self.__boto3_client.get_queue_url(QueueName=self.__name)['QueueUrl']

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def boto3_client(self):
        return self.__boto3_client

    @property
    def queue_url(self):
        return self.__queue_url


    def get_new_messages(self):
        return self.boto3_client.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=2,
            VisibilityTimeout=0,
        ).get('Messages',[])

    def remove_messages_batch(self, messages):
        self.boto3_client.delete_message_batch(
            QueueUrl = self.queue_url,
            Entries = messages
        )

    def remove_message(self, receipt_handle):
        self.boto3_client.delete_message(
            QueueUrl = self.queue_url,
            ReceiptHandle = receipt_handle
        )

    def check_queue_for_new_messages(self):
        return len(self.get_new_messages()) > 0

    def delete_all_messages(self):
        self.boto3_client.purge_queue(QueueUrl=self.queue_url)