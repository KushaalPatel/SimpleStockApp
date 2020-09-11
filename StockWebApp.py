import streamlit as sl
import yfinance as yf
from datetime import date



sl.sidebar.header('User Input')

def get_input():
    start_date = sl.sidebar.text_input("Start Date","2020-01-01") # default start date is jan 1 2020
    today = date.today()
    ed = today.strftime("%Y-%m-%d")
    end_date = sl.sidebar.text_input("End Date",ed) # default end data is current day
    tickerSymbol = sl.sidebar.text_input("Stock Ticker","GOOGL") # default ticker = GOOGL, Alphabet inc
    return start_date, end_date, tickerSymbol.upper()

def get_data(ticker, start, end):
    tickerData = yf.Ticker(ticker)
    tickerDf = tickerData.history(start = start, end = end)
    return tickerDf, tickerData

    
start, end, symbol = get_input()
Df, tData = get_data(symbol, start, end)


sl.write("""# Simple Stock App""") #Always display
try: # valid ticker
    tData.actions.any() #check if ticker is valid
    sl.write("""Shown are the stock closing price and volume of""", tData.info['longName'],"from", start, "to", end,)
    sl.write("""## Closing Price""")
    sl.line_chart(Df.Close)
    sl.write("""## Volume""")
    sl.line_chart(Df.Volume)
except: # not valid ticker
    sl.write("""***Invalid Ticker***""")
    sl.write("""***Please Enter Valid Ticker***""")

