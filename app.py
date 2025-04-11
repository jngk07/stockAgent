
import streamlit as st
from agent1_news_reader import get_news
from agent2_sentiment_signal import analyze_news
from agent3_trader import execute_trade
from agent4_price_predictor import predict_price
import yfinance as yf

st.title("🧠 AI News-Based Stock Trading Agent")

company = st.text_input("Enter Company Name", "Tesla")
symbol = st.text_input("Enter Stock Symbol", "TSLA")
news_api_key = st.text_input("News API Key", type="password")
alpaca_api_key = st.text_input("Alpaca API Key", type="password")
alpaca_secret_key = st.text_input("Alpaca Secret Key", type="password")
use_test_news = st.checkbox("Use Custom Test News Instead of Live News")
run_price_prediction = st.checkbox("Enable Price Prediction Agent (Agent 4)")

if st.button("Run Trading Agent"):
    if not alpaca_api_key or not alpaca_secret_key:
        st.error("Please enter all API keys.")
    else:
        if use_test_news:
            news = [
                f"{company} stock explodes after incredible earnings blowout! 🚀",
                f"Top analysts overwhelmingly upgrade {company}, calling it a must-buy!",
                f"{company} revolutionizes the market with mind-blowing AI tech. Investors thrilled!"
            ]
        else:
            news = get_news(company, news_api_key)

        st.subheader("🗞️ Latest News Articles")
        for i, article in enumerate(news, 1):
            st.markdown(f"**{i}.** {article}")

        decision, score = analyze_news(news)
        st.subheader("📊 Sentiment Analysis")
        st.write(f"**Sentiment Score:** {score:.2f}")
        st.write(f"**Decision from Sentiment Agent:** `{decision}`")

        predicted = None
        current_price = None

        if run_price_prediction:
            with st.spinner("Predicting future price..."):
                predicted = predict_price(symbol)
                if predicted:
                    st.subheader("🔮 Predicted Next Close Price")
                    st.write(f"${predicted:.2f}")
                    try:
                        current_price = yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]
                        st.subheader("💵 Current Market Price")
                        st.write(f"${current_price:.2f}")

                        delta = predicted - current_price
                        st.subheader("📈 Prediction Delta")
                        st.write(f"Change: ${delta:.2f} ({'Up' if delta > 0 else 'Down'})")

                        # Optional override logic
                        if decision == "BUY" and predicted < current_price:
                            st.warning("Positive sentiment detected, but price prediction is bearish. Holding instead.")
                            decision = "HOLD"
                    except:
                        st.error("Could not fetch current price.")
                else:
                    st.error("Could not predict price.")

        if decision in ["BUY", "SELL"]:
            with st.spinner(f"Executing {decision} order..."):
                execute_trade(symbol, decision, qty=1, api_key=alpaca_api_key, secret_key=alpaca_secret_key)
                st.success(f"{decision} order executed successfully!")
        else:
            st.info("No trade executed. Decision is HOLD.")
