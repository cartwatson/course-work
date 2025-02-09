import unittest
from unittest.mock import patch
import consumer

class TestWidgetConsumer(unittest.TestCase):
    
    @patch('consumer.store_in_s3')
    @patch('consumer.store_in_dynamodb')
    def test_process_request_create_s3(self, mock_dynamo, mock_s3):
        request = {"type": "create", "widget_id": "1", "owner": "John Doe"}
        consumer.process_request(request, 's3', None, None)
        mock_s3.assert_called_once()
        mock_dynamo.assert_not_called()

    @patch('consumer.store_in_s3')
    @patch('consumer.store_in_dynamodb')
    def test_process_request_create_dynamodb(self, mock_dynamo, mock_s3):
        request = {"type": "create", "widget_id": "1", "owner": "John Doe"}
        consumer.process_request(request, 'dynamodb', None, None)
        mock_s3.assert_not_called()
        mock_dynamo.assert_called_once()

    @patch('consumer.boto3.client')
    def test_update_widget(self, mock_boto3_client):
        mock_s3_client = mock_boto3_client.return_value
        mock_s3_client.get_object.return_value = {'Body': b'{"existing": "data"}'}
        consumer.update_widget('some_widget_id', {'new': 'data'})
        mock_s3_client.get_object.assert_called_once_with(Bucket='bucket_name', Key='some_key')
        mock_s3_client.put_object.assert_called_once()

    @patch('consumer.boto3.client')
    def test_delete_widget(self, mock_boto3_client):
        mock_s3_client = mock_boto3_client.return_value
        consumer.delete_widget('some_widget_id')
        mock_s3_client.delete_object.assert_called_once_with(Bucket='bucket_name', Key='some_key')

if __name__ == '__main__':
    unittest.main()
