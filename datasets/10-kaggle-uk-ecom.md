# 10. Kaggle E-Commerce Data (UK retailer — CC0 mirror of UCI Online Retail)

- **Link**: https://www.kaggle.com/datasets/carrie1/ecommerce-data
- **License**: CC0 1.0 (public domain)
- **Sample in this repo**: See [`samples/uci-online-retail-sample.csv`](../samples/uci-online-retail-sample.csv) — same data, slightly different format.

## What this is
This is functionally the same file as [UCI Online Retail](01-uci-online-retail.md), re-hosted on Kaggle under the **CC0** (public domain) license. The data content is identical to the UCI version; the only meaningful difference is the license.

## Why have it as a separate entry
- **License clarity**: CC0 = no attribution needed, can be embedded in any commercial product without restriction. Pick this over the UCI mirror for any internal product feature or customer-facing demo.
- **Kaggle ecosystem**: Hundreds of public notebooks already analyze this file. Useful for learning what others have done.

## Files
- `data.csv` — single CSV, UTF-8 with BOM, 541,909 rows × 8 columns.

## Schema (identical to UCI)
| Column | Type | Notes |
|---|---|---|
| InvoiceNo | str | Cancellations start with 'C' |
| StockCode | str | |
| Description | str | Uppercase, sometimes blank |
| Quantity | int | Can be negative (returns) |
| InvoiceDate | datetime | Format: M/D/YYYY HH:MM |
| UnitPrice | float | GBP |
| CustomerID | float | ~25% missing |
| Country | str | 38 distinct |

## Representative rows
Same as UCI — see [`samples/uci-online-retail-sample.csv`](../samples/uci-online-retail-sample.csv) for 500 real rows.

## How a Retail PM uses this *(General knowledge)*
Same use cases as UCI (RFM, CLV, returns, cohort, geo expansion, affinity, wholesale detection).

**Additional use case unique to the CC0 version**:
- **Embed in product demos / public dashboards** — license-clean for internal tools, customer demos, sales-engineering examples. No "do not redistribute" footnotes required.

## Gotchas
- Some Kaggle uploads of this file have data-quality fixes baked in (price 0 rows removed, NULL CustomerID dropped). Read the version's README before claiming "1M rows."
- File is CSV; date parsing varies — set `dayfirst=False` and `dtype={'InvoiceNo': str, 'StockCode': str}` when loading.
- The "Carrie1" upload (most popular mirror) is missing the explicit description sheet that comes with the UCI .xlsx — fewer metadata clues for first-time readers.
