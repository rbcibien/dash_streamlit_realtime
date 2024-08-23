import os
from dotenv import load_dotenv
import requests
import datetime


load_dotenv()

DOMAIN = os.getenv("JIRA_DOMAIN")
EMAIL = os.getenv("JIRA_EMAIL")
AUTH_KEY = os.getenv("JIRA_AUTH_KEY")
# DATABASE_URL = os.getenv("DATABASE_URL")

def get_jira_response(email:str, api_token:str, url:str, headers:dict, params:dict=None):
    response = requests.get(url, auth=(email, api_token), headers=headers, params=params)
    return response.json()


def datetime_to_unix_milliseconds(dt:datetime):
    # Get Unix timestamp in seconds and convert to milliseconds
    unix_timestamp_ms = int(dt.timestamp() * 1000)
    return unix_timestamp_ms

def datetime_string_to_unix_milliseconds(dt_string:str, date_format='%Y-%m-%d'):
    # Parse the string into a datetime object
    dt = datetime.datetime.strptime(dt_string, date_format)
    # Get Unix timestamp in milliseconds
    unix_timestamp_ms = int(dt.timestamp() * 1000)
    return unix_timestamp_ms

def get_unix_milliseconds(dt):
    if isinstance(dt, datetime.datetime):
        return datetime_to_unix_milliseconds(dt)
    elif isinstance(dt, str):
        return datetime_string_to_unix_milliseconds(dt)
    else:
        print('Please select a datetime or string data.')