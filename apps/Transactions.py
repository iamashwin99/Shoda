import streamlit as st
import time
import requests
import json
import plotly.express as px
import pandas as pd
from st_material_table import st_material_table
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

def app():
    selected_address = st.session_state["address"]
    avaliableChains = st.session_state["chains"]
    st.title("Transactions :open_file_folder:")
    # st.write("This section is work in progress")
    with st.spinner("Fetching data ..."):
        selectedChain = st.selectbox("Select Chain", avaliableChains.keys(),0)
        response = requests.get(f"https://api.covalenthq.com/v1/{avaliableChains[selectedChain]}/address/{selected_address}/transactions_v2/?key=ckey_4cd27b24d9c248e0a0727d3a7dd")
        df = pd.DataFrame(response.json()['data']['items'])
        # drop log_events column from df
        dffinal = df.drop(columns=['log_events'])
       
        # dffinal = df[['logo_url','contract_name','contract_ticker_symbol','contract_address','quote_rate','rank','contract_decimals']].dropna()
        # # # Rename the dffinal colums as Logo contract Name, symbol, balance, Valuation symbol
        # dffinal.columns = ['Logo','Contract Name','Contract Symbol','Address','USD Value','MarketCap rank','Decimals']
        # format_dict = {}
        # format_dict['Logo'] = path_to_image_html
    # st.write(df.dropna())
    # st.write("list of all tickers sorted by market cap.")
    st.markdown((df.to_html(escape=False )) , unsafe_allow_html=True)