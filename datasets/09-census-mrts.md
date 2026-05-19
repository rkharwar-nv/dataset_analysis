# 9. US Census Monthly Retail Trade Survey (MRTS / MARTS / ARTS / MSRS)

- **Link**: https://www.census.gov/retail/
- **License**: US Public Domain — free reuse.
- **Sample in this repo**: [`samples/census-marts-apr2026.xlsx`](../samples/census-marts-apr2026.xlsx) — full April 2026 advance release.

## Data products *(verbatim from census.gov/retail)*
| Product | Cadence | Covers |
|---|---|---|
| **MARTS** (Advance Monthly Retail Trade Survey) | Monthly | Preliminary current-month estimate of retail and food-services sales |
| **MRTS** (Monthly Retail Trade Survey) | Monthly | Final, revised monthly estimate (publishes ~6 weeks after MARTS) |
| **ARTS** (Annual Retail Trade Survey) → AIES | Annual | Annual retail statistics, now folded into the Annual Integrated Economic Survey |
| **MSRS** (Monthly State Retail Sales) | Monthly, experimental | Modeled state-level retail sales using MRTS + third-party + admin data |
| **Quarterly E-Commerce Sales Report** | Quarterly | E-commerce as share of total retail; latest cited estimate Q4 2025 = $316.1B (+1.7% QoQ) |

> "These data are widely used throughout government, academic, and business communities. The Bureau of Economic Analysis uses the estimates to calculate Gross Domestic Product." — census.gov/retail

## Verified by direct download (this repo)
The committed file `rs2604.xlsx` (April 2026 advance) contains 3 sheets:

- **Table 1**: Estimated Monthly Sales by NAICS code, in $ millions, both seasonally-adjusted and not.
- **Table 2**: % change month-over-month, year-over-year, 3-mo vs prior 3-mo.
- **Table 3**: Sampling-variability measures (CV, standard error) and historical revision sizes.

### Real data from Table 1 (April 2026 advance release, $ millions, seasonally adjusted)
```
Retail & food services, total             757,085  (Apr) vs 753,370 (Mar) vs 722,319 (Apr 2025)
Total excl. motor vehicle & parts         617,856
Total excl. gasoline stations             695,573
Total excl. motor vehicle & gasoline      …
```

## NAICS codes you'll care about as a Retail PM
| NAICS | Kind of business |
|---|---|
| 441 | Motor vehicle & parts dealers |
| 442 | Furniture & home furnishings |
| 443 | Electronics & appliance stores |
| 444 | Building material & garden equipment |
| 445 | Food & beverage stores (incl. grocery) |
| 446 | Health & personal care stores |
| 447 | Gasoline stations |
| 448 | Clothing & clothing accessories |
| 451 | Sporting goods, hobby, book |
| 452 | General merchandise (incl. warehouse clubs, supercenters) |
| 454 | Nonstore retailers (e-commerce) |
| 722 | Food services & drinking places |

## How a Retail PM uses this *(General knowledge)*
1. **Macro benchmark for category growth** — your business's YoY in NAICS 4541 (electronic shopping) vs the industry. If industry is +6% and you're +2%, you're losing share.
2. **Channel-mix narrative** — quarterly e-commerce share trend. Powers exec slides like "e-commerce is now X% of US retail."
3. **State-level demand sizing** — MSRS gives state-level retail sales for new-market expansion business cases.
4. **Macro shock detection** — sudden inflection in a NAICS series often precedes private-data trend shifts by 30–60 days.
5. **Forecast anchor** — if your bottom-up SKU forecast doesn't reconcile with Census category growth, one of them is wrong.
6. **Credible exec data** — public, citable, government-issued. Drops cleanly into board decks with no licensing concerns.

## Gotchas
- MARTS is **advance** = subject to revision; the MRTS final number lands a month later. Don't anchor major decisions on MARTS alone.
- Seasonally-adjusted vs not-adjusted: use SA for trend analysis, NSA for "actual dollars I should compare to my own NSA reports."
- E-commerce definition is NAICS 4541 + electronic portions of other NAICS, NOT just `e-commerce_only_stores`. The methodology note matters.
- April 2026 release shown here is the **advance**; the `(p)` and `(r)` flags indicate preliminary/revised statuses.
