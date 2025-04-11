
from agent1_news_reader import get_news
from agent2_sentiment_signal import analyze_news
from agent3_trader import execute_trade

NEWS_API_KEY = "YOUR_NEWS_API_KEY"
ALPACA_API_KEY = "YOUR_ALPACA_KEY"
ALPACA_SECRET_KEY = "YOUR_ALPACA_SECRET"
COMPANY = "Tesla"
SYMBOL = "TSLA"

news = get_news(COMPANY, NEWS_API_KEY)
decision, score = analyze_news(news)

print(f"[Signal] {decision} (Score: {score:.2f})")

if decision in ["BUY", "SELL"]:
    execute_trade(SYMBOL, decision, qty=1, api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY)
