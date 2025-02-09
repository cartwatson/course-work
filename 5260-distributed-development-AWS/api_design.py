import json
import boto3
import logging

logging.basicConfig(level=logging.INFO)  # Set the log level to INFO

# Initialize the SQS client
sqs_client = boto3.client('sqs', region_name='us-east-1')
queue_url = sqs_client.get_queue_url(QueueName='cs5260-requests')['QueueUrl']
logging.info(f"SQS queue URL: {queue_url}")

def lambda_handler(event, context):
    logging.info(json.dumps(event))
    try:
        if validateRequest(event):
            # NOTE: Data flows from json to dict to json; this is not necessary
            # but it does make it more extensible for the future if one needed
            # to generate fields from the existing data 
            widget_request = transform_to_widget_request(event)
            logging.info(widget_request) #DEBUG
            enqueueRequest(widget_request)
            return response(200, "Request submitted successfully.")
        else:
            return response(400, "Invalid request.")
    except Exception as e:
        return response(500, f"Internal server error: {e}")

def validateRequest(event):
    # If the request is a POST request with Content-Type as application/json, then it is valid
    if event['httpMethod'] == 'POST':
        if event.get('headers').get('Content-Type') == 'application/json':
            logging.info("validated request")
            return True
    return False

def transform_to_widget_request(event):
    return json.loads(event['body'])

def enqueueRequest(widget_request):
    # Send the message to SQS
    try:
        sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(widget_request)
        )
    except Exception as e:
        logging.error(f"Unable to send message to SQS: {e}")

def response(status_code, message):
    return {
        "statusCode": status_code,
        "body": json.dumps({"message": message})
    }
