#!/usr/bin/env python3
"""
Yahoo Finance Scraper Script
Scrape real-time and historical financial data from Yahoo Finance.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

try:
    import yfinance as yf
    import pandas as pd
except ImportError:
    print("Error: Required libraries not installed. Run: pip install yfinance pandas")
    sys.exit(1)


def get_quote(ticker_symbol: str) -> Dict[str, Any]:
    """Get current quote data for a ticker."""
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    return {
        "symbol": ticker_symbol,
        "timestamp": datetime.now().isoformat(),
        "currentPrice": info.get("currentPrice") or info.get("regularMarketPrice"),
        "previousClose": info.get("previousClose"),
        "open": info.get("open"),
        "dayHigh": info.get("dayHigh"),
        "dayLow": info.get("dayLow"),
        "volume": info.get("volume"),
        "marketCap": info.get("marketCap"),
        "currency": info.get("currency", "USD"),
        "exchange": info.get("exchangeName", "Unknown"),
        "name": info.get("shortName") or info.get("longName", ticker_symbol),
        "change": info.get("regularMarketChange"),
        "changePercent": info.get("regularMarketChangePercent"),
    }


def get_historical(
    ticker_symbol: str,
    period: str = "1mo",
    interval: str = "1d",
    start: Optional[str] = None,
    end: Optional[str] = None,
) -> Dict[str, Any]:
    """Get historical price data for a ticker."""
    ticker = yf.Ticker(ticker_symbol)

    if start and end:
        data = ticker.history(start=start, end=end, interval=interval)
    else:
        data = ticker.history(period=period, interval=interval)

    if data.empty:
        return {"symbol": ticker_symbol, "data": [], "message": "No data available"}

    # Convert DataFrame to dict
    records = []
    for index, row in data.iterrows():
        records.append({
            "date": index.isoformat(),
            "open": float(row["Open"]) if pd.notna(row["Open"]) else None,
            "high": float(row["High"]) if pd.notna(row["High"]) else None,
            "low": float(row["Low"]) if pd.notna(row["Low"]) else None,
            "close": float(row["Close"]) if pd.notna(row["Close"]) else None,
            "volume": int(row["Volume"]) if pd.notna(row["Volume"]) else None,
        })

    return {
        "symbol": ticker_symbol,
        "period": period,
        "interval": interval,
        "startDate": str(data.index[0].date()) if len(data) > 0 else None,
        "endDate": str(data.index[-1].date()) if len(data) > 0 else None,
        "recordCount": len(records),
        "data": records,
    }


def get_financials(ticker_symbol: str) -> Dict[str, Any]:
    """Get financial statements for a ticker."""
    ticker = yf.Ticker(ticker_symbol)

    result = {"symbol": ticker_symbol, "timestamp": datetime.now().isoformat()}

    try:
        income = ticker.income_stmt
        if not income.empty:
            result["incomeStatement"] = income.to_dict()
    except Exception as e:
        result["incomeStatementError"] = str(e)

    try:
        balance = ticker.balance_sheet
        if not balance.empty:
            result["balanceSheet"] = balance.to_dict()
    except Exception as e:
        result["balanceSheetError"] = str(e)

    try:
        cashflow = ticker.cashflow
        if not cashflow.empty:
            result["cashFlow"] = cashflow.to_dict()
    except Exception as e:
        result["cashFlowError"] = str(e)

    return result


def get_key_stats(ticker_symbol: str) -> Dict[str, Any]:
    """Get key statistics for a ticker."""
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    key_metrics = {
        # Valuation
        "marketCap": info.get("marketCap"),
        "enterpriseValue": info.get("enterpriseValue"),
        "trailingPE": info.get("trailingPE"),
        "forwardPE": info.get("forwardPE"),
        "priceToBook": info.get("priceToBook"),
        "evToEarnings": info.get("evToEarnings"),
        # Profitability
        "profitMargins": info.get("profitMargins"),
        "grossMargins": info.get("grossMargins"),
        "operatingMargins": info.get("operatingMargins"),
        "ebitdaMargins": info.get("ebitdaMargins"),
        # Growth
        "revenueGrowth": info.get("revenueGrowth"),
        "earningsGrowth": info.get("earningsGrowth"),
        "revenueQuarterlyGrowth": info.get("revenueQuarterlyGrowth"),
        "earningsQuarterlyGrowth": info.get("earningsQuarterlyGrowth"),
        # Dividends
        "dividendRate": info.get("dividendRate"),
        "dividendYield": info.get("dividendYield"),
        "trailingAnnualDividendRate": info.get("trailingAnnualDividendRate"),
        "trailingAnnualDividendYield": info.get("trailingAnnualDividendYield"),
        # Share Structure
        "sharesOutstanding": info.get("sharesOutstanding"),
        "sharesShort": info.get("sharesShort"),
        "floatShares": info.get("floatShares"),
        # Financial Health
        "totalDebt": info.get("totalDebt"),
        "totalCash": info.get("totalCash"),
        "currentRatio": info.get("currentRatio"),
        "quickRatio": info.get("quickRatio"),
        "debtToEquity": info.get("debtToEquity"),
        # Returns
        "returnOnAssets": info.get("returnOnAssets"),
        "returnOnEquity": info.get("returnOnEquity"),
        # Analyst
        "targetMeanPrice": info.get("targetMeanPrice"),
        "targetHighPrice": info.get("targetHighPrice"),
        "targetLowPrice": info.get("targetLowPrice"),
        "recommendationKey": info.get("recommendationKey"),
        "numberOfAnalystOpinions": info.get("numberOfAnalystOpinions"),
    }

    return {
        "symbol": ticker_symbol,
        "timestamp": datetime.now().isoformat(),
        "metrics": {k: v for k, v in key_metrics.items() if v is not None},
    }


def get_company_info(ticker_symbol: str) -> Dict[str, Any]:
    """Get company information for a ticker."""
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info

    company_info = {
        "symbol": ticker_symbol,
        "name": info.get("longName") or info.get("shortName"),
        "summary": info.get("longBusinessSummary"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "website": info.get("website"),
        "exchange": info.get("exchangeName"),
        "currency": info.get("currency"),
        "country": info.get("country"),
        "city": info.get("city"),
        "state": info.get("state"),
        "zip": info.get("zip"),
        "employees": info.get("fullTimeEmployees"),
        "ceo": info.get("ceo"),
    }

    return {k: v for k, v in company_info.items() if v is not None}


def get_dividends(ticker_symbol: str, period: str = "1y") -> Dict[str, Any]:
    """Get dividend history for a ticker."""
    ticker = yf.Ticker(ticker_symbol)
    divs = ticker.dividends

    if divs.empty:
        return {"symbol": ticker_symbol, "dividends": [], "message": "No dividend data"}

    records = []
    for date, amount in divs.items():
        records.append({"date": date.isoformat(), "amount": float(amount)})

    return {
        "symbol": ticker_symbol,
        "period": period,
        "recordCount": len(records),
        "dividends": records[-30:],  # Last 30 dividends
    }


def get_options(ticker_symbol: str) -> Dict[str, Any]:
    """Get options chain for a ticker."""
    ticker = yf.Ticker(ticker_symbol)

    try:
        opt = ticker.option_chain()
        return {
            "symbol": ticker_symbol,
            "timestamp": datetime.now().isoformat(),
            "calls": opt.calls.to_dict("records") if hasattr(opt.calls, "to_dict") else [],
            "puts": opt.puts.to_dict("records") if hasattr(opt.puts, "to_dict") else [],
            "expirationDates": opt.expiration_dates if hasattr(opt, "expiration_dates") else [],
        }
    except Exception as e:
        return {"symbol": ticker_symbol, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Yahoo Finance Scraper")
    parser.add_argument("ticker", help="Stock ticker symbol (e.g., AAPL)")
    parser.add_argument(
        "--type",
        choices=["quote", "history", "financials", "stats", "info", "dividends", "options"],
        default="quote",
        help="Type of data to fetch",
    )
    parser.add_argument("--period", default="1mo", help="Period for historical data")
    parser.add_argument("--interval", default="1d", help="Interval for historical data")
    parser.add_argument("--start", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", help="End date (YYYY-MM-DD)")
    parser.add_argument("--output", help="Output file (JSON)")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON")

    args = parser.parse_args()

    # Fetch data based on type
    if args.type == "quote":
        result = get_quote(args.ticker.upper())
    elif args.type == "history":
        result = get_historical(args.ticker.upper(), args.period, args.interval, args.start, args.end)
    elif args.type == "financials":
        result = get_financials(args.ticker.upper())
    elif args.type == "stats":
        result = get_key_stats(args.ticker.upper())
    elif args.type == "info":
        result = get_company_info(args.ticker.upper())
    elif args.type == "dividends":
        result = get_dividends(args.ticker.upper(), args.period)
    elif args.type == "options":
        result = get_options(args.ticker.upper())
    else:
        result = {"error": "Unknown data type"}

    # Output
    if args.pretty:
        output = json.dumps(result, indent=2, default=str)
    else:
        output = json.dumps(result, default=str)

    print(output)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)


if __name__ == "__main__":
    main()
