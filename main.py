import streamlit as st
from streamlit_option_menu import option_menu
from apps import Balances,Portfolio,Tickers,Transactions,Transfers,Wallet

st.set_page_config(page_title="Shoda - Blockchain Explorer", page_icon="💰", layout="wide")

apps = [
    {"func": Portfolio.app, "title": "Portfolio", "icon": "graph-up-arrow"},
    {"func": Balances.app, "title": "Balances", "icon": "cash-coin"},
    {"func": Tickers.app, "title": "Tickers", "icon": "bar-chart-steps"},
    {"func": Transactions.app, "title": "Transactions", "icon": "arrows-angle-contract"},
    {"func": Transfers.app, "title": "Transfers", "icon": "send-check-fill"},
    {"func": Wallet.app, "title": "Wallet", "icon": "wallet2"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0


with st.sidebar:
    selected_address = st.text_input("Address", "")
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
for app in apps:
    if app["title"] == selected:
        app["func"]()
        break