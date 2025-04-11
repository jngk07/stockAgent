
import alpaca_trade_api as tradeapi

def execute_trade(symbol, action, qty, api_key, secret_key):
    api = tradeapi.REST(api_key, secret_key, base_url="https://paper-api.alpaca.markets")
    
    if action == "BUY":
        api.submit_order(symbol=symbol, qty=qty, side='buy', type='market', time_in_force='gtc')
        print(f"✅ Bought {qty} shares of {symbol}")
    elif action == "SELL":
        api.submit_order(symbol=symbol, qty=qty, side='sell', type='market', time_in_force='gtc')
        print(f"✅ Sold {qty} shares of {symbol}")
    else:
        print("⏸️ No action taken")

# Test
if __name__ == "__main__":
    execute_trade("TSLA", "BUY", 1, api_key="YOUR_KEY", secret_key="YOUR_SECRET")
