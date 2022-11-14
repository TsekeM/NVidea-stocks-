import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('NVidia_stock_history.csv')

# Delete rows where the date is before 1/1/2019

df['Date'] = pd.to_datetime(df['Date'])
df = df[~(df['Date'] < '2019-01-01')]
df.head()

# Reset the index to the Date column.
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
df.reset_index(drop=True, inplace=True)
df.set_index('Date', inplace=True)

# Specify the title and logo for the web page.
st.set_page_config(page_title='Nvidia Stock Prices',
                   page_icon='https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', layout="wide")

# Add social media tags and links to the web page.
"""
[![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tseke-maila-29057715a/)

# Nvidia's Stock Performance

"""

# Add a sidebar to the web page.
st.markdown('---')
# Sidebar Configuration
st.sidebar.image(
    'https://cdn.freebiesupply.com/logos/thumbs/1x/nvidia-logo.png', width=200)
st.sidebar.markdown('# Nvidia Stock Price Analysis')
st.sidebar.markdown(
    'Nvidia is a global leader in artificial intelligence hardware and software.')
st.sidebar.markdown('Stock Data from 2019 thru 2021')
st.sidebar.markdown(
    'You can visualise Nvidia \'s Stock Prices Trends and Patterns over a given time span.')

st.sidebar.markdown('---')
st.sidebar.write('Developed by Tseke Maila')
st.sidebar.write('Contact at tseke@muluma.co.za')

# Display some data in the app view
st.subheader('Looking at the data')
st.dataframe(df.describe())

# Selection for specific time frame
st.subheader('Select range')
df_select = df

col1, col2 = st.columns(2)

with col1:
    st.write('Select a Start Date')
    start_date = st.date_input('Start on', min_value=datetime.date(
        2019, 1, 2), max_value=datetime.date(2021, 11, 12), value=datetime.date(2019, 1, 2))

with col2:
    st.write('Select an End Date')
    end_date = st.date_input('End on', min_value=datetime.date(
        1999, 1, 22), max_value=datetime.date(2021, 11, 12), value=datetime.date(2021, 11, 12))

if (start_date != None or end_date != None):
    if (start_date < end_date):
        df_select = df[start_date:end_date]
    else:
        st.warning("Invalid Date Range - Re-enter Dates")

# Open and Close Prices.
st.subheader("Open & Close Prices for Nvidia Stock")
st.markdown("\n\n")
st.line_chart(df_select[['Open', 'Close']])

# High and Low Prices.
st.subheader("High and Low Prices for Nvidia Stock")
st.markdown("\n\n")
st.line_chart(df_select[['High', 'Low']])

# Volume of Stock Traded.
st.subheader("Volumn Traded for Nvidia Stock")
st.markdown("\n\n")
st.bar_chart(df_select['Volume'])

# Moving average from 50 days to 250 days.
st.subheader('Moving Averages of Open and Closing Stock Prices')
movevavg_len = st.slider(
    'Select the number of days for Moving Averages', min_value=0, max_value=250, value=50)
moveavg_oc = df_select[['Open', 'Close']].rolling(50).mean()
st.line_chart(moveavg_oc)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
