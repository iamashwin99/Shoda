import streamlit as st
import time
import requests
import json
import plotly.express as px
import pandas as pd

def app():
     selected_address = st.session_state["address"]
     avaliableChains = st.session_state["chains"]
     st.title("About :information_source:")
     st.write("""
     This project is an entry for ETH Global HackMoney 2022 hackathon

    Use the Sidebar for Navigation through the various use cases of the WebApp!

    Shoda serves the purpose of integrating multiple networks using Covalent APIs and making a site with which you can search transactions, balance etc without having to check individual network explorer site.
    
     Working with this project has enabled me to connect to developers in this field and motivated me to look for future opportunities in the field.

    Powered by: Covalent API  
     """)
     st.image("https://www.covalenthq.com/static/images/covalent-logo.png", width=150)