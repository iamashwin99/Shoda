
import streamlit as st
import time
import requests
import json
import plotly.express as px
import pandas as pd

@st.cache(allow_output_mutation=True)
def fetchBalancePerChain(chain_id, selected_address):
    avaliableChains = st.session_state["chains"]
    response = requests.get(
        f"https://api.covalenthq.com/v1/{chain_id}/address/{selected_address}/portfolio_v2/?&key=ckey_4cd27b24d9c248e0a0727d3a7dd")
    data = json.loads(response.text)['data']['items']
    # st.json(data)
    if len(data) == 0:
        st.error(
            f"No data found for given address in {avaliableChains.index(chain_id)}")
    
    numOfTokens = len(data)
    totalNumDays = len(data[0]['holdings'])
    dayArray = []
    totlaValuationArray = []
    for day in range(totalNumDays):
        daystamp = data[0]['holdings'][day]["timestamp"]
        totalUSDVal = 0
        for tokenPos in range(numOfTokens):

            # tokenBase = float( 10**(data[tokenPos]['contract_decimals']) )
            # try:
            #     tokenClosePrice = float( data[tokenPos]['holdings'][day]['quote_rate'])
            # except:
            #     tokenClosePrice = 0
            # tokenCloseBalance = float( data[tokenPos]['holdings'][day]['close']['balance'] )
            # tokenValuation = (tokenClosePrice/tokenBase)*tokenCloseBalance

            try:
                tokenValuation = float(data[tokenPos]['holdings'][day]['close']['quote'])
            except:
                tokenValuation = 0
            totalUSDVal += tokenValuation
        dayArray.append(daystamp)
        totlaValuationArray.append(totalUSDVal)
    return dayArray, totlaValuationArray


def app():
    selected_address = st.session_state["address"]
    st.title("Portfolio :briefcase:")

    avaliableChains = st.session_state["chains"]
    df = pd.DataFrame()

    selectedChains = st.multiselect(
        "Select chains :", avaliableChains.keys(), default=['Ethereum'])
    with st.spinner(f"Fetching data for {selected_address}"):

        for chain in selectedChains:
            chain_id = avaliableChains[chain]
            dayArray, totlaValuationArray = fetchBalancePerChain(
                chain_id, selected_address)
            dfGivenChain = pd.DataFrame(
                {"Day": dayArray, "Valuation": totlaValuationArray, "Chain":chain})

            #append dfGivenChain to df
            df = df.append(dfGivenChain)
            
        st.write("Last `30` days portfolio valuation for selected chains:")
        fig = px.line(df,x="Day", y="Valuation", color="Chain",markers=True)
        st.plotly_chart(fig)
        st.info(""" **Note**: Portfolio valuation is calculated as the sum of all tokens values in the wallet.
         Some tokens could be **fake** tokens with  no intrensic value but with intent only to **scam** the user up on a DEX trade.
          Covalent API which is used in thei projects do not isolate them, thus the valuation showed here could be skewed because of that. Please be carefull about trade of such token """)
