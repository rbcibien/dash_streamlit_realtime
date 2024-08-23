from .utils import get_jira_response
from .utils import DOMAIN, EMAIL, AUTH_KEY

# JIRA API credentials
email = EMAIL
api_token = AUTH_KEY

# Request headers
headers = {
    'Content-Type': 'application/json'
}

def get_current_user_id(
        email:str=email,
        api_token:str=api_token,
        url:str=f'https://{DOMAIN}.atlassian.net/rest/api/3/myself',
        headers:dict=headers,
    ):
        response = get_jira_response(email, api_token, url, headers)
        user_id = response['accountId']
        return user_id