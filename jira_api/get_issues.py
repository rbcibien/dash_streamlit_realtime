from utils import get_jira_response
from utils import DOMAIN, EMAIL, AUTH_KEY

# JIRA API credentials
email = EMAIL
api_token = AUTH_KEY

# Request headers
headers = {
    'Content-Type': 'application/json'
}

def issue_params_func(startDate:str='startOfMonth()', endDate:str='endOfMonth()', startAt:int=0):
    params = {
        'jql': f'worklogAuthor=currentUser() AND worklogDate >= {startDate} AND worklogDate <= {endDate}',
        'fields': 'project,issuetype,worklog,assignee,status,summary',
        'maxResults': 100,
        'startAt': startAt,
    }
    return params

def get_user_issues_in_period(
        startDate:str,
        endDate:str,
        startAt:int=0,
        email:str=email,
        api_token:str=api_token,
        url:str=f'https://{DOMAIN}.atlassian.net/rest/api/3/search',
        headers:dict=headers,
        loop:bool=True
    ):
    """
    Função que retorna as Issues do usuário atual em um período selecionado.

    args: startDate, endDate
    return: list of Issues
    """
    issues = []
    while loop:
        params = issue_params_func(startDate, endDate, startAt)
        print(url+"?jql="+params['jql']+"&fileds"+params['fields'])
        response = get_jira_response(email, api_token, url, headers, params)

        issues = response['issues']
        
        total = response['total']
        startAt = response['startAt']
        maxResults = response['maxResults']
        endAt = startAt + maxResults

        loop = total > endAt
        startAt = endAt if loop else startAt

    return issues
