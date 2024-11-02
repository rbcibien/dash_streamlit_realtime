import streamlit as st
import time
import datetime
import matplotlib.pyplot as plt

from jira_api.issues import transform_issues_to_dataframe


# Streamlit app
st.title('Date Range Selector for Dataframe')

# Date input from the user
start_date = st.date_input('Select Start Date', value=datetime.date(2023, 1, 1))
end_date = st.date_input('Select End Date', value=datetime.date.today())

if st.button('Get Data'):
    if start_date > end_date:
        st.error('Error: End Date must be after Start Date.')
    else:
        # Call the function and display the dataframe
        df = transform_issues_to_dataframe(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        with st.spinner("Wait for it..."):
            time.sleep(2)
        st.success("Done!")
        
        total_worklog = df['worklog_hours'].sum()
        st.write(f'Total worklog hours: {total_worklog:.2f}')
        
        total_hours_by_type = df.groupby('issue_type')['worklog_hours'].sum().reset_index().sort_values(by='worklog_hours', ascending=False)
        st.subheader('Total Worked Hours by Issue Type')
        st.write(total_hours_by_type)
        
        # Total hours by day
        hours_by_day = df.groupby('worklog_start')['worklog_hours'].sum().reset_index()

        # Calculate running total
        hours_by_day['running_total'] = hours_by_day['worklog_hours'].cumsum()

        # Plotting
        fig, ax = plt.subplots()
        ax.bar(hours_by_day['worklog_start'], hours_by_day['worklog_hours'], color='skyblue', label='Hours per Day')
        ax.plot(hours_by_day['worklog_start'], hours_by_day['running_total'], color='orange', label='Running Total')

        plt.xticks(rotation=45)
        plt.xlabel('worklog_start')
        plt.ylabel('Hours')
        plt.title('Work Hours and Running Total')
        plt.legend()
        st.pyplot(fig)

        
        st.write('Dataframe based on selected dates:')
        st.dataframe(df)

