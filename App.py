import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Crypto-Stock Correlation Monitor", layout="wide")

# --- Sidebar Inputs ---
st.sidebar.header("Configuration")

crypto = st.sidebar.multiselect(
    "Select Crypto Symbols",
    ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD"],
    default=["BTC-USD", "ETH-USD"]
)

stocks = st.sidebar.multiselect(
    "Select Stock Symbols",
    ["AAPL", "MSFT", "TSLA", "GOOGL", "^NSEI", "^NSEBANK"],
    default=["AAPL", "TSLA"]
)

period = st.sidebar.selectbox("Data Period", ["1mo", "3mo", "6mo", "1y"], index=1)
interval = st.sidebar.selectbox("Interval", ["1h", "4h", "1d"], index=2)

st.title("📈 Crypto–Stock Correlation Monitor")

# --- Download Data ---
symbols = crypto + stocks
data = yf.download(symbols, period=period, interval=interval)["Close"]

st.subheader("Price Data (Closing Values)")
st.dataframe(data.tail())

# --- Compute Correlation ---
corr = data.corr()

st.subheader("Correlation Heatmap")
fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu",
    title="Correlation Matrix"
)
st.plotly_chart(fig, use_container_width=True)

# --- Rolling Correlation Example ---
if len(crypto) > 0 and len(stocks) > 0:
    c1 = crypto[0]
    s1 = stocks[0]

    st.subheader(f"Rolling Correlation: {c1} vs {s1} (30-period)")

    rolling_corr = data[c1].rolling(30).corr(data[s1])

    fig2 = px.line(
        rolling_corr,
        title=f"Rolling Correlation: {c1} vs {s1}",
        labels={"value": "Correlation"}
    )
    st.plotly_chart(fig2, use_container_width=True)

