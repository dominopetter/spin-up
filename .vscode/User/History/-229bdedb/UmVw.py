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
        "projectId": "6522b265eee6474600a1b418",
        "commandToRun": "main.py",
        "overrideHardwareTierId": "large-k8s",
        "environmentId": "6519f7d2c507a51d7d5c3876",
        "title": "PYTHON API Started"
    }

    # Set the payload from the JSON file
    # dataSAS = {
    #     "projectId": "6522b265eee6474600a1b418",
    #     "commandToRun": "main.sas",
    #     "overrideHardwareTierId": "large-k8s",
    #     "environmentId": "651b17ba8f83f33663a335ec",
    #     "title": "SAS API Started"
    # }
    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # response = requests.post(url, headers=headers, dataSAS=json.dumps(data))