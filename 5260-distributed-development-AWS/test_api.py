import unittest
from unittest.mock import patch, MagicMock
import api_design

class TestAPIDesign(unittest.TestCase):
    
    def setUp(self):
        # Set up any common variables or configurations used in multiple tests
        self.event = {
            'httpMethod': 'POST',
            'headers': {'Content-Type': 'application/json'},
            'body': '{"key": "value"}'
        }
        self.context = {}  # Mock context if needed

    @patch('api_design.validateRequest')
    @patch('api_design.transform_to_widget_request')
    @patch('api_design.enqueueRequest')
    @patch('api_design.response')
    def test_lambda_handler(self, mock_response, mock_enqueueRequest, mock_transform_to_widget_request, mock_validateRequest):
        # Test lambda_handler function
        mock_validateRequest.return_value = True
        api_design.lambda_handler(self.event, self.context)
        mock_validateRequest.assert_called_once_with(self.event)
        mock_transform_to_widget_request.assert_called_once()
        mock_enqueueRequest.assert_called_once()
        mock_response.assert_called_once_with(200, "Request submitted successfully.")

    def test_validateRequest(self):
        # Test validateRequest function
        valid = api_design.validateRequest(self.event)
        self.assertTrue(valid)

        invalid_event = self.event.copy()
        invalid_event['httpMethod'] = 'GET'
        invalid = api_design.validateRequest(invalid_event)
        self.assertFalse(invalid)

    def test_transform_to_widget_request(self):
        # Test transform_to_widget_request function
        transformed_request = api_design.transform_to_widget_request(self.event)
        expected_output = {"key": "value"}
        self.assertEqual(transformed_request, expected_output)

    @patch('api_design.sqs_client.send_message')
    def test_enqueueRequest(self, mock_send_message):
        # Test enqueueRequest function
        widget_request = {"key": "value"}
        api_design.enqueueRequest(widget_request)
        mock_send_message.assert_called_once_with(
            QueueUrl=api_design.queue_url,
            MessageBody='{"key": "value"}'
        )

    def test_response(self):
        # Test response function
        resp = api_design.response(200, "Success")
        expected_resp = {
            "statusCode": 200,
            "body": '{"message": "Success"}'
        }
        self.assertEqual(resp, expected_resp)

        resp = api_design.response(400, "Bad Request")
        expected_resp = {
            "statusCode": 400,
            "body": '{"message": "Bad Request"}'
        }
        self.assertEqual(resp, expected_resp)


if __name__ == '__main__':
    unittest.main()
