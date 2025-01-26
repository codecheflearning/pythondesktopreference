import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft.history(period="1mo"))

tickers = yf.Tickers('amzn att k')
tickers.tickers['ATT'].info
tickers.tickers['AMZN'].info
tickers.tickers['K'].actions

data = yf.download("goog", period="1mo")
print(data)