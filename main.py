import streamlit as st
from streamlit_option_menu import option_menu
from apps import Balances,Portfolio,Tickers,Transactions,Transfers,Wallet,About
from web3 import Web3
from ens.auto import ns


st.set_page_config(page_title="Shoda - Blockchain Explorer", page_icon="💰", layout="wide", initial_sidebar_state="expanded")


# setup constants 
connectedChains={
    "Ethereum":1,
    "Polygon":137,
    "Avalanche":43114,
    "Binance Smart Chain":56,
    "Klaytn":8217
}


infura_url='https://mainnet.infura.io/v3/1a8b2eb3cfe6493695013d90eec174a4' #your uri
w3 = Web3(Web3.HTTPProvider(infura_url))

apps = [
    {"func": Portfolio.app, "title": "Portfolio", "icon": "graph-up-arrow"},
    {"func": Balances.app, "title": "Balances", "icon": "cash-coin"},
    {"func": Tickers.app, "title": "Tickers", "icon": "bar-chart-steps"},
    {"func": Transactions.app, "title": "Transactions", "icon": "arrows-angle-contract"},
    # {"func": Transfers.app, "title": "Transfers", "icon": "send-check-fill"},
    {"func": Wallet.app, "title": "Wallet", "icon": "wallet2"},
    {"func": About.app, "title": "About", "icon": "info-circle"},
    
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

# setup  states variables 
params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = -1
if "address" in params:
    st.session_state["address"] = params["address"][0]
# else:
#     st.session_state["address"]="0xd0aD800d5799D114c2B165dA63D47708712B15e8"

st.session_state["chains"] = connectedChains


# Fill in sidebar data
with st.sidebar:
    selected_address = st.text_input("Address", key="address",value='0xd0aD800d5799D114c2B165dA63D47708712B15e8')
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        Shoda is a  simple blockchain explorer built using the covalent API.
    """
    )

if w3.isConnected():
    if not w3.isAddress(selected_address):        
        st.error("Invalid address entered in the sidebar, \n Please try again (ENS is not yet supported)")
        
    else:
        
        for app in apps:
            if app["title"] == selected:
                app["func"]()
                break