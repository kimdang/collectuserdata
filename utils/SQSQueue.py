import boto3 
import os 


class Queue:
    def __init__(self, REGION, ACCESS_KEY, SECRET_KEY, QueueName):
        self.sqs = boto3.resource('sqs', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=REGION)
        self.queue_name = QueueName

    def send_message(self, filename, bucketname):
        ## check that queue exists
        try:
            queue = self.sqs.get_queue_by_name(QueueName=self.queue_name)
        except KeyError: 
            print(f"{self.queue_name} cannot be found.")

        ## filename and bucketname are added to queue
        response = queue.send_message(MessageBody='test', MessageAttributes={
            'filename': {
                'DataType': 'String', 
                'StringValue': filename,
            },
            'bucketname': {
                'DataType': 'String', 
                'StringValue': bucketname,
            },
        })
        print(f"{filename} has been added to queue.")

        

