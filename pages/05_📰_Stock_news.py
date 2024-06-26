import streamlit as st
from stocknews import StockNews
import yfinance as yf
import datetime

if not st.session_state.get('logged_in'):
    st.session_state['login_message'] = "Please get login first 😊"
    st.switch_page("00_🔒_Login.py")
st.header("Top 10 Headlines")

# Initialize StockNews object with a list of stock symbols
@st.cache_resource
def download_data(op, start_date, end_date):
    df = yf.download(op, start=start_date, end=end_date, progress=False)
    return df


# Sidebar input
option = st.sidebar.text_input('Enter a Stock Symbol', value='SPY').upper()
today = datetime.date.today()
# duration = st.sidebar.number_input('Enter the duration (days)', value=3000)
# before = today - datetime.timedelta(days=duration)
# start_date = st.sidebar.date_input('Start Date', value=before)
# end_date = st.sidebar.date_input('End date', value=today)
st.header(f"Top 10 Headlines of {option}")
sn = StockNews(option, save_news=False)
df_news = sn.read_rss()

for i in range(10):
    st.subheader(f"{i + 1}. {df_news['title'][i]}")
    st.write(df_news["published"][i])
    st.write(df_news["summary"][i])
    title_sentimental = df_news["sentiment_title"][i]
    st.write(f"Title sentiment: {title_sentimental}")
    news_sentiment = df_news["sentiment_summary"][i]
    st.write(f"Summary sentiment: {news_sentiment}")