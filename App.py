import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

# Page Configuration

st.set_page_config(
    page_title="Crypto–Stock Correlation Monitor",
    layout="wide"
)

# Sidebar Configuration

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

period = st.sidebar.selectbox(
    "Data Period",
    ["1mo", "3mo", "6mo", "1y"],
    index=1
)

interval = st.sidebar.selectbox(
    "Interval",
    ["1h", "4h", "1d"],
    index=2
)

# Title

st.title("📈 Crypto–Stock Correlation Monitor")


# Download Market Data

symbols = crypto + stocks

@st.cache_data(show_spinner=False)
def load_data(symbols, period, interval):
    data = yf.download(
        symbols,
        period=period,
        interval=interval,
        auto_adjust=False
    )["Close"]
    return data

data = load_data(symbols, period, interval)

# Display Price Data

st.subheader("📊 Price Data (Closing Prices)")
st.dataframe(data.tail())


# Correlation Heatmap
corr = data.corr()

st.subheader(" Correlation Heatmap")

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu",
    title="Correlation Matrix"
)

st.plotly_chart(fig, use_container_width=True)


# Rolling Correlation (Corrected & Robust)

if len(crypto) > 0 and len(stocks) > 0:

    c1 = crypto[0]
    s1 = stocks[0]

    st.subheader(f"🔁 Rolling Correlation: {c1} vs {s1}")

    # Align crypto & stock data
    pair_data = data[[c1, s1]].dropna()

    # Adaptive rolling window
    window = min(30, len(pair_data) // 2)

    if window >= 5:
        rolling_corr = pair_data[c1].rolling(window).corr(pair_data[s1])

        fig2 = px.line(
            rolling_corr,
            title=f"Rolling Correlation ({window}-period window)",
            labels={"value": "Correlation", "index": "Date"}
        )

        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning(
            " Not enough overlapping data points to compute rolling correlation."
        )
