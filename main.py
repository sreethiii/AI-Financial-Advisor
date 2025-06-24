import streamlit as st
import plotly.graph_objs as go
from utils.stock_data import get_stock_summary, get_stock_history, get_year_over_year_change
from agents.advisor_agent import run_advisor_agent
import time

st.set_page_config(page_title="💼 AI Financial Advisor", layout="wide")

st.markdown("""
    <style>
        body { font-family: 'Segoe UI', sans-serif; }
        .big-title { font-size: 3rem; font-weight: bold; background: linear-gradient(90deg, #0072ff, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .stock-box { background-color: #f5f5f5; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 2rem; }
        .insight-box { 
    background: #f0f8ff;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
    font-size: 1.1rem;
    color: #2a2a72;
    font-weight: 500;
    border-left: 6px solid #0072ff;
    box-shadow: 0 2px 8px rgba(0, 114, 255, 0.2); }
        .footer { margin-top: 5rem; text-align: center; color: gray; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>📈 AI Financial Advisor</div>", unsafe_allow_html=True)

tickers_input = st.text_input("🔍 Enter stock tickers (comma-separated):", placeholder="e.g. AAPL, MSFT, TSLA")
risk_profile = st.selectbox("🧬 Select your risk profile:", ["Conservative", "Moderate", "Aggressive"])

tickers = [t.strip().upper() for t in tickers_input.split(',') if t.strip()]

for ticker in tickers:
    with st.container():
        with st.expander(f"📊 {ticker} – Detailed View", expanded=True):
            try:
                summary = get_stock_summary(ticker)
                history = get_stock_history(ticker)

                if not summary or not isinstance(summary, dict) or summary.get("Name", "N/A") == "N/A":
                    raise ValueError("Invalid or missing stock summary.")

                st.markdown(f"<div class='stock-box'>", unsafe_allow_html=True)
                st.subheader("📋 Stock Summary")
                for key, value in summary.items():
                    if value is None or str(value).lower() in ["nan", "none"]:
                        st.markdown(f"**{key}:** N/A")
                    elif isinstance(value, float):
                        st.markdown(f"**{key}:** {value:,.2f}")
                    else:
                        st.markdown(f"**{key}:** {value}")

                if history is not None and not history.empty:
                    st.subheader("📉 Historical Price Chart")
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=history.index, y=history['Close'], name='Close Price'))
                    fig.update_layout(xaxis_title="Date", yaxis_title="Price", template="plotly_dark", height=300)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("No historical data available.")

                yoy_change = get_year_over_year_change(ticker)
                if yoy_change is not None:
                    st.success(f"📅 Year-over-Year change: **{yoy_change}%**")
                else:
                    st.warning("Year-over-year data not available.")

                if st.button(f"💡 Generate AI Insight for {ticker}"):
                    with st.spinner("Thinking like a financial guru..."):
                        time.sleep(1.5)
                        insight = run_advisor_agent(summary, risk_profile)
                        st.markdown(f"<div class='insight-box'>{insight}</div>", unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"🚫 Error fetching data for {ticker}: {e}")

st.markdown("<div class='footer'>🚀 Built with ❤️ using Streamlit, Gemini, and Yahoo Finance</div>", unsafe_allow_html=True)
