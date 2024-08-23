import pandas as pd
from get_issues import get_user_issues_in_period

def transform_issues_to_dataframe(issues, current_user_id, start_date, end_date):
    df = pd.DataFrame()
    issues = get_user_issues_in_period(start_date, end_date)

    for issue in issues:
        issue_worklog = 0
        for worklog in issue['fields']['worklog']['worklogs']:
            if worklog['author']['accountId'] == current_user_id and worklog['started'] >= start_date and worklog['started'] <= end_date:
                issue_worklog += worklog['timeSpentSeconds']

        new_row = {
        "issue_id": issue['id'],
        "key": issue['key'],
        "self": issue['self'],
        "summary": issue['fields']['summary'],
        "project_id": issue['fields']['project']['id'],
        "project_key": issue['fields']['project']['key'],
        "project_self": issue['fields']['project']['self'],
        "project_name": issue['fields']['project']['name'],
        'worklog_hours': issue_worklog / 3600
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df