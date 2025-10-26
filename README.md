# ContactProject

This project contains a simple **Contact Us web application** using AWS Lambda and DynamoDB.


## Features

- **AWS Lambda** backend to handle GET & POST requests
- **DynamoDB** to store contact messages
- **HTML/JS frontend** to submit messages and display all stored messages
- **CORS enabled** for cross-origin requests
- **Optional JSON test events** for Lambda testing

## Setup Instructions

1. Create a DynamoDB table named `nikita` with `id` as the partition key (String).
2. Update Lambda function `lambda_function.py` and deploy it in the same AWS region as DynamoDB.
3. Set up API Gateway with **Lambda Proxy Integration** and enable CORS (GET, POST, OPTIONS).
4. Replace `YOUR_LAMBDA_API_URL` in `frontend/index.html` with the API Gateway endpoint URL.
5. Open `frontend/index.html` in browser or access via Lambda-served HTML page.
6. Submit messages and see them saved in DynamoDB and displayed live on the page.

## Testing Lambda

Use the provided sample JSON event in `config/sample_event.json` to test POST requests in Lambda console.

## Notes

- Lambda IAM role must have **AmazonDynamoDBFullAccess** permission.
- `boto3` is pre-installed in AWS Lambda Python runtime.

