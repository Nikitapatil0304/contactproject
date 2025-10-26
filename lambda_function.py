import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('nikita')

def lambda_handler(event, context):
    method = event.get('httpMethod', '')
    params = event.get('queryStringParameters', {})

    # Serve HTML (optional)
    if method == 'GET' and not params:
        return serve_html()

    # GET messages
    if method == 'GET' and params.get('getData') == 'true':
        response = table.scan()
        items = sorted(response.get('Items', []), key=lambda x: x.get('timestamp', ''), reverse=True)
        return send_json(200, {'contacts': items})

    # POST message
    if method == 'POST':
        body = json.loads(event.get('body', '{}'))
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        if not (name and email and message):
            return send_json(400, {'error': 'All fields are required'})

        item = {
            'id': str(uuid.uuid4()),
            'name': name,
            'email': email,
            'message': message,
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }
        table.put_item(Item=item)
        return send_json(200, {'message': 'Message saved!', 'data': item})

    # OPTIONS CORS preflight
    if method == 'OPTIONS':
        return send_json(200, {'message': 'CORS preflight OK'})

    return send_json(405, {'error': 'Method Not Allowed'})


def serve_html():
    html_file_path = '../frontend/index.html'
    with open(html_file_path, 'r') as f:
        content = f.read()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"},
        "body": content
    }


def send_json(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body)
    }

