# peoplewish — ADR%, dollar volume and 14-day velocity

20-day average daily range above 5%, 20-day average dollar volume above $50M, sorted by 14-day velocity.
This branch hit the shibui 200-row server cap, so the tail of the book is not visible.

Universe after the pre-filter (close > $3, market cap > $300M, NYSE/NASDAQ/AMEX): **175 names**.
`Stylists` counts distinct stylist lenses (not sub-screen labels). `10-29` is the move the screen had
already seen on shibui's bar; `10-30` is the settled close that followed.

| Ticker | Name | Close 10-29 | 10-29 | 10-30 | RS 3M | Stylists | Flags / note |
|---|---|---:|---:|---:|---:|---:|---|
| ABCL | AbCellera Biologics Inc. | 13.08 | n/a | -6.19% | +129.1% | 2 | wicky_breakout |
| ACHR | Archer Aviation Inc. | 4.38 | n/a | -4.11% | -5.6% | 1 | wicky_breakout |
| AI | C3.ai, Inc. | 12.17 | n/a | -2.63% | +32.6% | 1 | wicky_breakout |
| ALAB | Astera Labs, Inc. | 290.43 | n/a | -10.93% | -6.7% | 2 | wicky_breakout, ma_shrink_5d |
| ALGM | Allegro MicroSystems, Inc. | 33.03 | n/a | -7.57% | -20.4% | 1 | — |
| ALHC | Alignment Healthcare, Inc. | 8.06 | n/a | -9.80% | -45.7% | 1 | ma_shrink_5d |
| ALM | Almonty Industries Inc. | 9.30 | n/a | -6.45% | -15.9% | 1 | wicky_breakout, ma_shrink_5d |
| AMBA | Ambarella, Inc. | 64.58 | n/a | -2.26% | -24.9% | 1 | wicky_breakout |
| AMC | AMC Entertainment Holdings, Inc. | 3.08 | n/a | -0.65% | +9.2% | 1 | — |
| AMKR | Amkor Technology, Inc. | 41.21 | n/a | -4.15% | -17.4% | 1 | wicky_breakout, ma_shrink_5d |
| APLD | Applied Digital Corporation | 19.41 | n/a | -8.22% | -29.1% | 1 | wicky_breakout, ma_shrink_5d |
| ARXS | Arxis, Inc. | 54.93 | n/a | -7.48% | +1.2% | 1 | — |
| ASST | Strive, Inc. | 24.91 | n/a | -10.90% | +124.2% | 2 | — |
| ASTS | AST SpaceMobile, Inc. | 43.07 | n/a | -4.88% | -27.0% | 1 | wicky_breakout, ma_shrink_5d |
| AXTI | AXT Inc | 60.88 | n/a | -9.56% | +0.7% | 1 | ma_shrink_5d |
| BB | BlackBerry Limited | 9.19 | n/a | -8.38% | +8.1% | 2 | wicky_breakout |
| BE | Bloom Energy Corporation | 222.30 | n/a | -8.61% | +8.0% | 1 | wicky_breakout, ma_shrink_5d |
| BLLN | BillionToOne, Inc. | 114.84 | n/a | -1.32% | -17.1% | 1 | wicky_breakout |
| BMNR | BitMine Immersion Technologies, Inc. | 21.66 | n/a | -6.83% | +25.3% | 1 | wicky_breakout, ma_shrink_5d |
| BSP | Bending Spoons S.p.A. | 46.78 | n/a | -2.69% | +32.9% | 1 | wicky_breakout, ma_shrink_5d |
| BTDR | Bitdeer Technologies Group | 7.58 | -4.29% | -11.48% | -27.9% | 1 | wicky_breakout, ma_shrink_5d |
| CAI | Caris Life Sciences, Inc. | 36.14 | n/a | -5.01% | +130.6% | 2 | wicky_breakout |
| CAMT | Camtek Ltd. | 126.67 | n/a | -7.89% | -4.4% | 1 | wicky_breakout, ma_shrink_5d |
| CDNA | CareDx, Inc. | 71.52 | -0.85% | +22.22% | +63.6% | 3 | ma_shrink_5d |
| CELC | Celcuity Inc. | 69.30 | n/a | -0.25% | -19.8% | 1 | wicky_breakout, ma_shrink_5d |
| CIEN | Ciena Corporation | 349.45 | n/a | -8.22% | -7.3% | 1 | wicky_breakout, ma_shrink_5d |
| CLF | Cleveland-Cliffs Inc. | 14.26 | n/a | -0.07% | +23.8% | 2 | ma_shrink_5d |
| CLS | Celestica, Inc. | 282.75 | n/a | -6.09% | -14.7% | 1 | ma_shrink_5d |
| CLSK | CleanSpark, Inc. | 8.20 | n/a | -6.46% | -40.4% | 1 | wicky_breakout, ma_shrink_5d |
| COCO | The Vita Coco Company, Inc. | 56.27 | n/a | +3.93% | -14.7% | 1 | wicky_breakout |
| COHU | Cohu, Inc. | 53.40 | n/a | -4.89% | +11.3% | 1 | ma_shrink_5d |
| COIN | Coinbase Global, Inc. | 160.59 | n/a | -10.62% | +9.8% | 1 | wicky_breakout, ma_shrink_5d |
| CORZ | Core Scientific, Inc. | 14.43 | n/a | -8.18% | -30.4% | 1 | wicky_breakout |
| CRCL | Circle Internet Group, Inc. | 79.99 | n/a | -9.31% | +27.8% | 1 | wicky_breakout |
| CRSP | CRISPR Therapeutics AG | 54.26 | n/a | -5.23% | +13.1% | 1 | wicky_breakout |
| DAVE | Dave Inc. | 334.80 | n/a | -5.38% | -10.2% | 1 | wicky_breakout |
| DK | Delek US Holdings, Inc. | 71.10 | n/a | +3.47% | +4.8% | 1 | wicky_breakout |
| DXC | DXC Technology Company | 15.23 | n/a | -1.64% | +35.5% | 2 | wicky_breakout, ma_shrink_5d |
| ENPH | Enphase Energy, Inc. | 25.86 | n/a | -0.81% | -31.1% | 1 | — |
| ENTG | Entegris, Inc. | 160.00 | n/a | -3.51% | +34.4% | 1 | — |
| EQPT | EquipmentShare.com Inc | 18.18 | n/a | -5.50% | -3.0% | 1 | wicky_breakout, ma_shrink_5d |
| ERAS | Erasca, Inc. | 14.98 | n/a | -4.21% | -17.5% | 1 | wicky_breakout |
| FICO | Fair Isaac Corporation | 709.18 | n/a | +0.29% | -36.8% | 1 | — |
| FIGR | Figure Technology Solutions, Inc. | 23.59 | n/a | -8.52% | -5.3% | 1 | ma_shrink_5d |
| FIGS | FIGS, Inc. | 21.56 | +4.36% | -1.16% | +101.5% | 3 | wicky_breakout, ma_shrink_5d |
| FIVN | Five9, Inc. | 37.41 | n/a | -2.86% | +36.0% | 1 | wicky_breakout, ma_shrink_5d |
| FLEX | Flex Ltd. | 93.07 | n/a | -7.08% | -18.2% | 1 | ma_shrink_5d |
| FLY | Firefly Aerospace Inc. | 19.87 | n/a | -9.74% | -2.3% | 1 | wicky_breakout, ma_shrink_5d |
| FROG | JFrog Ltd. | 98.83 | n/a | -4.49% | +23.9% | 1 | wicky_breakout |
| FSLY | Fastly, Inc. | 25.64 | n/a | -9.85% | +13.2% | 1 | wicky_breakout |
| FTAI | FTAI Aviation Ltd. | 196.01 | +17.27% | -4.46% | -4.8% | 3 | — |
| GH | Guardant Health, Inc. | 185.31 | n/a | -3.51% | +14.4% | 1 | wicky_breakout |
| GLXY | Galaxy Digital Inc. | 18.13 | -5.03% | -11.75% | -13.7% | 1 | wicky_breakout |
| GMAB | Genmab A/S | 56.49 | n/a | +1.01% | +95.7% | 2 | wicky_breakout |
| GRAL | GRAIL, Inc. | 158.92 | +0.66% | -9.75% | +131.8% | 3 | wicky_breakout |
| HIMS | Hims & Hers Health, Inc. | 29.67 | n/a | -6.71% | +6.8% | 1 | wicky_breakout |
| HRI | Herc Holdings Inc. | 173.95 | n/a | -4.71% | +15.9% | 2 | — |
| HTFL | Heartflow, Inc. | 60.53 | +2.42% | -2.45% | +139.9% | 3 | ma_shrink_5d |
| HUT | Hut 8 Corp. | 66.44 | n/a | -10.60% | -38.3% | 1 | wicky_breakout, ma_shrink_5d |
| IBRX | ImmunityBio, Inc. | 8.74 | n/a | -5.15% | +21.9% | 1 | wicky_breakout, ma_shrink_5d |
| ILMN | Illumina, Inc. | 290.06 | +0.44% | -18.64% | +41.4% | 1 | wicky_breakout |
| INFQ | Infleqtion, Inc. | 9.43 | n/a | -5.83% | -4.1% | 1 | wicky_breakout, ma_shrink_5d |
| INIO | INNIO N.V. | 17.52 | n/a | -6.96% | -28.3% | 1 | — |
| IONQ | IonQ, Inc. | 31.72 | n/a | -5.30% | -13.0% | 1 | wicky_breakout, ma_shrink_5d |
| IRON | Disc Medicine, Inc. | 82.84 | n/a | -2.41% | +7.6% | 1 | wicky_breakout, ma_shrink_5d |
| JBLU | JetBlue Airways Corporation | 3.05 | n/a | -6.56% | -49.4% | 1 | ma_shrink_5d |
| JOBY | Joby Aviation, Inc. | 5.08 | n/a | -3.54% | -29.0% | 1 | wicky_breakout, ma_shrink_5d |
| KOD | Kodiak Sciences Inc | 100.40 | +3.46% | -1.22% | +141.5% | 3 | — |
| KRMN | Karman Holdings Inc. | 41.69 | n/a | -4.17% | -13.4% | 1 | — |
| KVYO | Klaviyo, Inc. Series A | 20.43 | n/a | -1.42% | +14.5% | 1 | ma_shrink_5d |
| KYMR | Kymera Therapeutics, Inc. | 122.60 | n/a | +3.29% | +18.6% | 2 | — |
| LBRT | Liberty Energy Inc. | 17.41 | n/a | -3.04% | -6.9% | 1 | wicky_breakout |
| LGN | Legence Corp. | 41.90 | n/a | -7.33% | -34.5% | 1 | ma_shrink_5d |
| LITE | Lumentum Holdings Inc. | 919.53 | n/a | -8.57% | +28.8% | 1 | — |
| LQDA | Liquidia Corporation | 44.99 | n/a | +0.16% | -46.5% | 1 | wicky_breakout, ma_shrink_5d |
| LUMN | Lumen Technologies, Inc. | 4.79 | n/a | +1.88% | -24.9% | 1 | wicky_breakout, ma_shrink_5d |
| LUNR | Intuitive Machines, Inc. | 11.68 | n/a | -8.65% | -5.3% | 1 | wicky_breakout, ma_shrink_5d |
| MANE | Veradermics, Incorporated | 143.85 | n/a | -2.89% | +37.0% | 1 | wicky_breakout, ma_shrink_5d |
| MDB | MongoDB, Inc. | 384.95 | n/a | -8.31% | +14.1% | 1 | wicky_breakout |
| MMYT | MakeMyTrip Limited | 43.00 | n/a | -0.74% | -24.5% | 1 | wicky_breakout |
| MNDY | monday.com Ltd. | 94.78 | n/a | +0.87% | +8.8% | 1 | wicky_breakout |
| MRNA | Moderna, Inc. | 222.76 | +4.01% | -0.47% | +306.3% | 3 | — |
| MRVL | Marvell Technology, Inc. | 218.34 | n/a | -10.05% | +16.4% | 2 | ma_shrink_5d |
| MSTR | Strategy Inc | 141.62 | n/a | -7.84% | +51.8% | 2 | wicky_breakout, ma_shrink_5d |
| MTRN | Materion Corporation | 239.81 | n/a | -7.45% | +13.7% | 2 | wicky_breakout, ma_shrink_5d |
| NBIS | Nebius Group N.V. | 171.99 | n/a | -10.38% | -9.7% | 1 | wicky_breakout, ma_shrink_5d |
| NESR | National Energy Services Reunited Corp | 21.43 | n/a | -0.56% | -20.5% | 1 | wicky_breakout, ma_shrink_5d |
| NET | Cloudflare, Inc. | 310.30 | n/a | -9.54% | +11.2% | 1 | ma_shrink_5d |
| NRIX | Nurix Therapeutics, Inc. | 27.12 | n/a | -1.18% | +16.8% | 1 | wicky_breakout, ma_shrink_5d |
| NTLA | Intellia Therapeutics, Inc. | 13.23 | n/a | -5.74% | +23.9% | 1 | wicky_breakout |
| NTSK | Netskope, Inc. | 26.19 | n/a | -7.22% | +108.0% | 2 | — |
| NVAX | Novavax, Inc. | 10.47 | n/a | -3.72% | +43.0% | 1 | ma_shrink_5d |
| NVTS | Navitas Semiconductor Corporation | 9.20 | n/a | -7.83% | -15.3% | 1 | wicky_breakout, ma_shrink_5d |
| NXT | Nextpower Inc. | 79.83 | n/a | -0.63% | -11.2% | 1 | — |
| OKTA | Okta, Inc. | 221.86 | n/a | -6.14% | +56.3% | 2 | — |
| ONDS | Ondas Inc | 6.88 | n/a | -8.14% | -8.1% | 2 | wicky_breakout |
| ORKA | Oruka Therapeutics, Inc. | 96.65 | n/a | +0.23% | +0.1% | 1 | wicky_breakout |
| OUST | Ouster, Inc. | 32.14 | n/a | -7.47% | -17.6% | 1 | wicky_breakout, ma_shrink_5d |
| P | Everpure, Inc. | 137.20 | -1.01% | -7.45% | +77.8% | 3 | wicky_breakout |
| PARR | Par Pacific Holdings, Inc. Common Stock | 73.31 | n/a | +4.00% | -14.8% | 1 | — |
| PBF | PBF Energy Inc. | 75.54 | n/a | +3.26% | +4.5% | 1 | — |
| PCVX | Vaxcyte, Inc. | 62.61 | n/a | -0.93% | +15.8% | 1 | wicky_breakout, ma_shrink_5d |
| PI | Impinj, Inc. | 182.55 | n/a | -1.58% | +20.6% | 1 | — |
| PL | Planet Labs PBC | 14.31 | n/a | -5.87% | -30.1% | 1 | ma_shrink_5d |
| POET | POET Technologies Inc. | 5.66 | n/a | -8.13% | -19.0% | 1 | wicky_breakout, ma_shrink_5d |
| POWL | Powell Industries, Inc. | 168.48 | n/a | -7.25% | -19.3% | 1 | ma_shrink_5d |
| PRIM | Primoris Services Corporation | 75.61 | n/a | -3.76% | -10.4% | 1 | — |
| PURR | Hyperliquid Strategies Inc | 12.29 | +23.27% | -10.41% | +97.9% | 3 | — |
| QBTS | D-Wave Quantum Inc. | 11.56 | n/a | -7.87% | -36.1% | 1 | ma_shrink_5d |
| QLYS | Qualys, Inc. | 230.29 | n/a | -2.68% | +59.1% | 2 | ma_shrink_5d |
| QNT | Quantinuum Inc. | 37.49 | n/a | -10.39% | -27.1% | 1 | wicky_breakout, ma_shrink_5d |
| QS | QuantumScape Corporation | 4.20 | n/a | -3.33% | -19.5% | 1 | wicky_breakout |
| QXO | QXO, Inc. | 11.38 | n/a | -2.99% | -14.4% | 1 | — |
| RBRK | Rubrik, Inc. | 133.63 | n/a | -7.09% | +84.7% | 2 | wicky_breakout |
| RDW | Redwire Corporation | 9.16 | n/a | -8.41% | +6.3% | 1 | ma_shrink_5d |
| RGEN | Repligen Corporation | 188.64 | n/a | -6.20% | +33.8% | 1 | wicky_breakout |
| RGTI | Rigetti Computing, Inc. | 12.06 | n/a | -6.72% | -19.3% | 1 | wicky_breakout, ma_shrink_5d |
| RIOT | Riot Platforms, Inc. | 13.74 | n/a | -6.77% | -31.9% | 1 | wicky_breakout, ma_shrink_5d |
| RKLB | Rocket Lab Corporation | 59.10 | n/a | -7.39% | -9.0% | 1 | wicky_breakout, ma_shrink_5d |
| RMBS | Rambus, Inc. | 90.99 | n/a | -6.97% | -0.0% | 1 | ma_shrink_5d |
| RNG | RingCentral, Inc. | 83.70 | n/a | -2.72% | +50.5% | 2 | wicky_breakout |
| RUN | Sunrun Inc. | 7.59 | n/a | -1.45% | -22.6% | 1 | — |
| RXRX | Recursion Pharmaceuticals, Inc. | 4.24 | n/a | -4.95% | +41.3% | 1 | wicky_breakout |
| SAIL | SailPoint, Inc. | 22.00 | n/a | -4.27% | +31.2% | 1 | — |
| SBET | Sharplink, Inc. | 7.23 | n/a | -6.78% | +18.1% | 1 | wicky_breakout, ma_shrink_5d |
| SDGR | Schrodinger, Inc. | 29.99 | n/a | -9.50% | +98.1% | 2 | wicky_breakout |
| SEDG | SolarEdge Technologies, Inc. | 30.54 | n/a | -1.59% | -25.9% | 1 | — |
| SEI | Solaris Energy Infrastructure, Inc. | 69.12 | n/a | +2.29% | +34.4% | 1 | wicky_breakout |
| SEZL | Sezzle Inc. | 133.86 | n/a | +0.74% | -13.5% | 2 | wicky_breakout |
| SIMO | Silicon Motion Technology Corporation | 227.75 | n/a | -8.39% | -10.2% | 1 | ma_shrink_5d |
| SITM | SiTime Corporation | 488.08 | n/a | -8.40% | -8.8% | 1 | wicky_breakout, ma_shrink_5d |
| SKYD | Skydance Corporation | 7.90 | n/a | +0.63% | -0.8% | 1 | wicky_breakout, ma_shrink_5d |
| SLS | SELLAS Life Sciences Group, Inc. | 10.15 | n/a | -4.68% | +1.4% | 1 | — |
| SMCI | Super Micro Computer, Inc. | 34.43 | n/a | -4.30% | +21.2% | 2 | wicky_breakout, ma_shrink_5d |
| SMMT | Summit Therapeutics Inc. | 16.20 | n/a | -1.05% | +24.4% | 1 | — |
| SMR | NuScale Power Corporation | 5.92 | n/a | -5.07% | -29.7% | 1 | ma_shrink_5d |
| SNAP | Snap Inc. | 5.68 | n/a | -5.99% | +21.1% | 2 | wicky_breakout |
| SNDK | Sandisk Corporation | 1330.05 | -5.32% | -13.47% | +9.5% | 1 | ma_shrink_5d |
| SPHR | Sphere Entertainment Co. | 113.10 | n/a | -3.50% | -21.0% | 1 | ma_shrink_5d |
| STX | Seagate Technology Holdings PLC | 700.47 | n/a | -7.98% | -18.2% | 2 | wicky_breakout, ma_shrink_5d |
| SYRE | Spyre Therapeutics, Inc. | 98.96 | n/a | -2.43% | +0.6% | 1 | wicky_breakout, ma_shrink_5d |
| TEM | Tempus AI, Inc. | 77.84 | n/a | -7.22% | +77.4% | 2 | — |
| TENB | Tenable Holdings, Inc. | 51.78 | n/a | -1.99% | +58.6% | 2 | — |
| THRM | Gentherm Inc | 32.20 | n/a | -3.88% | -20.7% | 1 | — |
| TLN | Talen Energy Corporation | 348.85 | n/a | -1.64% | +4.4% | 1 | wicky_breakout |
| TNGX | Tango Therapeutics, Inc. | 22.53 | n/a | +0.84% | -17.1% | 1 | wicky_breakout |
| TSEM | Tower Semiconductor Ltd. | 187.92 | n/a | -11.41% | -14.5% | 1 | wicky_breakout, ma_shrink_5d |
| TWLO | Twilio Inc. | 241.90 | -4.68% | -15.24% | +22.6% | 1 | wicky_breakout, ma_shrink_5d |
| TWST | Twist Bioscience Corporation | 173.45 | +0.00% | -11.92% | +89.5% | 2 | wicky_breakout |
| TXG | 10x Genomics, Inc. | 81.55 | -2.48% | -14.03% | +72.5% | 2 | wicky_breakout |
| UCTT | Ultra Clean Holdings, Inc. | 54.70 | n/a | -9.12% | -34.3% | 1 | ma_shrink_5d |
| UEC | Uranium Energy Corp. | 8.15 | n/a | -5.40% | -15.1% | 1 | wicky_breakout, ma_shrink_5d |
| USAR | USA Rare Earth, Inc. | 10.52 | n/a | -8.56% | -29.6% | 1 | wicky_breakout, ma_shrink_5d |
| UUUU | Energy Fuels Inc | 8.23 | n/a | -6.32% | -28.1% | 1 | wicky_breakout, ma_shrink_5d |
| VCYT | Veracyte, Inc. | 52.17 | n/a | -4.14% | +12.6% | 1 | wicky_breakout |
| VERA | Vera Therapeutics, Inc. | 30.53 | n/a | +1.47% | -4.9% | 1 | — |
| VG | Venture Global, Inc. | 14.77 | n/a | +0.14% | +10.4% | 2 | — |
| VKTX | Viking Therapeutics, Inc. | 26.86 | n/a | +1.56% | -15.4% | 1 | — |
| VSAT | ViaSat, Inc. | 77.99 | n/a | -1.24% | +1.4% | 2 | — |
| VSEC | VSE Corporation | 155.02 | n/a | -4.64% | -20.3% | 1 | wicky_breakout |
| VSH | Vishay Intertechnology, Inc. | 29.43 | n/a | -9.14% | -14.0% | 1 | wicky_breakout, ma_shrink_5d |
| VST | Vistra Corp. | 140.95 | n/a | -1.83% | -4.9% | 1 | wicky_breakout, ma_shrink_5d |
| VSTM | Verastem, Inc. | 9.66 | n/a | +0.93% | +66.6% | 2 | wicky_breakout, ma_shrink_5d |
| VSXY | Victorias Secret & Co. | 99.14 | n/a | -2.54% | +11.8% | 1 | — |
| WDC | Western Digital Corporation | 395.41 | n/a | -7.41% | -27.4% | 1 | wicky_breakout |
| WGS | GeneDx Holdings Corp. | 71.02 | n/a | -2.76% | +9.1% | 1 | — |
| WHR | Whirlpool Corporation | 29.35 | n/a | +2.01% | -21.7% | 1 | — |
| WING | Wingstop Inc. | 145.39 | n/a | +2.99% | +12.3% | 1 | — |
| WIX | Wix.com Ltd. | 78.06 | n/a | -1.27% | +41.8% | 1 | wicky_breakout |
| WOLF | Wolfspeed, Inc. | 24.95 | -6.34% | -11.90% | +5.6% | 1 | ma_shrink_5d |
| WRBY | Warby Parker Inc. | 24.59 | n/a | +0.08% | -7.9% | 1 | wicky_breakout, ma_shrink_5d |
| WULF | TeraWulf Inc. | 12.75 | n/a | -8.00% | -27.8% | 2 | wicky_breakout, ma_shrink_5d |
| XE | X-Energy, Inc. | 11.70 | n/a | -6.58% | -28.3% | 1 | atr_shrink, ma_shrink_5d |
| XMTR | Xometry, Inc. | 100.82 | n/a | -7.11% | +17.6% | 1 | — |
| ZS | Zscaler, Inc. | 247.82 | n/a | -4.03% | +63.9% | 2 | ma_shrink_5d |
