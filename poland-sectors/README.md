# Polish sectors and industries

This file maps Polish equities listed on the GPW main market and NewConnect to Biznesradar branża classifications.

- Source: Biznesradar market list pages and dynamically discovered branża pages.
- Refresh: `python3 /workspace/market-intel/bin/poland_sectors.py --refresh`
- `ticker`: exchange ticker.
- `name`: company/security name from the list page.
- `market`: `GPW` or `NC`.
- `sector`: macro-sector derived from the Branża; this is not a Biznesradar field.
- `industry`: Biznesradar branża display name.
- `isin`: intentionally blank by design; no per-ticker profile requests are made.
- `source`: data source.
- `fetched_at`: timezone-aware ISO-8601 timestamp in Asia/Bangkok.
