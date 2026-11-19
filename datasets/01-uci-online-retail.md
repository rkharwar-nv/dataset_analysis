# 1. UCI Online Retail / Online Retail II

- **Link**: https://archive.ics.uci.edu/dataset/352/online+retail
- **License**: CC BY 4.0 (share/adapt with attribution)
- **Citation**: Chen, D. (2015). *Online Retail*. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33
- **Sample in this repo**: [`samples/uci-online-retail-sample.csv`](../samples/uci-online-retail-sample.csv) (first 500 rows)

## From the dataset (verbatim from UCI)
> "This is a transactional data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers."

## Verified by direct download (this repo's exploration)
- **Shape**: 541,909 rows × 8 columns
- **Date range**: 2010-12-01 08:26 → 2011-12-09 12:50
- **Unique invoices**: 25,900
- **Unique customers**: 4,372
- **Unique countries**: 38 (top 5: United Kingdom 495,478; Germany 9,495; France 8,557; EIRE 8,196; Spain 2,533)
- **Bestsellers**: WHITE HANGING HEART T-LIGHT HOLDER, REGENCY CAKESTAND 3 TIER, JUMBO BAG RED RETROSPOT, PARTY BUNTING, LUNCH BAG RED RETROSPOT

## Schema

| Column | Type | Notes |
|---|---|---|
| InvoiceNo | object (str) | 6-digit invoice ID; if starts with 'C', it's a cancellation |
| StockCode | object (str) | Product code (5-digit + optional letter suffix) |
| Description | object (str) | Free-text product name (uppercase) |
| Quantity | int64 | Can be negative (returns) |
| InvoiceDate | datetime | Per-line timestamp |
| UnitPrice | float64 | GBP |
| CustomerID | float64 | ~25% null (guest/anonymous baskets) |
| Country | str | Customer country of residence |

## Real sample rows (verbatim from the downloaded file)
```
InvoiceNo  StockCode  Description                          Quantity  InvoiceDate           UnitPrice  CustomerID  Country
536365     85123A     WHITE HANGING HEART T-LIGHT HOLDER   6         2010-12-01 08:26:00   2.55       17850.0     United Kingdom
536365     71053      WHITE METAL LANTERN                  6         2010-12-01 08:26:00   3.39       17850.0     United Kingdom
536365     84406B     CREAM CUPID HEARTS COAT HANGER       8         2010-12-01 08:26:00   2.75       17850.0     United Kingdom
536365     84029G     KNITTED UNION FLAG HOT WATER BOTTLE  6         2010-12-01 08:26:00   3.39       17850.0     United Kingdom
536365     84029E     RED WOOLLY HOTTIE WHITE HEART.       6         2010-12-01 08:26:00   3.39       17850.0     United Kingdom
```

## Common analyses *(General knowledge)*
1. **Customer segmentation (RFM)** — Recency, Frequency, Monetary value model. Then map to loyalty tiers, retention campaigns.
2. **Customer Lifetime Value (CLV)** — fit BG/NBD + Gamma-Gamma models. Classic teaching dataset for probabilistic CLV.
3. **Returns / cancellations analysis** — invoices starting with `C` and negative `Quantity`. Used to estimate return rates and find products with abnormally high return rates.
4. **Cohort retention curves** — group by acquisition month, track repurchase rate over 12 months.
5. **Geographic expansion** — UK is 91% of rows. The international long tail (Germany, France, Ireland) supports cross-country demand comparisons.
6. **Product affinity** — co-purchased SKUs within an invoice → starter for "frequently bought together" rules.
7. **Wholesale vs retail signal** — Quantity > 10 or InvoiceNo total > £200 are common heuristics to find wholesale baskets.

## Gotchas
- ~25% of rows have null `CustomerID` — drop or treat as anonymous separately.
- The Online Retail **II** dataset extends coverage to 2009-12-01 and is preferred for newer studies.
- A few `UnitPrice` values are negative (adjustments). Filter `Quantity > 0` and `UnitPrice > 0` for "clean" revenue.
