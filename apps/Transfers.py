
import streamlit as st
import time

def app():
    st.title("Transfers :credit_card:")
    with st.spinner("Fetching data ..."):
        time.sleep(5)