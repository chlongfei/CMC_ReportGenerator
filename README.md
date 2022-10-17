# CoinMarketCap.com Report Generator

Generates reports from coinmarketcap.com via CMC API and spits into .xslx

## Currenty supported reports:
- Listings Latest (top 200 market cap)


# Dependencies
- requests
- io
- PILL (pillow)
- dotenv (python-dotenv)
- os
- json
- xlsxwriter

# Installation
1. Ensure all dependencies listed above are installed
2. Obtain Free API key from https://coinmarketcap.com/api/
3. Enter API key into `.env`
4. Ready to run by running `python main.py`

---
**Disclaimer:**

This project is in no way affiliated with Coin Market Cap or its affilliates. 

This is purely just a data gathering tool so I don't need to copy/paste from the site 100+ times.

CMC_ReportGenerator comes as-is warranty free. If you break it, fix it.