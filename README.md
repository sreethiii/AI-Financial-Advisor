# 💼 AI Financial Advisor

A personalized financial insights generator that analyzes real-time stock data and generates beginner-friendly investment advice using Google's Gemini Pro and Streamlit.

## 🔧 Tech Stack

- Streamlit
- Gemini API (via Google Generative AI)
- Yahoo Finance API (via yfinance)
- Plotly
- Python

## 🚀 Features

- 📈 Real-time stock summary and chart
- 🧠 AI-generated financial advice based on risk profile
- 📊 Year-over-year stock analysis

## ✅ Setup

```bash
git clone https://github.com/your-username/ai-financial-advisor.git
cd ai-financial-advisor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Create a .env file and add:
```bash
GOOGLE_API_KEY=your_google_api_key
```

## Run the app:
```bash
streamlit run main.py
```
