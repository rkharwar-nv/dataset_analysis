# 9. US Census Monthly Retail Trade Survey (MRTS / MARTS / ARTS / MSRS)

- **Link**: https://www.census.gov/retail/
- **License**: US Public Domain — free reuse.
- **Sample in this repo**: [`samples/census-marts-apr2026.xlsx`](../samples/census-marts-apr2026.xlsx) — single-month snapshot of the April 2026 advance release (not the full MRTS history).

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

## Retail NAICS codes
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

## Common analyses *(General knowledge)*
1. **Macro benchmark for category growth** — industry YoY growth by NAICS code (e.g. 4541, electronic shopping) serves as a reference for any firm-level series.
2. **Channel-mix narrative** — quarterly e-commerce share trend. Tracks e-commerce as a share of total US retail.
3. **State-level demand sizing** — MSRS gives state-level retail sales for regional market sizing.
4. **Macro shock detection** — sudden inflection in a NAICS series often precedes private-data trend shifts by 30–60 days.
5. **Forecast anchor** — category-level growth provides a top-down check for bottom-up SKU forecasts.
6. **Citable public data** — government-issued and public domain, with no licensing restrictions.

## Gotchas
- MARTS is **advance** = subject to revision; the MRTS final number lands a month later. Advance estimates are revised.
- Seasonally-adjusted vs not-adjusted: use SA for trend analysis, NSA for comparisons against other unadjusted series.
- E-commerce definition is NAICS 4541 + electronic portions of other NAICS, NOT just `e-commerce_only_stores`. The methodology note matters.
- April 2026 release shown here is the **advance**; the `(p)` and `(r)` flags indicate preliminary/revised statuses.
