import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

btc = yf.download("BTC-USD", start="2020-01-01", end="2025-12-31", auto_adjust=True)

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(btc.index, btc["Close"], color="orange", linewidth=1.5, label="BTC-USD")
ax.set_title("Bitcoin Price (2020–2025)", fontsize=16)
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
