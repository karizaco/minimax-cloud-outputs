# Yahoo Finance Scraper API Reference

Complete reference for the Yahoo Finance Scraper script.

## Installation

```bash
pip install yfinance pandas
```

## Command Line Usage

```bash
python scrape_yfinance.py <TICKER> [options]
```

### Basic Examples

```bash
# Get current quote for Apple
python scrape_yfinance.py AAPL

# Get 1 year of daily historical data
python scrape_yfinance.py AAPL --type history --period 1y

# Get specific date range
python scrape_yfinance.py AAPL --type history --start 2024-01-01 --end 2024-12-31

# Get financial statements
python scrape_yfinance.py AAPL --type financials

# Get key statistics
python scrape_yfinance.py AAPL --type stats

# Save output to file
python scrape_yfinance.py AAPL --output aapl_data.json --pretty
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `ticker` | Stock ticker symbol | Required |
| `--type` | Data type to fetch | `quote` |
| `--period` | Time period for historical data | `1mo` |
| `--interval` | Data interval | `1d` |
| `--start` | Start date (YYYY-MM-DD) | - |
| `--end` | End date (YYYY-MM-DD) | - |
| `--output` | Output file path | - |
| `--pretty` | Pretty print JSON | False |

## Data Types

### Quote (`--type quote`)

Returns real-time quote data including:

- Current price
- Previous close
- Open, high, low
- Volume
- Market cap
- Daily change

### Historical (`--type history`)

Returns OHLCV (Open, High, Low, Close, Volume) data.

**Periods**: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`

**Intervals**: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `1h`, `1d`, `1wk`, `1mo`

### Financials (`--type financials`)

Returns financial statements:

- Income statement
- Balance sheet
- Cash flow statement

### Statistics (`--type stats`)

Returns key metrics:

- Valuation (P/E, P/B, market cap)
- Profitability margins
- Growth rates
- Dividend information
- Analyst targets

### Company Info (`--type info`)

Returns company details:

- Business summary
- Sector and industry
- Location
- Executive information

### Dividends (`--type dividends`)

Returns dividend history with dates and amounts.

### Options (`--type options`)

Returns options chain with calls and puts data.

## Python API Usage

```python
from scrape_yfinance import (
    get_quote,
    get_historical,
    get_financials,
    get_key_stats,
    get_company_info,
    get_dividends,
    get_options,
)

# Get quote
quote = get_quote("AAPL")
print(f"AAPL: ${quote['currentPrice']}")

# Get historical data
data = get_historical("AAPL", period="1y")
print(f"Got {data['recordCount']} records")

# Get financial statements
financials = get_financials("AAPL")
print(financials.keys())

# Get key statistics
stats = get_key_stats("AAPL")
print(f"P/E Ratio: {stats['metrics'].get('trailingPE')}")
```

## Output Format

All functions return JSON-serializable dictionaries:

```python
{
    "symbol": "AAPL",
    "timestamp": "2024-01-15T10:30:00",
    # ... type-specific fields
}
```

## Error Handling

```python
try:
    quote = get_quote("INVALID_TICKER")
    if "error" in quote:
        print(f"Error: {quote['error']}")
except Exception as e:
    print(f"Failed to fetch: {e}")
```

## Rate Limiting

The script handles rate limiting gracefully:

- Automatic retries with exponential backoff
- Max 3 retry attempts
- Clear error messages for persistent failures

## Common Ticker Formats

| Type | Example | Format |
|------|---------|--------|
| US Stock | Apple | `AAPL` |
| Index | S&P 500 | `^GSPC` |
| ETF | S&P 500 ETF | `SPY` |
| Crypto | Bitcoin | `BTC-USD` |
| Forex | EUR/USD | `EURUSD=X` |
