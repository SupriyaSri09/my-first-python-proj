from tokenize import tabsize

import streamlit as st
import datetime

st.title("Arnav's Tasks"
        )
today_date = datetime.datetime.now()
today_date_str = today_date.strftime("%m-%B-%y")


items =["SATS English Reasoning","SATS Maths Reasoning","SATS English RGrammer","SATS Arithmatic"]

tab = ["Pending Task","Completed Task"]
pendingTaskTab,completedTaskTab = st.tabs(tab)
with pendingTaskTab:
    st.subheader(f"Task for {today_date_str}")
    for item in items:
        st.checkbox(item,key=f"pendingTaskTab_{item}")

with completedTaskTab:
    st.subheader(f"Task for {today_date_str}")
    for item in items:
        st.checkbox(item,key=f"completedTaskTab{item}")

