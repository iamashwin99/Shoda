
import streamlit as st
import time

def app():
    st.title("Transactions :open_file_folder:")
    st.write("This section is work in progress")
    with st.spinner("Fetching data ..."):
        time.sleep(5)