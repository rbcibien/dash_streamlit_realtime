import streamlit as st
import time

from jira_api import issues

with st.spinner("Wait for it..."):
    time.sleep(5)
st.success("Done!")
"Hello world"