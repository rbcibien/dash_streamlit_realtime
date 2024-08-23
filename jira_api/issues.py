import pandas as pd
from datetime import datetime

from .get_issues import get_user_issues_in_period
from .get_user import get_current_user_id

def transform_issues_to_dataframe(start_date:str, end_date:str):
    df = pd.DataFrame()
    issues = get_user_issues_in_period(start_date, end_date)
    current_user_id = get_current_user_id()

    for issue in issues:
        issue_worklog = 0
        worklog_start = 'a'
        for worklog in issue['fields']['worklog']['worklogs']:
            if worklog['author']['accountId'] == current_user_id and worklog['started'] >= start_date and worklog['started'] <= end_date:
                issue_worklog += worklog['timeSpentSeconds']
                worklog_start = min(worklog_start, worklog['started'])

        new_row = {
            "issue_id": issue['id'],
            "key": issue['key'],
            "self": issue['self'],
            "summary": issue['fields']['summary'],
            "project_id": issue['fields']['project']['id'],
            "project_key": issue['fields']['project']['key'],
            "project_self": issue['fields']['project']['self'],
            "project_name": issue['fields']['project']['name'],
            'worklog_hours': issue_worklog / 3600,
            'worklog_start': datetime.strptime(worklog_start, '%Y-%m-%dT%H:%M:%S.%f%z')
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df