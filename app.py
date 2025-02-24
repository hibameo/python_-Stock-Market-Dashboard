import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# App Title
st.title("📈 Stock Market Dashboard")

# User input for stock ticker
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, GOOGL)", "AAPL").upper()

# Fetch stock data
if st.button("Get Stock Data"):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="6mo")  # Last 6 months data
        
        if data.empty:
            st.error("Invalid ticker or no data available!")
        else:
            st.subheader(f"Stock Data for {ticker}")

            # Show stock price data
            st.write(data.tail(10))

            # Plot closing price chart
            fig = px.line(data, x=data.index, y="Close", title=f"{ticker} Stock Price Trend")
            st.plotly_chart(fig)

            # Show additional info
            st.subheader("Stock Info")
            st.write(f"**Current Price:** ${stock.info['lastPrice'] if 'lastPrice' in stock.info else 'N/A'}")
            st.write(f"**52-Week High:** ${stock.info['fiftyTwoWeekHigh'] if 'fiftyTwoWeekHigh' in stock.info else 'N/A'}")
            st.write(f"**52-Week Low:** ${stock.info['fiftyTwoWeekLow'] if 'fiftyTwoWeekLow' in stock.info else 'N/A'}")

    except Exception as e:
        st.error("Error fetching stock data! Please try again.")

