# Master — deduplicated union of all stylist screens

Master is the union of every stylist book after the pre-filter, deduplicated by ticker. Cap in the
spec is 200; this run produced a larger book because the peoplewish branch alone returns 200 rows under
the shibui row cap.

Universe after the pre-filter (close > $3, market cap > $300M, NYSE/NASDAQ/AMEX): **409 names**.
`Stylists` counts distinct stylist lenses (not sub-screen labels). `10-29` is the move the screen had
already seen on shibui's bar; `10-30` is the settled close that followed.

| Ticker | Name | Close 10-29 | 10-29 | 10-30 | RS 3M | Stylists | Flags / note |
|---|---|---:|---:|---:|---:|---:|---|
| AAL | American Airlines Group, Inc. | 12.78 | n/a | -1.41% | -16.3% | 1 | wicky_breakout |
| AAMI | Acadian Asset Management Inc. | 91.32 | n/a | -2.63% | +5.6% | 1 | — |
| AAPL | Apple Inc. | 348.91 | n/a | -1.23% | +12.9% | 1 | wicky_breakout |
| ABCL | AbCellera Biologics Inc. | 13.08 | n/a | -6.19% | +129.1% | 2 | wicky_breakout |
| ACCO | Acco Brands Corporation | 4.36 | -0.46% | +26.15% | +3.3% | 1 | — |
| ACHR | Archer Aviation Inc. | 4.38 | n/a | -4.11% | -5.6% | 1 | wicky_breakout |
| ADI | Analog Devices, Inc. | 433.28 | n/a | -3.73% | +17.9% | 1 | wicky_breakout |
| ADT | ADT Inc. | 9.87 | +33.20% | -0.10% | +29.2% | 2 | — |
| AFRM | Affirm Holdings, Inc. | 74.84 | n/a | -1.83% | +4.7% | 1 | — |
| AI | C3.ai, Inc. | 12.17 | n/a | -2.63% | +32.6% | 1 | wicky_breakout |
| ALAB | Astera Labs, Inc. | 290.43 | n/a | -10.93% | -6.7% | 2 | wicky_breakout, ma_shrink_5d |
| ALGM | Allegro MicroSystems, Inc. | 33.03 | n/a | -7.57% | -20.4% | 1 | — |
| ALHC | Alignment Healthcare, Inc. | 8.06 | n/a | -9.80% | -45.7% | 1 | ma_shrink_5d |
| ALM | Almonty Industries Inc. | 9.30 | n/a | -6.45% | -15.9% | 1 | wicky_breakout, ma_shrink_5d |
| AMBA | Ambarella, Inc. | 64.58 | n/a | -2.26% | -24.9% | 1 | wicky_breakout |
| AMC | AMC Entertainment Holdings, Inc. | 3.08 | n/a | -0.65% | +9.2% | 1 | — |
| AMD | Advanced Micro Devices, Inc. | 566.42 | n/a | -10.88% | +19.0% | 1 | wicky_breakout, ma_shrink_5d |
| AMG | Affiliated Managers Group, Inc. | 399.02 | n/a | -4.37% | +8.8% | 1 | wicky_breakout |
| AMKR | Amkor Technology, Inc. | 41.21 | n/a | -4.15% | -17.4% | 1 | wicky_breakout, ma_shrink_5d |
| AMN | AMN Healthcare Services Inc | 46.94 | n/a | +0.36% | +39.6% | 1 | wicky_breakout, ma_shrink_5d |
| AMZN | Amazon.com, Inc. | 243.79 | n/a | -1.41% | -10.2% | 1 | — |
| AN | AutoNation, Inc. | 169.34 | n/a | +6.08% | -20.3% | 1 | — |
| ANET | Arista Networks, Inc. | 184.22 | n/a | -8.34% | +2.1% | 1 | wicky_breakout, ma_shrink_5d |
| APH | Amphenol Corporation | 82.08 | n/a | -3.39% | +2.2% | 1 | — |
| APLD | Applied Digital Corporation | 19.41 | n/a | -8.22% | -29.1% | 1 | wicky_breakout, ma_shrink_5d |
| APPN | Appian Corporation | 50.47 | n/a | -2.71% | +87.2% | 1 | wicky_breakout, ma_shrink_5d |
| APPS | Digital Turbine, Inc. | 10.57 | +6.66% | -16.08% | +31.1% | 1 | ma_shrink_5d |
| AR | Antero Resources Corporation | 41.20 | n/a | +2.14% | +14.0% | 1 | ma_shrink_5d |
| ARW | Arrow Electronics, Inc. | 220.92 | n/a | -5.69% | +2.0% | 1 | wicky_breakout, ma_shrink_5d |
| ARX | Accelerant Holdings | 19.82 | n/a | +0.00% | +66.8% | 1 | atr_shrink |
| ARXS | Arxis, Inc. | 54.93 | n/a | -7.48% | +1.2% | 1 | — |
| ASAN | Asana, Inc. | 11.26 | n/a | -0.27% | +35.3% | 1 | ma_shrink_5d |
| ASIC | Ategrity Specialty Insurance Company Holdings | 24.40 | n/a | -2.38% | +1.6% | 1 | ma_shrink_5d |
| ASML | ASML Holding N.V. - New York Registry Shares | 1675.70 | n/a | -6.55% | +2.9% | 1 | wicky_breakout, ma_shrink_5d |
| ASST | Strive, Inc. | 24.91 | n/a | -10.90% | +124.2% | 2 | — |
| ASTH | Astrana Health Inc. | 36.62 | n/a | -0.25% | +3.0% | 1 | wicky_breakout, ma_shrink_5d |
| ASTS | AST SpaceMobile, Inc. | 43.07 | n/a | -4.88% | -27.0% | 1 | wicky_breakout, ma_shrink_5d |
| ASX | ASE Technology Holding Co., Ltd. | 44.55 | n/a | -11.34% | +26.7% | 1 | — |
| ATLC | Atlanticus Holdings Corporation | 98.15 | n/a | -4.78% | -7.0% | 1 | — |
| ATR | AptarGroup, Inc. | 130.64 | n/a | +5.02% | -2.5% | 1 | ma_shrink_5d |
| AUB | Atlantic Union Bankshares Corporation | 39.73 | n/a | -1.16% | -6.4% | 1 | wicky_breakout, ma_shrink_5d |
| AUGO | Aura Minerals Inc. | 78.30 | -4.30% | -15.43% | +43.5% | 1 | wicky_breakout, ma_shrink_5d |
| AUR | Aurora Innovation, Inc. | 4.41 | n/a | -1.02% | -31.7% | 1 | — |
| AVT | Avnet, Inc. | 92.43 | n/a | -4.58% | +4.0% | 1 | wicky_breakout, ma_shrink_5d |
| AXGN | Axogen, Inc. | 49.63 | n/a | -0.52% | +17.6% | 2 | wicky_breakout |
| AXTI | AXT Inc | 60.88 | n/a | -9.56% | +0.7% | 1 | ma_shrink_5d |
| BAM | Brookfield Asset Management Inc | 48.60 | n/a | -0.70% | +0.4% | 1 | — |
| BB | BlackBerry Limited | 9.19 | n/a | -8.38% | +8.1% | 2 | wicky_breakout |
| BBIO | BridgeBio Pharma, Inc. | 70.73 | n/a | +5.97% | -11.7% | 1 | — |
| BBT | Beacon Financial Corporation | 30.66 | n/a | -0.13% | -2.7% | 1 | ma_shrink_5d |
| BE | Bloom Energy Corporation | 222.30 | n/a | -8.61% | +8.0% | 1 | wicky_breakout, ma_shrink_5d |
| BFC | Bank First Corporation | 150.62 | n/a | -1.06% | -1.4% | 1 | ma_shrink_5d |
| BHC | Bausch Health Companies Inc. | 8.91 | +28.76% | -7.97% | +29.3% | 2 | — |
| BLDR | Builders FirstSource, Inc. | 63.06 | n/a | +2.93% | -5.1% | 1 | — |
| BLLN | BillionToOne, Inc. | 114.84 | n/a | -1.32% | -17.1% | 1 | wicky_breakout |
| BLMN | Bloomin' Brands, Inc. | 10.69 | n/a | -1.12% | +23.4% | 1 | — |
| BMNR | BitMine Immersion Technologies, Inc. | 21.66 | n/a | -6.83% | +25.3% | 1 | wicky_breakout, ma_shrink_5d |
| BOOT | Boot Barn Holdings, Inc. | 130.48 | n/a | +1.35% | -12.4% | 1 | — |
| BP | BP p.l.c. | 50.35 | n/a | +0.08% | +11.3% | 1 | wicky_breakout, ma_shrink_5d |
| BSP | Bending Spoons S.p.A. | 46.78 | n/a | -2.69% | +32.9% | 1 | wicky_breakout, ma_shrink_5d |
| BTDR | Bitdeer Technologies Group | 7.58 | -4.29% | -11.48% | -27.9% | 1 | wicky_breakout, ma_shrink_5d |
| BTSG | BrightSpring Health Services, Inc. | 60.22 | +1.28% | +11.08% | +0.9% | 1 | — |
| CAI | Caris Life Sciences, Inc. | 36.14 | n/a | -5.01% | +130.6% | 2 | wicky_breakout |
| CAMT | Camtek Ltd. | 126.67 | n/a | -7.89% | -4.4% | 1 | wicky_breakout, ma_shrink_5d |
| CCEC | Capital Clean Energy Carriers Corp. | 19.73 | n/a | +9.98% | -11.4% | 1 | ma_shrink_5d |
| CCNE | CNB Financial Corporation | 35.61 | n/a | -0.42% | +1.5% | 1 | wicky_breakout, ma_shrink_5d |
| CDLR | Cadeler A/S | 26.69 | n/a | +7.76% | +17.5% | 1 | wicky_breakout, ma_shrink_5d |
| CDNA | CareDx, Inc. | 71.52 | -0.85% | +22.22% | +63.6% | 3 | ma_shrink_5d |
| CELC | Celcuity Inc. | 69.30 | n/a | -0.25% | -19.8% | 1 | wicky_breakout, ma_shrink_5d |
| CIEN | Ciena Corporation | 349.45 | n/a | -8.22% | -7.3% | 1 | wicky_breakout, ma_shrink_5d |
| CIFR | Cipher Digital Inc. | 8.10 | n/a | -10.00% | -63.7% | 1 | ma_shrink_5d |
| CLF | Cleveland-Cliffs Inc. | 14.26 | n/a | -0.07% | +23.8% | 2 | ma_shrink_5d |
| CLMB | Climb Global Solutions, Inc. | 41.84 | n/a | -2.87% | +56.1% | 1 | — |
| CLS | Celestica, Inc. | 282.75 | n/a | -6.09% | -14.7% | 1 | ma_shrink_5d |
| CLSK | CleanSpark, Inc. | 8.20 | n/a | -6.46% | -40.4% | 1 | wicky_breakout, ma_shrink_5d |
| CMBT | CMB.TECH NV | 18.75 | n/a | -1.76% | +16.0% | 1 | wicky_breakout, ma_shrink_5d |
| CMG | Chipotle Mexican Grill, Inc. | 31.28 | n/a | +1.95% | -16.0% | 1 | — |
| CNH | CNH Industrial N.V. | 11.29 | n/a | +4.16% | +10.1% | 1 | ma_shrink_5d |
| CNQ | Canadian Natural Resources Limited | 55.09 | n/a | +1.85% | +15.5% | 1 | wicky_breakout, ma_shrink_5d |
| COCO | The Vita Coco Company, Inc. | 56.27 | n/a | +3.93% | -14.7% | 1 | wicky_breakout |
| COHU | Cohu, Inc. | 53.40 | n/a | -4.89% | +11.3% | 1 | ma_shrink_5d |
| COIN | Coinbase Global, Inc. | 160.59 | n/a | -10.62% | +9.8% | 1 | wicky_breakout, ma_shrink_5d |
| COLM | Columbia Sportswear Company | 63.69 | n/a | +6.04% | +7.3% | 1 | ma_shrink_5d |
| COP | ConocoPhillips | 150.03 | n/a | +2.67% | +24.5% | 1 | wicky_breakout, ma_shrink_5d |
| CORZ | Core Scientific, Inc. | 14.43 | n/a | -8.18% | -30.4% | 1 | wicky_breakout |
| CPRI | Capri Holdings Limited | 16.06 | +5.04% | +16.31% | +0.8% | 1 | ma_shrink_5d |
| CRCL | Circle Internet Group, Inc. | 79.99 | n/a | -9.31% | +27.8% | 1 | wicky_breakout |
| CRGY | Crescent Energy Company | 13.75 | n/a | +3.27% | +19.9% | 1 | wicky_breakout, ma_shrink_5d |
| CROX | Crocs, Inc. | 150.26 | +25.54% | +0.17% | +17.4% | 2 | — |
| CRSP | CRISPR Therapeutics AG | 54.26 | n/a | -5.23% | +13.1% | 1 | wicky_breakout |
| CRWV | CoreWeave, Inc. | 60.74 | n/a | -9.66% | -15.4% | 1 | wicky_breakout, ma_shrink_5d |
| CVCO | Cavco Industries, Inc. | 547.25 | +2.76% | +13.11% | +0.0% | 1 | wicky_breakout, ma_shrink_5d |
| CVE | Cenovus Energy Inc | 32.13 | n/a | +1.87% | +6.4% | 1 | wicky_breakout |
| CVEO | Civeo Corporation (Canada) | 30.55 | +1.09% | +17.74% | -3.0% | 1 | wicky_breakout |
| CVI | CVR Energy Inc. | 56.82 | n/a | +2.73% | +59.5% | 2 | wicky_breakout |
| CVNA | Carvana Co. | 68.31 | +15.68% | -0.03% | +9.5% | 2 | — |
| CVX | Chevron Corporation | 231.46 | n/a | +1.75% | +17.6% | 1 | wicky_breakout, ma_shrink_5d |
| CXT | Crane NXT, Co. | 60.22 | n/a | -2.69% | +15.9% | 1 | ma_shrink_5d |
| DAVE | Dave Inc. | 334.80 | n/a | -5.38% | -10.2% | 1 | wicky_breakout |
| DDOG | Datadog, Inc. | 265.84 | -4.51% | -11.50% | -0.8% | 1 | — |
| DELL | Dell Technologies Inc. | 475.51 | n/a | -10.77% | +17.3% | 1 | ma_shrink_5d |
| DFIN | Donnelley Financial Solutions, Inc. | 61.07 | +14.97% | +9.53% | +29.1% | 2 | — |
| DGII | Digi International Inc. | 77.63 | n/a | -6.30% | +11.3% | 1 | wicky_breakout |
| DHT | DHT Holdings, Inc. | 25.08 | n/a | -0.24% | +35.1% | 1 | ma_shrink_5d |
| DINO | HF Sinclair Corporation | 111.89 | n/a | +2.78% | +22.3% | 1 | — |
| DK | Delek US Holdings, Inc. | 71.10 | n/a | +3.47% | +4.8% | 1 | wicky_breakout |
| DMLP | Dorchester Minerals, L.P. | 30.44 | n/a | -2.10% | +10.2% | 1 | ma_shrink_5d |
| DNA | Ginkgo Bioworks Holdings, Inc. | 12.74 | -4.35% | -12.01% | +57.5% | 1 | wicky_breakout |
| DRS | Leonardo DRS, Inc. | 39.64 | n/a | -4.94% | -13.9% | 1 | — |
| DVN | Devon Energy Corporation | 51.17 | n/a | +1.92% | +13.4% | 1 | wicky_breakout, ma_shrink_5d |
| DXC | DXC Technology Company | 15.23 | n/a | -1.64% | +35.5% | 2 | wicky_breakout, ma_shrink_5d |
| ECO | Okeanis Eco Tankers Corp. | 101.63 | n/a | -0.30% | +68.5% | 1 | — |
| ELF | e.l.f. Beauty, Inc. | 112.95 | n/a | -1.12% | +36.3% | 1 | — |
| ENPH | Enphase Energy, Inc. | 25.86 | n/a | -0.81% | -31.1% | 1 | — |
| ENTG | Entegris, Inc. | 160.00 | n/a | -3.51% | +34.4% | 1 | — |
| EOG | EOG Resources, Inc. | 162.22 | n/a | +2.05% | +9.1% | 1 | wicky_breakout, ma_shrink_5d |
| EPD | Enterprise Products Partners L.P. | 39.05 | n/a | -2.30% | +2.6% | 1 | — |
| EQBK | Equity Bancshares, Inc. | 49.11 | n/a | -0.88% | -3.1% | 1 | wicky_breakout, ma_shrink_5d |
| EQPT | EquipmentShare.com Inc | 18.18 | n/a | -5.50% | -3.0% | 1 | wicky_breakout, ma_shrink_5d |
| ERAS | Erasca, Inc. | 14.98 | n/a | -4.21% | -17.5% | 1 | wicky_breakout |
| ERIE | Erie Indemnity Company | 250.79 | n/a | +4.23% | +3.6% | 1 | wicky_breakout, ma_shrink_5d |
| EXEL | Exelixis, Inc. | 66.20 | n/a | +4.82% | +24.8% | 1 | ma_shrink_5d |
| EXPD | Expeditors International of Washington, Inc. | 198.39 | n/a | +0.23% | +18.2% | 1 | — |
| F | Ford Motor Company | 12.36 | n/a | -0.89% | -15.8% | 1 | — |
| FANG | Diamondback Energy, Inc. | 206.43 | n/a | +2.74% | +1.7% | 1 | wicky_breakout, ma_shrink_5d |
| FCN | FTI Consulting, Inc. | 181.24 | n/a | +0.88% | +13.7% | 1 | — |
| FDXF | FedEx Freight Holding Company, Inc. | 109.69 | +1.26% | +14.91% | -21.9% | 1 | — |
| FICO | Fair Isaac Corporation | 709.18 | n/a | +0.29% | -36.8% | 1 | — |
| FIGR | Figure Technology Solutions, Inc. | 23.59 | n/a | -8.52% | -5.3% | 1 | ma_shrink_5d |
| FIGS | FIGS, Inc. | 21.56 | +4.36% | -1.16% | +101.5% | 3 | wicky_breakout, ma_shrink_5d |
| FIS | Fidelity National Information Services, Inc. | 37.28 | n/a | +3.41% | -16.7% | 1 | ma_shrink_5d |
| FISV | Fiserv, Inc. | 48.48 | n/a | +3.18% | -10.1% | 1 | — |
| FIVN | Five9, Inc. | 37.41 | n/a | -2.86% | +36.0% | 1 | wicky_breakout, ma_shrink_5d |
| FLEX | Flex Ltd. | 93.07 | n/a | -7.08% | -18.2% | 1 | ma_shrink_5d |
| FLS | Flowserve Corporation | 80.35 | n/a | -1.67% | +5.7% | 1 | — |
| FLY | Firefly Aerospace Inc. | 19.87 | n/a | -9.74% | -2.3% | 1 | wicky_breakout, ma_shrink_5d |
| FROG | JFrog Ltd. | 98.83 | n/a | -4.49% | +23.9% | 1 | wicky_breakout |
| FSLY | Fastly, Inc. | 25.64 | n/a | -9.85% | +13.2% | 1 | wicky_breakout |
| FTAI | FTAI Aviation Ltd. | 196.01 | +17.27% | -4.46% | -4.8% | 3 | — |
| FVRR | Fiverr International Ltd. | 9.05 | n/a | -7.29% | +1.3% | 1 | — |
| GATX | GATX Corporation | 180.47 | n/a | +0.37% | +0.9% | 1 | — |
| GBCI | Glacier Bancorp, Inc. | 48.79 | n/a | -0.47% | -1.0% | 1 | ma_shrink_5d |
| GCT | GigaCloud Technology Inc | 60.62 | n/a | -3.70% | +38.6% | 1 | wicky_breakout |
| GDDY | GoDaddy Inc. | 105.89 | n/a | +10.72% | +28.0% | 1 | — |
| GDYN | Grid Dynamics Holdings, Inc. | 9.49 | +8.46% | +40.78% | +37.7% | 1 | — |
| GEN | Gen Digital Inc. | 28.20 | +15.81% | +3.30% | +2.7% | 2 | — |
| GH | Guardant Health, Inc. | 185.31 | n/a | -3.51% | +14.4% | 1 | wicky_breakout |
| GKOS | Glaukos Corporation | 242.48 | +33.65% | -2.01% | +45.4% | 2 | — |
| GLBE | Global-E Online Ltd. | 43.04 | n/a | -3.81% | +9.5% | 1 | ma_shrink_5d |
| GLOB | Globant S.A. | 43.68 | n/a | +6.96% | +19.3% | 1 | ma_shrink_5d |
| GLXY | Galaxy Digital Inc. | 18.13 | -5.03% | -11.75% | -13.7% | 1 | wicky_breakout |
| GMAB | Genmab A/S | 56.49 | n/a | +1.01% | +95.7% | 2 | wicky_breakout |
| GOOGL | Alphabet Inc. | 283.82 | n/a | -1.40% | -20.3% | 1 | — |
| GPN | Global Payments Inc. | 85.72 | +2.60% | +12.97% | +2.0% | 1 | — |
| GRAL | GRAIL, Inc. | 158.92 | +0.66% | -9.75% | +131.8% | 3 | wicky_breakout |
| GTLB | GitLab Inc. | 56.65 | n/a | -4.52% | +64.2% | 1 | ma_shrink_5d |
| HALO | Halozyme Therapeutics, Inc. | 131.18 | n/a | -0.21% | +58.9% | 1 | wicky_breakout, ma_shrink_5d |
| HAPN | Happen, Inc. | 16.04 | n/a | -3.18% | -16.2% | 1 | — |
| HBT | HBT Financial, Inc. | 36.80 | n/a | -0.76% | +2.7% | 1 | wicky_breakout |
| HII | Huntington Ingalls Industries, Inc. | 316.21 | n/a | +0.21% | -3.1% | 1 | — |
| HIMS | Hims & Hers Health, Inc. | 29.67 | n/a | -6.71% | +6.8% | 1 | wicky_breakout |
| HLN | Haleon plc | 8.57 | n/a | +1.05% | -13.2% | 1 | — |
| HP | Helmerich & Payne, Inc. | 41.58 | n/a | +3.39% | +20.3% | 1 | — |
| HPE | Hewlett Packard Enterprise Company | 58.87 | n/a | -6.42% | +22.9% | 1 | wicky_breakout, ma_shrink_5d |
| HPK | HighPeak Energy, Inc. | 10.45 | n/a | -2.49% | +46.2% | 2 | ma_shrink_5d |
| HRI | Herc Holdings Inc. | 173.95 | n/a | -4.71% | +15.9% | 2 | — |
| HRMY | Harmony Biosciences Holdings, Inc. | 38.59 | n/a | +0.44% | +9.5% | 1 | wicky_breakout |
| HTFL | Heartflow, Inc. | 60.53 | +2.42% | -2.45% | +139.9% | 3 | ma_shrink_5d |
| HUM | Humana Inc. | 417.56 | n/a | -0.73% | +14.8% | 1 | wicky_breakout, ma_shrink_5d |
| HUT | Hut 8 Corp. | 66.44 | n/a | -10.60% | -38.3% | 1 | wicky_breakout, ma_shrink_5d |
| IBRX | ImmunityBio, Inc. | 8.74 | n/a | -5.15% | +21.9% | 1 | wicky_breakout, ma_shrink_5d |
| ICLR | ICON plc | 215.48 | n/a | -1.91% | +31.7% | 1 | — |
| ILMN | Illumina, Inc. | 290.06 | +0.44% | -18.64% | +41.4% | 1 | wicky_breakout |
| IMO | Imperial Oil Limited | 130.87 | n/a | +5.52% | +1.0% | 1 | wicky_breakout, ma_shrink_5d |
| INCY | Incyte Corporation | 116.80 | n/a | +3.07% | -2.3% | 1 | — |
| INDB | Independent Bank Corp. | 83.71 | n/a | -1.16% | -0.1% | 1 | wicky_breakout, ma_shrink_5d |
| INFQ | Infleqtion, Inc. | 9.43 | n/a | -5.83% | -4.1% | 1 | wicky_breakout, ma_shrink_5d |
| INIO | INNIO N.V. | 17.52 | n/a | -6.96% | -28.3% | 1 | — |
| INSM | Insmed Incorporated | 111.59 | +15.06% | +0.89% | +13.2% | 2 | — |
| INSW | International Seaways, Inc. | 113.60 | n/a | -1.45% | +18.1% | 1 | wicky_breakout, ma_shrink_5d |
| INTC | Intel Corporation | 92.07 | -3.62% | -28.58% | +2.1% | 1 | ma_shrink_5d |
| INTR | Inter & Co. Inc. | 4.17 | n/a | -3.84% | -25.5% | 1 | wicky_breakout |
| IONQ | IonQ, Inc. | 31.72 | n/a | -5.30% | -13.0% | 1 | wicky_breakout, ma_shrink_5d |
| IOVA | Iovance Biotherapeutics, Inc. | 9.56 | -35.45% | -11.30% | +134.9% | 3 | — |
| IREN | IREN Limited | 26.25 | n/a | -8.76% | -28.7% | 1 | ma_shrink_5d |
| IRON | Disc Medicine, Inc. | 82.84 | n/a | -2.41% | +7.6% | 1 | wicky_breakout, ma_shrink_5d |
| ITG | ITG, Inc. | 5.68 | n/a | +5.11% | -56.1% | 1 | ma_shrink_5d |
| ITUB | Itau Unibanco Banco Holding SA | 7.37 | n/a | -3.26% | -12.9% | 1 | wicky_breakout |
| JBLU | JetBlue Airways Corporation | 3.05 | n/a | -6.56% | -49.4% | 1 | ma_shrink_5d |
| JOBY | Joby Aviation, Inc. | 5.08 | n/a | -3.54% | -29.0% | 1 | wicky_breakout, ma_shrink_5d |
| JPM | JP Morgan Chase & Co. | 343.58 | n/a | -1.90% | -2.3% | 1 | wicky_breakout |
| KARO | Karooooo Ltd. | 66.70 | n/a | -1.56% | +3.8% | 1 | ma_shrink_5d |
| KEYS | Keysight Technologies Inc. | 329.84 | n/a | -6.86% | +3.4% | 1 | wicky_breakout, ma_shrink_5d |
| KNSA | Kiniksa Pharmaceuticals International, plc | 97.56 | n/a | -5.45% | +31.2% | 2 | — |
| KNTK | Kinetik Holdings Inc. | 58.09 | n/a | -2.56% | +14.9% | 1 | wicky_breakout |
| KOD | Kodiak Sciences Inc | 100.40 | +3.46% | -1.22% | +141.5% | 3 | — |
| KRMN | Karman Holdings Inc. | 41.69 | n/a | -4.17% | -13.4% | 1 | — |
| KSS | Kohl's Corporation | 24.50 | n/a | -0.78% | +28.0% | 1 | ma_shrink_5d |
| KVYO | Klaviyo, Inc. Series A | 20.43 | n/a | -1.42% | +14.5% | 1 | ma_shrink_5d |
| KYMR | Kymera Therapeutics, Inc. | 122.60 | n/a | +3.29% | +18.6% | 2 | — |
| LB | LandBridge Corporation | 82.83 | n/a | +0.92% | +6.8% | 1 | wicky_breakout, ma_shrink_5d |
| LBRT | Liberty Energy Inc. | 17.41 | n/a | -3.04% | -6.9% | 1 | wicky_breakout |
| LGN | Legence Corp. | 41.90 | n/a | -7.33% | -34.5% | 1 | ma_shrink_5d |
| LGND | Ligand Pharmaceuticals Incorporated | 317.33 | n/a | +1.71% | +10.4% | 1 | — |
| LITE | Lumentum Holdings Inc. | 919.53 | n/a | -8.57% | +28.8% | 1 | — |
| LLY | Eli Lilly and Company | 1373.70 | n/a | +3.19% | +19.6% | 2 | — |
| LPG | Dorian LPG Ltd. | 54.68 | n/a | -0.46% | +15.3% | 1 | wicky_breakout |
| LQDA | Liquidia Corporation | 44.99 | n/a | +0.16% | -46.5% | 1 | wicky_breakout, ma_shrink_5d |
| LTC | LTC Properties, Inc. | 44.32 | n/a | +0.97% | +10.1% | 1 | — |
| LUMN | Lumen Technologies, Inc. | 4.79 | n/a | +1.88% | -24.9% | 1 | wicky_breakout, ma_shrink_5d |
| LUNR | Intuitive Machines, Inc. | 11.68 | n/a | -8.65% | -5.3% | 1 | wicky_breakout, ma_shrink_5d |
| MANE | Veradermics, Incorporated | 143.85 | n/a | -2.89% | +37.0% | 1 | wicky_breakout, ma_shrink_5d |
| MAX | MediaAlpha, Inc. | 14.13 | +20.56% | +4.39% | +14.1% | 2 | — |
| MBIN | Merchants Bancorp | 52.00 | n/a | +0.17% | -5.8% | 1 | — |
| MDB | MongoDB, Inc. | 384.95 | n/a | -8.31% | +14.1% | 1 | wicky_breakout |
| MEOH | Methanex Corporation | 62.76 | -1.24% | +14.04% | +13.0% | 2 | wicky_breakout |
| MESO | Mesoblast Limited | 15.67 | n/a | -3.25% | +10.6% | 1 | — |
| MHK | Mohawk Industries, Inc. | 129.99 | n/a | +7.25% | +5.6% | 1 | — |
| MIR | Mirion Technologies, Inc. | 18.67 | n/a | -1.61% | +24.6% | 1 | — |
| MMYT | MakeMyTrip Limited | 43.00 | n/a | -0.74% | -24.5% | 1 | wicky_breakout |
| MNDY | monday.com Ltd. | 94.78 | n/a | +0.87% | +8.8% | 1 | wicky_breakout |
| MPC | Marathon Petroleum Corporation | 432.51 | n/a | +2.83% | +36.7% | 2 | wicky_breakout |
| MRNA | Moderna, Inc. | 222.76 | +4.01% | -0.47% | +306.3% | 3 | — |
| MRVL | Marvell Technology, Inc. | 218.34 | n/a | -10.05% | +16.4% | 2 | ma_shrink_5d |
| MSFT | Microsoft Corporation | 530.14 | n/a | -1.55% | +14.1% | 1 | — |
| MSTR | Strategy Inc | 141.62 | n/a | -7.84% | +51.8% | 2 | wicky_breakout, ma_shrink_5d |
| MTDR | Matador Resources Company | 59.83 | n/a | +1.75% | +19.9% | 1 | wicky_breakout, ma_shrink_5d |
| MTRN | Materion Corporation | 239.81 | n/a | -7.45% | +13.7% | 2 | wicky_breakout, ma_shrink_5d |
| MTZ | MasTec, Inc. | 177.82 | n/a | +4.63% | -32.4% | 1 | ma_shrink_5d |
| MU | Micron Technology, Inc. | 934.27 | n/a | -5.30% | +13.5% | 1 | — |
| MUR | Murphy Oil Corporation | 42.84 | n/a | +2.59% | +7.8% | 1 | wicky_breakout, ma_shrink_5d |
| MUSA | Murphy USA Inc. | 540.00 | n/a | -0.94% | -11.1% | 1 | — |
| NBBK | NB Bancorp, Inc. | 22.56 | n/a | -1.91% | -2.0% | 1 | — |
| NBIS | Nebius Group N.V. | 171.99 | n/a | -10.38% | -9.7% | 1 | wicky_breakout, ma_shrink_5d |
| NCLH | Norwegian Cruise Line Holdings Ltd. | 18.22 | n/a | -3.57% | -1.7% | 1 | — |
| NESR | National Energy Services Reunited Corp | 21.43 | n/a | -0.56% | -20.5% | 1 | wicky_breakout, ma_shrink_5d |
| NET | Cloudflare, Inc. | 310.30 | n/a | -9.54% | +11.2% | 1 | ma_shrink_5d |
| NEXT | NextDecade Corporation | 7.26 | n/a | +1.65% | +8.0% | 1 | — |
| NFLX | Netflix, Inc. | 62.05 | n/a | +0.05% | -13.5% | 1 | wicky_breakout |
| NGL | NGL ENERGY PARTNERS LP | 16.65 | n/a | -1.38% | +1.6% | 1 | — |
| NOK | Nokia Corporation Sponsored | 9.31 | n/a | -8.06% | +1.9% | 1 | ma_shrink_5d |
| NOW | ServiceNow, Inc. | 109.67 | n/a | -4.15% | -1.4% | 2 | — |
| NP | Neptune Insurance Holdings Inc. | 28.81 | n/a | +1.28% | -9.1% | 1 | — |
| NRIX | Nurix Therapeutics, Inc. | 27.12 | n/a | -1.18% | +16.8% | 1 | wicky_breakout, ma_shrink_5d |
| NSP | Insperity, Inc. | 46.29 | n/a | +5.16% | -8.5% | 1 | — |
| NTAP | NetApp, Inc. | 218.42 | n/a | -8.81% | +22.4% | 1 | wicky_breakout |
| NTLA | Intellia Therapeutics, Inc. | 13.23 | n/a | -5.74% | +23.9% | 1 | wicky_breakout |
| NTRS | Northern Trust Corporation | 172.92 | n/a | -2.17% | -5.1% | 1 | wicky_breakout |
| NTSK | Netskope, Inc. | 26.19 | n/a | -7.22% | +108.0% | 2 | — |
| NU | Nu Holdings Ltd. | 12.05 | n/a | -3.65% | -15.9% | 1 | wicky_breakout |
| NVAX | Novavax, Inc. | 10.47 | n/a | -3.72% | +43.0% | 1 | ma_shrink_5d |
| NVDA | NVIDIA Corporation | 213.66 | n/a | -4.22% | +6.4% | 2 | wicky_breakout, ma_shrink_5d |
| NVGS | Navigator Holdings Ltd. | 21.71 | n/a | -0.92% | -2.9% | 1 | wicky_breakout, ma_shrink_5d |
| NVTS | Navitas Semiconductor Corporation | 9.20 | n/a | -7.83% | -15.3% | 1 | wicky_breakout, ma_shrink_5d |
| NXT | Nextpower Inc. | 79.83 | n/a | -0.63% | -11.2% | 1 | — |
| OBA | Oxley Bridge Acquisition Limited | 10.37 | n/a | -0.10% | +1.1% | 1 | ma_shrink_5d |
| OKE | ONEOK, Inc. | 95.82 | n/a | +1.30% | +5.5% | 1 | wicky_breakout, ma_shrink_5d |
| OKTA | Okta, Inc. | 221.86 | n/a | -6.14% | +56.3% | 2 | — |
| OMC | Omnicom Group Inc. | 80.97 | n/a | +0.36% | +2.9% | 1 | — |
| OMER | Omeros Corporation | 18.95 | n/a | -2.69% | +60.1% | 1 | — |
| ONC | BeOne Medicines Ltd. | 371.56 | n/a | -0.33% | +17.6% | 1 | wicky_breakout |
| ONDS | Ondas Inc | 6.88 | n/a | -8.14% | -8.1% | 2 | wicky_breakout |
| ORCL | Oracle Corporation | 139.56 | n/a | -6.37% | +7.5% | 1 | — |
| ORKA | Oruka Therapeutics, Inc. | 96.65 | n/a | +0.23% | +0.1% | 1 | wicky_breakout |
| OSPN | OneSpan Inc. | 20.15 | +0.35% | +27.34% | +30.2% | 1 | — |
| OUST | Ouster, Inc. | 32.14 | n/a | -7.47% | -17.6% | 1 | wicky_breakout, ma_shrink_5d |
| OVV | Ovintiv Inc. (DE) | 71.57 | n/a | +1.47% | +14.6% | 1 | wicky_breakout, ma_shrink_5d |
| OXY | Occidental Petroleum Corporation | 63.01 | n/a | +1.57% | +10.4% | 1 | wicky_breakout, ma_shrink_5d |
| P | Everpure, Inc. | 137.20 | -1.01% | -7.45% | +77.8% | 3 | wicky_breakout |
| PAA | Plains All American Pipeline, L.P. | 26.91 | n/a | -1.50% | +9.5% | 1 | ma_shrink_5d |
| PAGP | Plains GP Holdings, L.P. | 28.82 | n/a | -1.49% | +9.5% | 1 | wicky_breakout, ma_shrink_5d |
| PAGS | PagSeguro Digital Ltd. | 8.07 | n/a | -1.61% | -16.3% | 1 | wicky_breakout |
| PARR | Par Pacific Holdings, Inc. Common Stock | 73.31 | n/a | +4.00% | -14.8% | 1 | — |
| PAY | Paymentus Holdings, Inc. | 32.26 | n/a | +1.74% | -5.4% | 1 | wicky_breakout |
| PBF | PBF Energy Inc. | 75.54 | n/a | +3.26% | +4.5% | 1 | — |
| PBT | Permian Basin Royalty Trust | 32.46 | n/a | -2.59% | +9.6% | 1 | ma_shrink_5d |
| PCVX | Vaxcyte, Inc. | 62.61 | n/a | -0.93% | +15.8% | 1 | wicky_breakout, ma_shrink_5d |
| PI | Impinj, Inc. | 182.55 | n/a | -1.58% | +20.6% | 1 | — |
| PINS | Pinterest, Inc. | 19.92 | n/a | -2.81% | -17.0% | 1 | — |
| PL | Planet Labs PBC | 14.31 | n/a | -5.87% | -30.1% | 1 | ma_shrink_5d |
| PLTR | Palantir Technologies Inc. | 196.42 | n/a | -6.27% | +59.6% | 1 | wicky_breakout, ma_shrink_5d |
| POET | POET Technologies Inc. | 5.66 | n/a | -8.13% | -19.0% | 1 | wicky_breakout, ma_shrink_5d |
| POWL | Powell Industries, Inc. | 168.48 | n/a | -7.25% | -19.3% | 1 | ma_shrink_5d |
| PR | Permian Resources Corporation | 25.57 | n/a | +1.76% | +20.0% | 1 | wicky_breakout, ma_shrink_5d |
| PRCH | Porch Group, Inc. | 20.89 | +28.16% | -1.58% | +44.6% | 2 | — |
| PRIM | Primoris Services Corporation | 75.61 | n/a | -3.76% | -10.4% | 1 | — |
| PRME | Prime Medicine, Inc. | 5.24 | n/a | -9.92% | +79.5% | 1 | — |
| PSIX | Power Solutions International, Inc. | 48.38 | n/a | -5.48% | +75.2% | 1 | wicky_breakout |
| PSX | Phillips 66 | 273.61 | n/a | +3.37% | +29.3% | 1 | — |
| PURR | Hyperliquid Strategies Inc | 12.29 | +23.27% | -10.41% | +97.9% | 3 | — |
| PWR | Quanta Services, Inc. | 635.18 | n/a | -2.27% | -4.8% | 1 | — |
| QBTS | D-Wave Quantum Inc. | 11.56 | n/a | -7.87% | -36.1% | 1 | ma_shrink_5d |
| QLYS | Qualys, Inc. | 230.29 | n/a | -2.68% | +59.1% | 2 | ma_shrink_5d |
| QMCO | Quantum Corporation | 20.77 | +0.24% | -12.04% | +95.2% | 1 | ma_shrink_5d |
| QNT | Quantinuum Inc. | 37.49 | n/a | -10.39% | -27.1% | 1 | wicky_breakout, ma_shrink_5d |
| QS | QuantumScape Corporation | 4.20 | n/a | -3.33% | -19.5% | 1 | wicky_breakout |
| QXO | QXO, Inc. | 11.38 | n/a | -2.99% | -14.4% | 1 | — |
| RBRK | Rubrik, Inc. | 133.63 | n/a | -7.09% | +84.7% | 2 | wicky_breakout |
| RDW | Redwire Corporation | 9.16 | n/a | -8.41% | +6.3% | 1 | ma_shrink_5d |
| REAL | The RealReal, Inc. | 11.35 | n/a | +5.37% | -6.1% | 1 | — |
| REGN | Regeneron Pharmaceuticals, Inc. | 818.77 | +0.68% | +13.33% | +7.4% | 1 | ma_shrink_5d |
| REPL | Replimune Group, Inc. | 17.39 | n/a | +1.27% | +55.3% | 1 | — |
| REPX | Riley Exploration Permian, Inc. | 52.10 | n/a | +2.25% | +52.0% | 2 | wicky_breakout, ma_shrink_5d |
| RGEN | Repligen Corporation | 188.64 | n/a | -6.20% | +33.8% | 1 | wicky_breakout |
| RGTI | Rigetti Computing, Inc. | 12.06 | n/a | -6.72% | -19.3% | 1 | wicky_breakout, ma_shrink_5d |
| RIG | Transocean Ltd (Switzerland) | 6.69 | n/a | +3.74% | +25.8% | 1 | wicky_breakout, ma_shrink_5d |
| RIOT | Riot Platforms, Inc. | 13.74 | n/a | -6.77% | -31.9% | 1 | wicky_breakout, ma_shrink_5d |
| RIVN | Rivian Automotive, Inc. | 11.45 | n/a | +6.20% | -24.8% | 2 | ma_shrink_5d |
| RKLB | Rocket Lab Corporation | 59.10 | n/a | -7.39% | -9.0% | 1 | wicky_breakout, ma_shrink_5d |
| RMBS | Rambus, Inc. | 90.99 | n/a | -6.97% | -0.0% | 1 | ma_shrink_5d |
| RNG | RingCentral, Inc. | 83.70 | n/a | -2.72% | +50.5% | 2 | wicky_breakout |
| RNST | Renasant Corporation | 40.26 | n/a | -0.82% | -7.6% | 1 | — |
| RPD | Rapid7, Inc. | 17.08 | n/a | -3.04% | +77.0% | 1 | — |
| RS | Reliance, Inc. | 439.71 | n/a | -0.64% | +8.3% | 1 | wicky_breakout |
| RUN | Sunrun Inc. | 7.59 | n/a | -1.45% | -22.6% | 1 | — |
| RXRX | Recursion Pharmaceuticals, Inc. | 4.24 | n/a | -4.95% | +41.3% | 1 | wicky_breakout |
| SAIL | SailPoint, Inc. | 22.00 | n/a | -4.27% | +31.2% | 1 | — |
| SBET | Sharplink, Inc. | 7.23 | n/a | -6.78% | +18.1% | 1 | wicky_breakout, ma_shrink_5d |
| SBS | Companhia de saneamento Basico Do Estado De Sao Paulo - Sabesp | 4.64 | n/a | -2.16% | -14.9% | 1 | wicky_breakout |
| SCCO | Southern Copper Corporation | 191.75 | n/a | -7.42% | +6.2% | 1 | wicky_breakout, ma_shrink_5d |
| SDGR | Schrodinger, Inc. | 29.99 | n/a | -9.50% | +98.1% | 2 | wicky_breakout |
| SEDG | SolarEdge Technologies, Inc. | 30.54 | n/a | -1.59% | -25.9% | 1 | — |
| SEI | Solaris Energy Infrastructure, Inc. | 69.12 | n/a | +2.29% | +34.4% | 1 | wicky_breakout |
| SEZL | Sezzle Inc. | 133.86 | n/a | +0.74% | -13.5% | 2 | wicky_breakout |
| SFM | Sprouts Farmers Market, Inc. | 48.00 | n/a | +3.54% | -44.9% | 2 | — |
| SG | Sweetgreen, Inc. | 11.41 | n/a | -2.98% | +76.9% | 1 | wicky_breakout |
| SGRY | Surgery Partners, Inc. | 23.21 | n/a | +0.00% | +50.7% | 1 | wicky_breakout |
| SHOP | Shopify Inc. | 166.89 | n/a | -5.63% | +42.5% | 1 | wicky_breakout, ma_shrink_5d |
| SIMO | Silicon Motion Technology Corporation | 227.75 | n/a | -8.39% | -10.2% | 1 | ma_shrink_5d |
| SITM | SiTime Corporation | 488.08 | n/a | -8.40% | -8.8% | 1 | wicky_breakout, ma_shrink_5d |
| SKY | Champion Homes, Inc. | 81.05 | n/a | +4.50% | +1.8% | 1 | wicky_breakout, ma_shrink_5d |
| SKYD | Skydance Corporation | 7.90 | n/a | +0.63% | -0.8% | 1 | wicky_breakout, ma_shrink_5d |
| SLS | SELLAS Life Sciences Group, Inc. | 10.15 | n/a | -4.68% | +1.4% | 1 | — |
| SM | SM Energy Company | 39.58 | n/a | +2.02% | +21.7% | 1 | wicky_breakout, ma_shrink_5d |
| SMCI | Super Micro Computer, Inc. | 34.43 | n/a | -4.30% | +21.2% | 2 | wicky_breakout, ma_shrink_5d |
| SMMT | Summit Therapeutics Inc. | 16.20 | n/a | -1.05% | +24.4% | 1 | — |
| SMP | Standard Motor Products, Inc. | 38.25 | +0.98% | +10.88% | +0.1% | 1 | wicky_breakout |
| SMR | NuScale Power Corporation | 5.92 | n/a | -5.07% | -29.7% | 1 | ma_shrink_5d |
| SNAP | Snap Inc. | 5.68 | n/a | -5.99% | +21.1% | 2 | wicky_breakout |
| SNDK | Sandisk Corporation | 1330.05 | -5.32% | -13.47% | +9.5% | 1 | ma_shrink_5d |
| SNPS | Synopsys, Inc. | 490.19 | n/a | -4.61% | +26.1% | 1 | — |
| SNX | TD SYNNEX Corporation | 255.07 | n/a | -7.23% | -0.2% | 1 | wicky_breakout, ma_shrink_5d |
| SOFI | SoFi Technologies, Inc. | 17.61 | n/a | -4.83% | +8.0% | 1 | — |
| SPCX | Space Exploration Technologies Corp | 143.89 | n/a | -6.37% | +32.8% | 1 | wicky_breakout, ma_shrink_5d |
| SPHR | Sphere Entertainment Co. | 113.10 | n/a | -3.50% | -21.0% | 1 | ma_shrink_5d |
| STGW | Stagwell Inc. | 9.95 | +12.68% | +5.23% | +17.8% | 2 | — |
| STLD | Steel Dynamics, Inc. | 253.53 | n/a | -1.08% | +0.9% | 1 | wicky_breakout |
| STNE | StoneCo Ltd. | 8.00 | n/a | -3.12% | -29.7% | 1 | wicky_breakout |
| STX | Seagate Technology Holdings PLC | 700.47 | n/a | -7.98% | -18.2% | 2 | wicky_breakout, ma_shrink_5d |
| SU | Suncor Energy Inc. | 77.63 | n/a | +2.31% | +15.4% | 1 | wicky_breakout, ma_shrink_5d |
| SYRE | Spyre Therapeutics, Inc. | 98.96 | n/a | -2.43% | +0.6% | 1 | wicky_breakout, ma_shrink_5d |
| T | AT&T Inc. | 20.92 | n/a | +2.34% | -10.0% | 1 | wicky_breakout, ma_shrink_5d |
| TDOC | Teladoc Health, Inc. | 8.73 | +26.89% | -2.52% | +30.1% | 2 | — |
| TECK | Teck Resources Ltd | 63.72 | n/a | -4.88% | +5.8% | 1 | — |
| TEM | Tempus AI, Inc. | 77.84 | n/a | -7.22% | +77.4% | 2 | — |
| TENB | Tenable Holdings, Inc. | 51.78 | n/a | -1.99% | +58.6% | 2 | — |
| THRM | Gentherm Inc | 32.20 | n/a | -3.88% | -20.7% | 1 | — |
| TLN | Talen Energy Corporation | 348.85 | n/a | -1.64% | +4.4% | 1 | wicky_breakout |
| TNGX | Tango Therapeutics, Inc. | 22.53 | n/a | +0.84% | -17.1% | 1 | wicky_breakout |
| TNK | Teekay Tankers Ltd. | 101.23 | n/a | -0.42% | +27.5% | 1 | wicky_breakout, ma_shrink_5d |
| TPG | TPG Inc. | 47.94 | n/a | -2.63% | +9.8% | 1 | — |
| TRMD | TORM plc | 43.05 | n/a | -0.82% | +42.0% | 2 | — |
| TSEM | Tower Semiconductor Ltd. | 187.92 | n/a | -11.41% | -14.5% | 1 | wicky_breakout, ma_shrink_5d |
| TTE | TotalEnergies SE | 94.03 | n/a | +1.38% | +7.0% | 1 | wicky_breakout, ma_shrink_5d |
| TWFG | TWFG, Inc. | 27.15 | n/a | -0.70% | +1.3% | 1 | wicky_breakout |
| TWLO | Twilio Inc. | 241.90 | -4.68% | -15.24% | +22.6% | 1 | wicky_breakout, ma_shrink_5d |
| TWST | Twist Bioscience Corporation | 173.45 | +0.00% | -11.92% | +89.5% | 2 | wicky_breakout |
| TXG | 10x Genomics, Inc. | 81.55 | -2.48% | -14.03% | +72.5% | 2 | wicky_breakout |
| TXN | Texas Instruments Incorporated | 312.94 | n/a | -3.87% | +13.5% | 1 | — |
| TXT | Textron Inc. | 87.46 | n/a | -2.01% | +2.6% | 1 | — |
| UCTT | Ultra Clean Holdings, Inc. | 54.70 | n/a | -9.12% | -34.3% | 1 | ma_shrink_5d |
| UEC | Uranium Energy Corp. | 8.15 | n/a | -5.40% | -15.1% | 1 | wicky_breakout, ma_shrink_5d |
| ULH | Universal Logistics Holdings, Inc. | 17.42 | +2.23% | +29.68% | +30.2% | 1 | — |
| UPBD | Upbound Group, Inc. | 19.98 | n/a | +3.60% | +3.0% | 1 | — |
| USAR | USA Rare Earth, Inc. | 10.52 | n/a | -8.56% | -29.6% | 1 | wicky_breakout, ma_shrink_5d |
| UUUU | Energy Fuels Inc | 8.23 | n/a | -6.32% | -28.1% | 1 | wicky_breakout, ma_shrink_5d |
| VCYT | Veracyte, Inc. | 52.17 | n/a | -4.14% | +12.6% | 1 | wicky_breakout |
| VERA | Vera Therapeutics, Inc. | 30.53 | n/a | +1.47% | -4.9% | 1 | — |
| VG | Venture Global, Inc. | 14.77 | n/a | +0.14% | +10.4% | 2 | — |
| VKTX | Viking Therapeutics, Inc. | 26.86 | n/a | +1.56% | -15.4% | 1 | — |
| VLTO | Veralto Corp | 104.06 | n/a | +6.77% | +10.5% | 1 | wicky_breakout, ma_shrink_5d |
| VNOM | Viper Energy, Inc. | 46.83 | n/a | +1.82% | +5.0% | 1 | wicky_breakout, ma_shrink_5d |
| VRT | Vertiv Holdings, LLC | 245.92 | n/a | -5.46% | +1.8% | 1 | — |
| VRTX | Vertex Pharmaceuticals Incorporated | 540.00 | n/a | +3.50% | +13.2% | 1 | wicky_breakout |
| VSAT | ViaSat, Inc. | 77.99 | n/a | -1.24% | +1.4% | 2 | — |
| VSEC | VSE Corporation | 155.02 | n/a | -4.64% | -20.3% | 1 | wicky_breakout |
| VSH | Vishay Intertechnology, Inc. | 29.43 | n/a | -9.14% | -14.0% | 1 | wicky_breakout, ma_shrink_5d |
| VST | Vistra Corp. | 140.95 | n/a | -1.83% | -4.9% | 1 | wicky_breakout, ma_shrink_5d |
| VSTM | Verastem, Inc. | 9.66 | n/a | +0.93% | +66.6% | 2 | wicky_breakout, ma_shrink_5d |
| VSXY | Victorias Secret & Co. | 99.14 | n/a | -2.54% | +11.8% | 1 | — |
| VVX | V2X, Inc. | 80.52 | n/a | -0.19% | -10.8% | 1 | wicky_breakout |
| WDC | Western Digital Corporation | 395.41 | n/a | -7.41% | -27.4% | 1 | wicky_breakout |
| WELL | Welltower Inc. | 233.17 | n/a | +0.61% | -0.5% | 1 | — |
| WGS | GeneDx Holdings Corp. | 71.02 | n/a | -2.76% | +9.1% | 1 | — |
| WHR | Whirlpool Corporation | 29.35 | n/a | +2.01% | -21.7% | 1 | — |
| WING | Wingstop Inc. | 145.39 | n/a | +2.99% | +12.3% | 1 | — |
| WIX | Wix.com Ltd. | 78.06 | n/a | -1.27% | +41.8% | 1 | wicky_breakout |
| WOLF | Wolfspeed, Inc. | 24.95 | -6.34% | -11.90% | +5.6% | 1 | ma_shrink_5d |
| WRBY | Warby Parker Inc. | 24.59 | n/a | +0.08% | -7.9% | 1 | wicky_breakout, ma_shrink_5d |
| WT | WisdomTree, Inc. | 21.55 | n/a | -3.90% | +11.3% | 1 | wicky_breakout, ma_shrink_5d |
| WTM | White Mountains Insurance Group, Ltd. | 2245.46 | n/a | +1.09% | +7.0% | 1 | wicky_breakout, ma_shrink_5d |
| WULF | TeraWulf Inc. | 12.75 | n/a | -8.00% | -27.8% | 2 | wicky_breakout, ma_shrink_5d |
| XE | X-Energy, Inc. | 11.70 | n/a | -6.58% | -28.3% | 1 | atr_shrink, ma_shrink_5d |
| XMTR | Xometry, Inc. | 100.82 | n/a | -7.11% | +17.6% | 1 | — |
| XOM | ExxonMobil Holdings Corporation | 183.29 | n/a | +2.16% | +17.9% | 1 | wicky_breakout, ma_shrink_5d |
| XP | XP Inc. | 15.05 | n/a | -5.05% | -11.8% | 1 | — |
| ZETA | Zeta Global Holdings Corp. | 32.74 | n/a | -4.80% | +51.6% | 1 | — |
| ZION | Zions Bancorporation N.A. | 66.23 | n/a | -1.30% | -5.0% | 1 | wicky_breakout, ma_shrink_5d |
| ZS | Zscaler, Inc. | 247.82 | n/a | -4.03% | +63.9% | 2 | ma_shrink_5d |
