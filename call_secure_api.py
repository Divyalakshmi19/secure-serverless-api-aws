import boto3
from requests_aws4auth import AWS4Auth
import requests

# Configuration
region = 'eu-north-1'
service = 'execute-api'
api_url = 'https://ytvs25aqs6.execute-api.eu-north-1.amazonaws.com/dev'  # your API URL

# Get credentials from profile
session = boto3.Session(profile_name='secureapiuser')
credentials = session.get_credentials().get_frozen_credentials()

# Set up auth
auth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    region,
    service,
    session_token=credentials.token
)

# Send GET request
response = requests.get(api_url, auth=auth)

# Output
print("Status Code:", response.status_code)
print("Response Body:", response.text)
