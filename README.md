# Crypto-Stock-Correlation-Monitor-Project

📈 Crypto–Stock Correlation Monitor

A Python + Streamlit based web application that analyzes and visualizes the correlation between cryptocurrencies and stock market assets.
The dashboard allows users to explore price movements, correlation heatmaps, and rolling correlations using real market data.

🚀 Features

📊 Interactive price visualization for Crypto & Stocks

🔥 Correlation heatmap between selected assets

🔁 Rolling correlation analysis

⏱ Configurable time period and interval

🌐 Web-based dashboard using Streamlit

📉 Real-time market data via Yahoo Finance

🛠 Technologies Used

Python 3.9+

Streamlit – Web UI

yfinance – Market data fetching

Pandas & NumPy – Data processing

Plotly – Interactive charts

📁 Project Structure
Crypto–Stock Correlation Monitor/
│── App.py
│── requirements.txt
│── README.md
│── .venv/

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/crypto-stock-correlation-monitor.git
cd Crypto–Stock-Correlation-Monitor

2️⃣ Create & Activate Virtual Environment (Recommended)
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux


For Windows:

.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application

⚠️ Important: Streamlit apps must be run using streamlit run.

streamlit run App.py


The app will open automatically in your browser at:

http://localhost:8501

📊 How It Works

User selects cryptocurrencies and stocks

Market data is fetched using Yahoo Finance

Closing prices are extracted and aligned

Correlation matrix is computed

Results are visualized using Plotly heatmaps and line charts

📌 Example Assets Supported
Cryptocurrencies

BTC-USD

ETH-USD

BNB-USD

SOL-USD

Stocks / Indices

AAPL

TSLA

MSFT

GOOGL

NIFTY (^NSEI)

BANK NIFTY (^NSEBANK)

⚠️ Common Issues & Fixes
❌ missing ScriptRunContext warning

Cause: Running with python App.py

✅ Fix:

streamlit run App.py

❌ Module not found error

Cause: Packages not installed in virtual environment

✅ Fix:

pip install -r requirements.txt

🎯 Use Cases

Market research & analysis

Portfolio diversification study

Crypto vs equity correlation tracking

Academic projects & demonstrations

Financial data visualization

🔮 Future Enhancements

Real-time data via WebSockets

Correlation alerts (Email / SMS)

Sentiment analysis (Twitter & News)

Export data to CSV / Excel

Cloud deployment (AWS / Render)


Project: Crypto–Stock Correlation Monitor

📜 License

This project is intended for educational and research purposes.
