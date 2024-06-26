import streamlit as st
from ta.volatility import BollingerBands
from ta.trend import MACD, EMAIndicator, SMAIndicator
from ta.momentum import RSIIndicator
import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import yfinance as yf
import pandas as pd
if not st.session_state.get('logged_in'):
    st.session_state['login_message'] = "Please get login first 😊"
    st.switch_page("00_🔒_Login.py")
# from helper import fetch_stocks


# Define the main function

def main():

    option = st.sidebar.selectbox('Make a choice', ['Visualize', 'Recent Data', 'Predict'])
    if option == 'Visualize':
        tech_indicators()
    elif option == 'Recent Data':
        dataframe()
    else:
        predict()


@st.cache_resource
def download_data(op, start_date, end_date):
    df = yf.download(op, start=start_date, end=end_date, progress=False)
    return df


# Sidebar input
option = st.sidebar.text_input('Enter a Stock Symbol', value='SPY').upper()
today = datetime.date.today()
duration = st.sidebar.number_input('Enter the duration (days)', value=3000)
before = today - datetime.timedelta(days=duration)
start_date = st.sidebar.date_input('Start Date', value=before)
end_date = st.sidebar.date_input('End date', value=today)

if st.sidebar.button('Send'):
    if start_date < end_date:
        st.sidebar.success(f'Start date: {start_date}\n\nEnd date: {end_date}')
    else:
        st.sidebar.error('Error: End date must fall after start date')

data = download_data(option, start_date, end_date)
scaler = StandardScaler()


def tech_indicators():
    st.header('Technical Indicators')
    indicator_option = st.radio('Choose a Technical Indicator to Visualize',
                                ['Close', 'BB', 'MACD', 'RSI', 'SMA', 'EMA'])

    # Bollinger bands
    bb_indicator = BollingerBands(data['Close'])
    data['bb_h'] = bb_indicator.bollinger_hband()
    data['bb_l'] = bb_indicator.bollinger_lband()
    # MACD
    data['MACD'] = MACD(data['Close']).macd()
    # RSI
    data['RSI'] = RSIIndicator(data['Close']).rsi()
    # SMA
    data['SMA'] = SMAIndicator(data['Close'], window=14).sma_indicator()
    # EMA
    data['EMA'] = EMAIndicator(data['Close']).ema_indicator()

    if indicator_option == 'Close':
        st.write('Close Price')
        st.line_chart(data['Close'])
    elif indicator_option == 'BB':
        st.write('Bollinger Bands')
        st.line_chart(data[['Close', 'bb_h', 'bb_l']])
    elif indicator_option == 'MACD':
        st.write('Moving Average Convergence Divergence')
        st.line_chart(data['MACD'])
    elif indicator_option == 'RSI':
        st.write('Relative Strength Indicator')
        st.line_chart(data['RSI'])
    elif indicator_option == 'SMA':
        st.write('Simple Moving Average')
        st.line_chart(data['SMA'])
    else:
        st.write('Exponential Moving Average')
        st.line_chart(data['EMA'])


def dataframe():
    st.header('Recent Data')
    st.dataframe(data.tail(10))


def predict():
    model_option = st.radio('Choose a model',
                            ['LinearRegression', 'RandomForestRegressor', 'ExtraTreesRegressor', 'KNeighborsRegressor',
                             'XGBRegressor'])
    num_days = st.number_input('How many days forecast?', value=5, min_value=1)

    if st.button('Predict'):
        model_dict = {
            'LinearRegression': LinearRegression(),
            'RandomForestRegressor': RandomForestRegressor(),
            'ExtraTreesRegressor': ExtraTreesRegressor(),
            'KNeighborsRegressor': KNeighborsRegressor(),
            'XGBRegressor': XGBRegressor()
        }

        model = model_dict[model_option]
        model_engine(model, num_days)


def model_engine(model, num):
    df = data[['Close']]
    df['preds'] = data['Close'].shift(-num)
    x = df.drop(['preds'], axis=1).values
    x = scaler.fit_transform(x)
    x_forecast = x[-num:]
    x = x[:-num]
    y = df['preds'].values[:-num]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)
    model.fit(x_train, y_train)
    preds = model.predict(x_test)

    st.text(f'r2_score: {r2_score(y_test, preds):.2f}\nMAE: {mean_absolute_error(y_test, preds):.2f}')

    forecast_pred = model.predict(x_forecast)
    for day, prediction in enumerate(forecast_pred, 1):
        st.text(f'Day {day}: {prediction:.2f}')


if __name__ == '__main__':
    main()
