from aws_utils.boto3_manager import get_sqs_client
from local_utils.LoggerGenerator import LoggerGenerator


class SQS:
    def __init__(self, name):
        self.__name = name
        self.__boto3_client = get_sqs_client()
        self.__queue_url = self.__boto3_client.get_queue_url(QueueName=self.__name)['QueueUrl']
        self.__logger = LoggerGenerator().get_file_logger("file","SQSLogger")

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


    def check_queue_for_new_messages(self):
        self.__logger.log_debug(f"Checking Queue: {self.name} for new messages")
        return len(self.boto3_client.receive_message(
            QueueUrl=self.queue_url
        ).get('Messages',[])) > 0

    def delete_all_messages(self):
        self.__logger.log_debug(f"Deleting all Messages from Queue: {self.name}")
        self.boto3_client.purge_queue(QueueUrl=self.queue_url)