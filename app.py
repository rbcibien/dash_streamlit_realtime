import streamlit as st
import time
import datetime

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
            time.sleep(5)
        st.success("Done!")
        st.write('Dataframe based on selected dates:')
        st.dataframe(df)

