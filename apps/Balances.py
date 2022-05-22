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
     st.title("Balances :bar_chart:")
     with st.spinner("Fetching data ..."):
          selectedChain = st.selectbox("Select Chain", avaliableChains.keys(),0)

          response = requests.get(f"https://api.covalenthq.com/v1/{avaliableChains[selectedChain]}/address/{selected_address}/balances_v2/?key=ckey_4cd27b24d9c248e0a0727d3a7dd")
          df = pd.DataFrame(response.json()['data']['items'])
          dffinal = df[['logo_url','contract_name','contract_ticker_symbol','balance','quote_rate']].dropna()
          # Rename the dffinal colums as Logo contract Name, symbol, balance, Valuation symbol
          dffinal.columns = ['Logo','Contract Name','Contract Symbol','Balance','USD Value']
          # round the USD Value column to 3 Decimals and convert to string
          dffinal['USD Value'] = dffinal['USD Value'].round(3).astype(str)
          
          format_dict = {}
          format_dict['Logo'] = path_to_image_html
     # st.dataframe(dffinal)
     st.markdown(((dffinal.to_html(escape=False ,formatters=format_dict))) , unsafe_allow_html=True)
     # _ = st_material_table(df)

     