import requests
import json
import os

def start_job():
    # Set the API endpoint
    url = "https://nvs.domino-eval.com/v4/jobs/start"

    # Get API key from environment variable
    api_key = os.getenv('DOMINO_USER_API_KEY')
    if not api_key:
        raise ValueError("API key not found in environment variable DOMINO_USER_API_KEY")

    # Set the headers
    headers = {
        "accept": "application/json",
        "X-Domino-Api-Key": api_key,
        "Content-Type": "application/json"
    }

    # Set the payload from the JSON file
    data = {
        "projectId": "651a0d1c4c3fc9080dec1b99",
        "commandToRun": "main.py",
        "overrideHardwareTierId": "large-k8s",
        "environmentId": "6519f7d2c507a51d7d5c3876",
        "title": "API Started"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))