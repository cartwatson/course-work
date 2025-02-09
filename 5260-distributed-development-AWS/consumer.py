import os
import logging
import argparse
import json
import time
import boto3
from botocore.exceptions import ClientError

# Define the main function
def main():
    # Configure logging
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logging.basicConfig(filename=os.path.join(logs_dir, 'consumer.log'), 
                        level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        filemode='w')
    
    # Get command-line arguments
    args = parse_arguments()

    # Init AWS resources
    s3_client = boto3.client('s3', region_name=args.region)
    dynamodb = boto3.resource('dynamodb', region_name=args.region)
    sqs_client = boto3.client('sqs', region_name=args.region)
    
    # Get the SQS queue URL
    queue_url = None
    if args.queue_name:
        queue_url = sqs_client.get_queue_url(QueueName=args.queue_name)['QueueUrl']
        logging.info(f"SQS queue URL: {queue_url}")

    # Polling loop
    while True:
        # Keep functionality with S3
        if args.bucket_name: # If bucket name exists (eg. not "" or None)
            request = get_next_widget_request(s3_client, args.bucket_name)
            if request:
                process_request(request, args.storage_strategy, s3_client, dynamodb, args.bucket_name)
        
        # Handle SQS
        if queue_url:
            messages = sqs_client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=10)
            if 'Messages' in messages:
                for message in messages['Messages']:
                    sqs_request = json.loads(message['Body'])
                    process_request(sqs_request, args.storage_strategy, s3_client, dynamodb)

                    # Delete message from the queue after processing
                    receipt_handle = message['ReceiptHandle']
                    sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
        
        # Wait for 100ms
        time.sleep(0.1)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Widget Consumer Program")
    parser.add_argument("--region", required=False, help="AWS Region", default="us-east-1")
    parser.add_argument("--storage-strategy", choices=['s3', 'dynamodb'], required=True, help="Storage strategy (s3 or dynamodb)")
    parser.add_argument("--bucket-name", required=False, help="Name of the S3 bucket for widget requests")
    parser.add_argument("--queue-name", required=False, help="Name of the SQS queue for widget requests")
    return parser.parse_args()

def get_next_widget_request(s3_client, bucket_name):
    try:
        logging.info("Fetching the next widget request from the bucket")
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        # Check if the bucket has any objects
        if 'Contents' not in response:
            return None

        # Sort objects by key
        objects = sorted(response['Contents'], key=lambda obj: obj['Key'])

        # Get the first object (smallest key)
        first_object_key = objects[0]['Key']

        # Get the object content
        object_content = s3_client.get_object(Bucket=bucket_name, Key=first_object_key)
        
        # Read the content of the object
        request_data = object_content['Body'].read().decode('utf-8')
        request = json.loads(request_data)

        return request

    except ClientError as e:
        logging.error(f"An error occurred while fetching widget request: {e}")
        return None


def process_request(request, storage_strategy, s3_client, dynamodb, bucket_name=None):
    try:
        # Determine the type of request
        request_type = request.get('type')
        print(f"Processing request: {request}")
        logging.info(f"Processing request: {request}")

        # Process according to request type
        if request_type == 'create':
            process_create_request(request, storage_strategy, s3_client, dynamodb, bucket_name)
        elif request_type == 'update':
            process_update_request(request, storage_strategy, s3_client, dynamodb, bucket_name)
        elif request_type == 'delete':
            process_delete_request(request, storage_strategy, s3_client, dynamodb, bucket_name)
        else:
            print(f"Unknown request type: {request_type}")

    except Exception as e:
        print(f"An error occurred while processing the request: {e}")
        logging.error(f"An error occurred while processing the request: {e}")

def process_create_request(request, storage_strategy, s3_client, dynamodb, bucket_name):
    if storage_strategy == 's3':
        store_in_s3(request, s3_client, bucket_name)
    elif storage_strategy == 'dynamodb':
        store_in_dynamodb(request, dynamodb)

def process_update_request(request, storage_strategy, s3_client, dynamodb, bucket_name):
    # Update widget data in S3
    if storage_strategy == 's3':
        # Use request to construct the object key
        owner = request['owner'].replace(" ", "-").lower()
        widget_id = request["widgetId"]
        key = f"widgets/{owner}/{widget_id}"
        new_data = request['new_data']
        # Fetch the existing object
        current_data = s3_client.get_object(Bucket=bucket_name, Key=key)['Body'].read().decode('utf-8')
        current_data = json.loads(current_data)
        # Modify the data
        current_data.update(new_data)
        # Re-upload the updated data to S3
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(current_data)) 
        logging.info(f"Widget updated in S3 with key: {key}")
        
    # Update widget data in DynamoDB
    elif storage_strategy == 'dynamodb':
        table = dynamodb.Table('widgets')
        table.update_item(
            Key={"widgetId": widget_id},
            UpdateExpression='SET attribute_name = :val1',
            ExpressionAttributeValues={':val1': new_data}
        )
        logging.info(f"Widget updated in DynamoDB with ID: {widget_id}")

def process_delete_request(request, storage_strategy, s3_client, dynamodb, bucket_name):
    # Parse the request to get the widget identifier
    widget_id = request["widgetId"]

    # Delete widget data from S3
    if storage_strategy == 's3':
        # Use request to construct the object key
        owner = request['owner'].replace(" ", "-").lower()
        widget_id = request["widgetId"]
        key = f"widgets/{owner}/{widget_id}"
        # then delete the object
        s3_client.delete_object(Bucket=bucket_name, Key=key)
        logging.info(f"Widget deleted from S3 with key: {key}")

    # Delete widget data from DynamoDB
    elif storage_strategy == 'dynamodb':
        table = dynamodb.Table('widgets')
        table.delete_item(
            Key={"widgetId": widget_id}
        )
        logging.info(f"Widget deleted from DynamoDB with ID: {widget_id}")

def store_in_s3(request, s3_client, bucket_name):
    owner = request['owner'].replace(" ", "-").lower()
    widget_id = request['widgetId']
    key = f"widgets/{owner}/{widget_id}"

    try:
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(request))
        print(f"Widget stored in S3 with key: {key}")
        logging.info(f"Widget stored in S3 with key: {key}")
    except ClientError as e:
        print(f"Error storing widget in S3: {e}")
        logging.error(f"Error storing widget in S3: {e}")

def store_in_dynamodb(request, dynamodb):
    table = dynamodb.Table('widgets')
    try:
        # Flatten the request dictionary for DynamoDB
        item = {**request, **request.pop('otherAttributes', {})}
        table.put_item(Item=item)
        print(f"Widget stored in DynamoDB with ID: {request['widgetId']}")
        logging.info(f"Widget stored in DynamoDB with ID: {request['widgetId']}")
    except ClientError as e:
        print(f"Error storing widget in DynamoDB: {e}")
        logging.error(f"Error storing widget in DynamoDB: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
