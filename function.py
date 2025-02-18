import json
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import requests


def lambda_handler(event, context):
    try:
        # Parse the incoming request body
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event

        ingredients = body.get('ingredients', [])
        if not ingredients:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No ingredients provided'})
            }

        # AWS region and endpoint configuration
        region = "us-east-1"  # Replace with your region
        bedrock_endpoint = f"https://bedrock.{region}.amazonaws.com"
        model_id = "amazon.titan-text-premier-v1:0"
        url = f"{bedrock_endpoint}/model/{model_id}/invoke"

        # AWS credentials setup
        session = boto3.Session()
        credentials = session.get_credentials().get_frozen_credentials()

        # Prepare and sign the request
        request = AWSRequest(method="POST", url=url, data=json.dumps({"ingredients": ingredients}))
        SigV4Auth(credentials, "bedrock", region).add_auth(request)

        headers = dict(request.headers)
        headers["Content-Type"] = "application/json"

        # Send the request to the Bedrock endpoint
        response = requests.post(url, headers=headers, json={"ingredients": ingredients})

        if response.status_code != 200:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'error': response.text})
            }

        # Parse the response from the model
        model_output = response.json()
        recipe = model_output.get('recipe', 'No recipe found')

        return {
            'statusCode': 200,
            'body': json.dumps({'recipe': recipe})
        }

    except Exception as e:
        print("Error occurred: ", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
