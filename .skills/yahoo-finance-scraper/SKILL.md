---
name: yahoo-finance-scraper
description: Scrape real-time and historical financial data from Yahoo Finance. Use when users ask to fetch stock prices, historical price data, company financials, market summaries, stock quotes, financial ratios, or any Yahoo Finance data. Triggers on phrases like "get stock price", "fetch financial data", "Yahoo Finance", "stock quote", "historical prices", "company financials".
---

# Yahoo Finance Scraper

Scrape real-time and historical financial data from Yahoo Finance using the yfinance Python library.

## Capabilities

- **Stock Quotes**: Real-time current price, open, high, low, volume
- **Historical Data**: Daily, weekly, monthly price history with configurable date ranges
- **Company Info**: Business summary, sector, industry, executive team
- **Financial Statements**: Income statement, balance sheet, cash flow
- **Key Statistics**: P/E ratio, EPS, dividend yield, market cap, beta
- **Options Data**: Options chains and expiration dates
- **Analyst Recommendations**: Price targets and ratings history
- **Sustainability**: ESG scores and sustainability metrics

## Supported Tickers

- US stocks: AAPL, GOOGL, MSFT, TSLA, etc.
- Indices: ^GSPC (S&P 500), ^DJI (Dow Jones), ^IXIC (NASDAQ)
- ETFs: SPY, QQQ, IWM, etc.
- Crypto: BTC-USD, ETH-USD, etc.
- Forex: USDJPY=X, EURUSD=X

## Workflow

1. **Identify ticker symbol**
   - Parse stock symbol from user request
   - Validate format (typically 1-5 uppercase letters, optionally with -USD suffix)
   - Handle special cases (indices with ^ prefix)

2. **Determine data type needed**
   - Quote only → fast single API call
   - Historical → date range + interval
   - Full analysis → multiple data types

3. **Execute scraping**
   - Use yfinance library for reliable data retrieval
   - Handle rate limiting gracefully
   - Cache recent results when appropriate

4. **Format output**
   - Return structured JSON for programmatic use
   - Format numbers with appropriate precision
   - Include metadata (timestamp, currency, exchange)

## Data Types

| Type | Method | Returns |
|------|--------|---------|
| Quote | `ticker.info` | Current price, change, volume |
| History | `ticker.history()` | OHLCV data by period/date |
| Financials | `ticker.financials` | Income statement |
| Balance Sheet | `ticker.balance_sheet` | Assets, liabilities |
| Cash Flow | `ticker.cashflow` | Operating, investing, financing |
| Dividends | `ticker.dividends` | Historical dividend payments |
| Splits | `ticker.splits` | Stock split history |
| Options | `ticker.option_chain()` | Available options contracts |
| Recommendations | `ticker.recommendations` | Analyst ratings |

## Common Parameters

| Parameter | Values | Default |
|-----------|--------|---------|
| period | 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max | 1mo |
| interval | 1m, 2m, 5m, 15m, 30m, 60m, 1h, 1d, 1wk, 1mo | 1d |
| start | YYYY-MM-DD | period start |
| end | YYYY-MM-DD | today |

## Usage Examples

### Get Current Quote
```python
import yfinance as yf
ticker = yf.Ticker("AAPL")
info = ticker.info
print(f"AAPL: ${info['currentPrice']}")
```

### Historical Data
```python
data = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
```

### Financial Statements
```python
ticker = yf.Ticker("MSFT")
income = ticker.income_stmt
balance = ticker.balance_sheet
```

### Multiple Tickers
```python
data = yf.download("AAPL GOOGL MSFT", period="1d")
```

## Error Handling

- **Invalid ticker**: Return error with suggestion to verify symbol
- **Network failure**: Retry with exponential backoff, max 3 attempts
- **No data**: Return empty result with explanation
- **Rate limited**: Wait and retry, inform user of delay
