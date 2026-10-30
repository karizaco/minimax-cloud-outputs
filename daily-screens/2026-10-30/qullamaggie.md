# Qullamaggi — multi-timeframe RS, earnings gaps, 5-day movers

The relative-strength book (1M/3M/6M), the earnings-gap book (10%+ open gap on 50M+ dollar volume) and
the 5-day gainer and loser books. The RS branch required a 252-trading-day lookback to be non-empty.

Universe after the pre-filter (close > $3, market cap > $300M, NYSE/NASDAQ/AMEX): **71 names**.
`Stylists` counts distinct stylist lenses (not sub-screen labels). `10-29` is the move the screen had
already seen on shibui's bar; `10-30` is the settled close that followed.

| Ticker | Name | Close 10-29 | 10-29 | 10-30 | RS 3M | Stylists | Flags / note |
|---|---|---:|---:|---:|---:|---:|---|
| ABCL | AbCellera Biologics Inc. | 13.08 | n/a | -6.19% | +129.1% | 2 | wicky_breakout |
| AMN | AMN Healthcare Services Inc | 46.94 | n/a | +0.36% | +39.6% | 1 | wicky_breakout, ma_shrink_5d |
| APPN | Appian Corporation | 50.47 | n/a | -2.71% | +87.2% | 1 | wicky_breakout, ma_shrink_5d |
| APPS | Digital Turbine, Inc. | 10.57 | +6.66% | -16.08% | +31.1% | 1 | ma_shrink_5d |
| ASAN | Asana, Inc. | 11.26 | n/a | -0.27% | +35.3% | 1 | ma_shrink_5d |
| ASST | Strive, Inc. | 24.91 | n/a | -10.90% | +124.2% | 2 | — |
| BHC | Bausch Health Companies Inc. | 8.91 | +28.76% | -7.97% | +29.3% | 2 | — |
| BLMN | Bloomin' Brands, Inc. | 10.69 | n/a | -1.12% | +23.4% | 1 | — |
| CAI | Caris Life Sciences, Inc. | 36.14 | n/a | -5.01% | +130.6% | 2 | wicky_breakout |
| CDNA | CareDx, Inc. | 71.52 | -0.85% | +22.22% | +63.6% | 3 | ma_shrink_5d |
| CLF | Cleveland-Cliffs Inc. | 14.26 | n/a | -0.07% | +23.8% | 2 | ma_shrink_5d |
| CVI | CVR Energy Inc. | 56.82 | n/a | +2.73% | +59.5% | 2 | wicky_breakout |
| DNA | Ginkgo Bioworks Holdings, Inc. | 12.74 | -4.35% | -12.01% | +57.5% | 1 | wicky_breakout |
| DXC | DXC Technology Company | 15.23 | n/a | -1.64% | +35.5% | 2 | wicky_breakout, ma_shrink_5d |
| FIGS | FIGS, Inc. | 21.56 | +4.36% | -1.16% | +101.5% | 3 | wicky_breakout, ma_shrink_5d |
| GKOS | Glaukos Corporation | 242.48 | +33.65% | -2.01% | +45.4% | 2 | — |
| GLOB | Globant S.A. | 43.68 | n/a | +6.96% | +19.3% | 1 | ma_shrink_5d |
| GMAB | Genmab A/S | 56.49 | n/a | +1.01% | +95.7% | 2 | wicky_breakout |
| GRAL | GRAIL, Inc. | 158.92 | +0.66% | -9.75% | +131.8% | 3 | wicky_breakout |
| GTLB | GitLab Inc. | 56.65 | n/a | -4.52% | +64.2% | 1 | ma_shrink_5d |
| HRI | Herc Holdings Inc. | 173.95 | n/a | -4.71% | +15.9% | 2 | — |
| HTFL | Heartflow, Inc. | 60.53 | +2.42% | -2.45% | +139.9% | 3 | ma_shrink_5d |
| ICLR | ICON plc | 215.48 | n/a | -1.91% | +31.7% | 1 | — |
| KNSA | Kiniksa Pharmaceuticals International, plc | 97.56 | n/a | -5.45% | +31.2% | 2 | — |
| KOD | Kodiak Sciences Inc | 100.40 | +3.46% | -1.22% | +141.5% | 3 | — |
| KSS | Kohl's Corporation | 24.50 | n/a | -0.78% | +28.0% | 1 | ma_shrink_5d |
| MIR | Mirion Technologies, Inc. | 18.67 | n/a | -1.61% | +24.6% | 1 | — |
| MRNA | Moderna, Inc. | 222.76 | +4.01% | -0.47% | +306.3% | 3 | — |
| MSTR | Strategy Inc | 141.62 | n/a | -7.84% | +51.8% | 2 | wicky_breakout, ma_shrink_5d |
| NTSK | Netskope, Inc. | 26.19 | n/a | -7.22% | +108.0% | 2 | — |
| OKTA | Okta, Inc. | 221.86 | n/a | -6.14% | +56.3% | 2 | — |
| OMER | Omeros Corporation | 18.95 | n/a | -2.69% | +60.1% | 1 | — |
| P | Everpure, Inc. | 137.20 | -1.01% | -7.45% | +77.8% | 3 | wicky_breakout |
| PRCH | Porch Group, Inc. | 20.89 | +28.16% | -1.58% | +44.6% | 2 | — |
| PRME | Prime Medicine, Inc. | 5.24 | n/a | -9.92% | +79.5% | 1 | — |
| PSIX | Power Solutions International, Inc. | 48.38 | n/a | -5.48% | +75.2% | 1 | wicky_breakout |
| QLYS | Qualys, Inc. | 230.29 | n/a | -2.68% | +59.1% | 2 | ma_shrink_5d |
| QMCO | Quantum Corporation | 20.77 | +0.24% | -12.04% | +95.2% | 1 | ma_shrink_5d |
| RBRK | Rubrik, Inc. | 133.63 | n/a | -7.09% | +84.7% | 2 | wicky_breakout |
| REPL | Replimune Group, Inc. | 17.39 | n/a | +1.27% | +55.3% | 1 | — |
| RNG | RingCentral, Inc. | 83.70 | n/a | -2.72% | +50.5% | 2 | wicky_breakout |
| RPD | Rapid7, Inc. | 17.08 | n/a | -3.04% | +77.0% | 1 | — |
| SDGR | Schrodinger, Inc. | 29.99 | n/a | -9.50% | +98.1% | 2 | wicky_breakout |
| SG | Sweetgreen, Inc. | 11.41 | n/a | -2.98% | +76.9% | 1 | wicky_breakout |
| TDOC | Teladoc Health, Inc. | 8.73 | +26.89% | -2.52% | +30.1% | 2 | — |
| TEM | Tempus AI, Inc. | 77.84 | n/a | -7.22% | +77.4% | 2 | — |
| TENB | Tenable Holdings, Inc. | 51.78 | n/a | -1.99% | +58.6% | 2 | — |
| TWST | Twist Bioscience Corporation | 173.45 | +0.00% | -11.92% | +89.5% | 2 | wicky_breakout |
| TXG | 10x Genomics, Inc. | 81.55 | -2.48% | -14.03% | +72.5% | 2 | wicky_breakout |
| VSTM | Verastem, Inc. | 9.66 | n/a | +0.93% | +66.6% | 2 | wicky_breakout, ma_shrink_5d |
| ZETA | Zeta Global Holdings Corp. | 32.74 | n/a | -4.80% | +51.6% | 1 | — |
| ZS | Zscaler, Inc. | 247.82 | n/a | -4.03% | +63.9% | 2 | ma_shrink_5d |
| ADT | ADT Inc. | 9.87 | +33.20% | -0.10% | +29.2% | 2 | — |
| CROX | Crocs, Inc. | 150.26 | +25.54% | +0.17% | +17.4% | 2 | — |
| CVNA | Carvana Co. | 68.31 | +15.68% | -0.03% | +9.5% | 2 | — |
| FTAI | FTAI Aviation Ltd. | 196.01 | +17.27% | -4.46% | -4.8% | 3 | — |
| GEN | Gen Digital Inc. | 28.20 | +15.81% | +3.30% | +2.7% | 2 | — |
| INSM | Insmed Incorporated | 111.59 | +15.06% | +0.89% | +13.2% | 2 | — |
| PURR | Hyperliquid Strategies Inc | 12.29 | +23.27% | -10.41% | +97.9% | 3 | — |
| AXGN | Axogen, Inc. | 49.63 | n/a | -0.52% | +17.6% | 2 | wicky_breakout |
| SGRY | Surgery Partners, Inc. | 23.21 | n/a | +0.00% | +50.7% | 1 | wicky_breakout |
| VRT | Vertiv Holdings, LLC | 245.92 | n/a | -5.46% | +1.8% | 1 | — |
| VSAT | ViaSat, Inc. | 77.99 | n/a | -1.24% | +1.4% | 2 | — |
| INTR | Inter & Co. Inc. | 4.17 | n/a | -3.84% | -25.5% | 1 | wicky_breakout |
| IOVA | Iovance Biotherapeutics, Inc. | 9.56 | -35.45% | -11.30% | +134.9% | 3 | — |
| NOW | ServiceNow, Inc. | 109.67 | n/a | -4.15% | -1.4% | 2 | — |
| PAGS | PagSeguro Digital Ltd. | 8.07 | n/a | -1.61% | -16.3% | 1 | wicky_breakout |
| SBS | Companhia de saneamento Basico Do Estado De Sao Paulo - Sabesp | 4.64 | n/a | -2.16% | -14.9% | 1 | wicky_breakout |
| SFM | Sprouts Farmers Market, Inc. | 48.00 | n/a | +3.54% | -44.9% | 2 | — |
| STNE | StoneCo Ltd. | 8.00 | n/a | -3.12% | -29.7% | 1 | wicky_breakout |
| XP | XP Inc. | 15.05 | n/a | -5.05% | -11.8% | 1 | — |
