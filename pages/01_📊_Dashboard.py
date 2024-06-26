

# #
# from streamlit_option_menu import option_menu
# from ta.volatility import BollingerBands
# from ta.trend import MACD, EMAIndicator, SMAIndicator
# from ta.momentum import RSIIndicator
# import datetime
# from datetime import date
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsRegressor
# from xgboost import XGBRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.ensemble import ExtraTreesRegressor
# from sklearn.metrics import r2_score, mean_absolute_error
#
# #
# # with st.sidebar:
# #     selected = option_menu(
# #         menu_title = "main menu",
# #         options = ["one", "two", "three"]
# #
# # )
# # if selected == "one":
# #     st.write(f"you have selected {selected}")
# # if selected == "two":
# #     st.write(f"you have selected {selected}")
# # if selected == "three":
# #     st.write(f"you have selected {selected}")
# #
#
# import numpy as np
# import yfinance as yf
# from keras.models import load_model
# # from prophet import Prophet
# # from prophet.plot import plot_plotly
# from plotly import graph_objects as go
# from stocknews import StockNews
# import matplotlib.pyplot as plt
# import pandas as pd
# import streamlit as st
#
# ############################################################
# # tickers = st.sidebar.text_input("Tickers")
# # stocks = {"DOW JONES":"^DJI","NASDAQ":"^IXIC","GOLD":"GC=F","BITCOIN":"BTC-USD","AMAZON":"AMZN","APPLE":"APPL","TESLA":"TSLA","GOOGLE":"GOOG","META":"META","MICROSOFT":"MSFT"}
# #
# # stocks_selection = st.sidebar.selectbox("SELECT YOUR STOCKS", list(stocks.keys()),index=3)
# #
# # st.title(f"DA$HBoard for {stocks_selection}")
# # # stocks_selection = st.sidebar.selectbox("SELECT YOUR STOCKS",list(stocks.keys()), index=3)
# # sd = st.sidebar.date_input("Start Date")
# # ed = st.sidebar.date_input("End Date")
# # print("stocks=",stocks_selection)
# # f = stocks[stocks_selection]
# # data = yf.download(f,start=sd,end=ed,auto_adjust=True)
#
# ##################################################################
#
# @st.cache_resource
# def download_data(op, start_date, end_date):
#     df = yf.download(op, start=start_date, end=end_date, progress=False)
#     return df
#
#
# # Sidebar input
# option = st.sidebar.text_input('Enter a Stock Symbol', value='SPY').upper()
# today = datetime.date.today()
# duration = st.sidebar.number_input('Enter the duration (days)', value=3000)
# before = today - datetime.timedelta(days=duration)
# sd = st.sidebar.date_input('Start Date', value=before)
# ed = st.sidebar.date_input('End date', value=today)
#
# with st.sidebar:
#
#     select = option_menu(
#         menu_title=None,
#         options=["Pricing Data","Visuals","StockNews","Stock comparison"]
#
#     )
#
# if select == "Pricing Data":
#     st.subheader("Pricing Data")
#
#     st.write(f"ALL THE DATA IS FROM {sd} to {ed}")
#     data2 = option
#     st.header(f"Raw Pricing Data of {option}")
#
#     data2["%Change in Open"] = option["Open"] / option["Open"].shift(1)
#     data3 = data2
#     data3["%Change in Close"] = option["Close"] / option["Close"].shift(1) - 1
#     st.write(data2.describe())
#     annual_return = data3["%Change in Close"].mean() * 252 * 100
#     st.write("Annual Return : ", annual_return, "%")
#     stdev = np.std(data3["%Change in Close"] * np.sqrt(252))
#     st.write("Risk and Return at close : ", annual_return / (stdev * 100), "%")
#
# if select=="Visuals":
#
#     fig = go.Figure()
#     ma100_open = option['Open'].rolling(window=100).mean()
#     ma200_open = option['Open'].rolling(window=200).mean()
#     # fig.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines', name='Open', line=dict(color='Green')))
#     # fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close', line=dict(color='Red')))
#     # fig.add_trace(go.Scatter(x=data.index, y=ma100.values, mode='lines', name='MA100', line=dict(color='Blue') ))
#     # fig.add_trace(go.Scatter(x=data.index, y=ma200.values, mode='lines', name='MA200', line=dict(color='Yellow')))
#     st.header(option)
#     st.write(f"1. ALL THE DATA IS FROM {sd} to {ed} ")
#     st.write("2. PRICES ARE PLOTED WITH IT'S INDEPENDENT MOVING AVERAGES WHICH RANGES BETWEEN 100-200 DAYS")
#     fig2 = go.Figure()
#     # ma100 = data['Open'].rolling(window=100).mean()
#
#     fig2.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines', name='Open', line=dict(color='Green')))
#     fig2.add_trace(go.Scatter(x=data.index, y=ma100_open.values, mode='lines', name='MA100', line=dict(color='blue')))
#     fig2.add_trace(go.Scatter(x=data.index, y=ma200_open.values, mode='lines', name='MA200', line=dict(color='white')))
#     fig2.update_layout(xaxis_rangeslider_visible=True)
#     st.subheader("OPENED PRICE CHART")
#
#     st.plotly_chart(fig2)
#
#     ma100_close = option['Close'].rolling(window=100).mean()
#     ma200_close = option['Close'].rolling(window=200).mean()
#     fig3 = go.Figure()
#     fig3.add_trace(go.Scatter(x=option.index, y=option['Close'], mode='lines', name='Close', line=dict(color='Red')))
#     fig3.add_trace(go.Scatter(x=option.index, y=ma100_close.values, mode='lines', name='MA100', line=dict(color='blue')))
#     fig3.add_trace(go.Scatter(x=option.index, y=ma200_close.values, mode='lines', name='MA200', line=dict(color='white')))
#     fig3.update_layout(xaxis_rangeslider_visible=True)
#     st.subheader("CLOSED PRICE CHART")
#     st.plotly_chart(fig3)
#
#     fig.add_trace(go.Scatter(x=option.index, y=option['Open'], mode='lines', name='Open', line=dict(color='Green')))
#     fig.add_trace(go.Scatter(x=option.index, y=option['Close'], mode='lines', name='Close', line=dict(color='Red')))
#     fig.add_trace(go.Scatter(x=option.index, y=ma100_close.values, mode='lines', name='MA100', line=dict(color='Blue')))
#     fig.add_trace(go.Scatter(x=option.index, y=ma200_close.values, mode='lines', name='MA200', line=dict(color='white')))
#     fig.add_trace(go.Scatter(x=option.index, y=ma100_open.values, mode='lines', name='MA100', line=dict(color='Blue')))
#     fig.add_trace(go.Scatter(x=option.index, y=ma200_open.values, mode='lines', name='MA200', line=dict(color='white')))
#     fig.update_layout(xaxis_rangeslider_visible=True)
#     st.subheader("UNIVERSAL CHART")
#     st.plotly_chart(fig)
#
#
# if select=="StockNews":
#     st.header(f"Top 10 Headlines of {option}")
#     sn = StockNews(option, save_news=False)
#     df_news = sn.read_rss()
#     print(f"hi={df_news}")
#     for i in range(10):
#         st.subheader(f"{i + 1}. {df_news['title'][i]}")  # Fixed the unterminated expression in f-string
#         st.write(df_news["published"][i])
#
#         st.write(df_news["summary"][i])
#         title_sentimental = df_news["sentiment_title"][i]
#         st.write(f"title sentiment {title_sentimental}")
#         news_sentiment = df_news["sentiment_summary"][i]
#         st.write(f"summary sentimanetal {news_sentiment}")
#
#
# if select == "Stock comparison":
#     st.title("Stock Comparison")
#     # stocks = {"DOW JONES":"^DJI","NASDAQ":"^IXIC","GOLD":"GC=F","BITCOIN":"BTC-USD","AMAZON":"AMZN","APPLE":"APPL","TESLA":"TSLA","GOOGLE":"GOOG","META":"META","MICROSOFT":"MSFT"}
#     #
#     #
#     # selected_stocks = st.multiselect("SELECT YOUR STOCKS", list(stocks.keys()))
#     #
#     # p = [stocks[stock] for stock in selected_stocks]
#     # ticker_to_stock = {v: k for k, v in stocks.items()}
#     # selected_stocks_names = [ticker_to_stock[ticker] for ticker in p]
#     #
#     #
#     # start = st.date_input('Start')
#     #
#     # end = st.date_input('End')
#     #
#     #
#     #
#     #
#     # def relativeret(newData):
#     #     rel = newData.pct_change()
#     #     cumret = (1+rel).cumprod()-1
#     #     cumret = cumret.fillna(0)
#     #     return cumret
#     #
#     # if  (len(p)>0):
#     #     newData = relativeret(yf.download(p,start,end,auto_adjust=True)['Close'])
#     #     st.subheader(f"{selected_stocks_names}")
#     #     st.line_chart(newData)
#
#     # st.title("Stock Comparison")
#
#     stocks = {
#         "DOW JONES": "^DJI",
#         "NASDAQ": "^IXIC",
#         "GOLD": "GC=F",
#         "BITCOIN": "BTC-USD",
#         "AMAZON": "AMZN",
#         "APPLE": "AAPL",
#         "TESLA": "TSLA",
#         "GOOGLE": "GOOG",
#         "META": "META",
#         "MICROSOFT": "MSFT"
#     }
#
#     selected_stocks = st.multiselect("SELECT YOUR STOCKS", list(stocks.keys()))
#
#     ticker_symbols = [stocks[stock] for stock in selected_stocks]
#     ticker_to_stock = {v: k for k, v in stocks.items()}
#     selected_stocks_names = [ticker_to_stock[ticker] for ticker in ticker_symbols]
#
#     start = st.date_input('Start')
#     end = st.date_input('End')
#
#
#     def relativeret(newData):
#         rel = newData.pct_change()
#         cumret = (1 + rel).cumprod() - 1
#         cumret = cumret.fillna(0)
#         return cumret
#
#
#     if len(selected_stocks) > 0:
#         data = yf.download(ticker_symbols, start=start, end=end, auto_adjust=True)['Close']
#         newData = relativeret(data)
#
#         fig = go.Figure()
#         for stock_name, values in newData.items():
#             fig.add_trace(go.Scatter(x=values.index, y=values.values, mode='lines', name=stock_name))
#
#         fig.update_layout(
#             title="Stock Prices Over Time",
#             xaxis_title="Date",
#             yaxis_title="Cumulative Return",
#             legend_title="Stocks",
#             hovermode="x"
#         )
#
#         st.subheader("Stocks Comparison")
#         st.plotly_chart(fig)
#


import streamlit as st
from streamlit_option_menu import option_menu
from ta.volatility import BollingerBands
from ta.trend import MACD, EMAIndicator, SMAIndicator
from ta.momentum import RSIIndicator
import datetime
from datetime import date
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import numpy as np
import yfinance as yf
from keras.models import load_model
from plotly import graph_objects as go
from stocknews import StockNews
import matplotlib.pyplot as plt
import pandas as pd

# Check if user is logged in
if not st.session_state.get('logged_in'):
    st.session_state['login_message'] = "Please get login first 😊"
    st.switch_page("00_🔒_Login.py")
import sys
sys.path.append("..")
from login import login
login()



@st.cache_resource
def download_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    return df


# Sidebar input
option = st.sidebar.text_input('Enter a Stock Symbol', value='SPY').upper()
today = datetime.date.today()
duration = st.sidebar.number_input('Enter the duration (days)', value=3000)
before = today - datetime.timedelta(days=duration)
sd = st.sidebar.date_input('Start Date', value=before)
ed = st.sidebar.date_input('End date', value=today)

with st.sidebar:
    select = option_menu(
        menu_title=None,
        options=["Pricing Data", "Visuals", "Stock comparison"]
    )

data = download_data(option, sd, ed)

if select == "Pricing Data":
    st.subheader("Pricing Data")
    st.write(f"ALL THE DATA IS FROM {sd} to {ed}")
    st.header(f"Raw Pricing Data of {option}")

    data["%Change in Open"] = data["Open"] / data["Open"].shift(1)
    data["%Change in Close"] = data["Close"] / data["Close"].shift(1) - 1
    st.write(data.describe())

    annual_return = data["%Change in Close"].mean() * 252 * 100
    st.write("Annual Return: ", annual_return, "%")
    stdev = np.std(data["%Change in Close"] * np.sqrt(252))
    st.write("Risk and Return at close: ", annual_return / (stdev * 100), "%")

if select == "Visuals":
    fig = go.Figure()
    ma100_open = data['Open'].rolling(window=100).mean()
    ma200_open = data['Open'].rolling(window=200).mean()

    st.header(option)
    st.write(f"1. ALL THE DATA IS FROM {sd} to {ed} ")
    st.write("2. PRICES ARE PLOTTED WITH THEIR INDEPENDENT MOVING AVERAGES WHICH RANGES BETWEEN 100-200 DAYS")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines', name='Open', line=dict(color='Green')))
    fig2.add_trace(go.Scatter(x=data.index, y=ma100_open.values, mode='lines', name='MA100', line=dict(color='blue')))
    fig2.add_trace(go.Scatter(x=data.index, y=ma200_open.values, mode='lines', name='MA200', line=dict(color='white')))
    fig2.update_layout(xaxis_rangeslider_visible=True)
    st.subheader("OPENED PRICE CHART")
    st.plotly_chart(fig2)

    ma100_close = data['Close'].rolling(window=100).mean()
    ma200_close = data['Close'].rolling(window=200).mean()
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close', line=dict(color='Red')))
    fig3.add_trace(go.Scatter(x=data.index, y=ma100_close.values, mode='lines', name='MA100', line=dict(color='blue')))
    fig3.add_trace(go.Scatter(x=data.index, y=ma200_close.values, mode='lines', name='MA200', line=dict(color='white')))
    fig3.update_layout(xaxis_rangeslider_visible=True)
    st.subheader("CLOSED PRICE CHART")
    st.plotly_chart(fig3)

    fig.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines', name='Open', line=dict(color='Green')))
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close', line=dict(color='Red')))
    fig.add_trace(go.Scatter(x=data.index, y=ma100_close.values, mode='lines', name='MA100', line=dict(color='Blue')))
    fig.add_trace(go.Scatter(x=data.index, y=ma200_close.values, mode='lines', name='MA200', line=dict(color='white')))
    fig.add_trace(go.Scatter(x=data.index, y=ma100_open.values, mode='lines', name='MA100', line=dict(color='Blue')))
    fig.add_trace(go.Scatter(x=data.index, y=ma200_open.values, mode='lines', name='MA200', line=dict(color='white')))
    fig.update_layout(xaxis_rangeslider_visible=True)
    st.subheader("UNIVERSAL CHART")
    st.plotly_chart(fig)




if select == "Stock comparison":
    st.title("Stock Comparison")

    stocks = {
        "DOW JONES": "^DJI",
        "NASDAQ": "^IXIC",
        "GOLD": "GC=F",
        "BITCOIN": "BTC-USD",
        "AMAZON": "AMZN",
        "APPLE": "AAPL",
        "TESLA": "TSLA",
        "GOOGLE": "GOOG",
        "META": "META",
        "MICROSOFT": "MSFT"
    }

    selected_stocks = st.multiselect("SELECT YOUR STOCKS", list(stocks.keys()))
    ticker_symbols = [stocks[stock] for stock in selected_stocks]
    ticker_to_stock = {v: k for k, v in stocks.items()}
    selected_stocks_names = [ticker_to_stock[ticker] for ticker in ticker_symbols]

    start = st.date_input('Start')
    end = st.date_input('End')


    def relativeret(newData):
        rel = newData.pct_change()
        cumret = (1 + rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret


    if len(ticker_symbols) > 0:
        data = yf.download(ticker_symbols, start=start, end=end, auto_adjust=True)['Close']
        newData = relativeret(data)

        fig = go.Figure()
        for stock_name, values in newData.items():
            fig.add_trace(go.Scatter(x=values.index, y=values.values, mode='lines', name=stock_name))

        fig.update_layout(
            title="Stock Prices Over Time",
            xaxis_title="Date",
            yaxis_title="Cumulative Return",
            legend_title="Stocks",
            hovermode="x"
        )

        st.subheader("Stocks Comparison")
        st.plotly_chart(fig)
