# Scorecard 1 — Customer Health (RFM + CLV)

> Measures whether your customer base is growing in value over time.

## Source datasets
- [UCI Online Retail](../datasets/01-uci-online-retail.md) — best starting point
- [Olist Brazilian](../datasets/02-olist-brazilian.md) — adds review_score for satisfaction overlay
- [Dunnhumby Complete Journey](../datasets/07-dunnhumby.md) — adds demographics

## Metrics

| Metric | Formula | What good looks like | Frequency |
|---|---|---|---|
| **Recency (R)** | days since last purchase | <30d for "active" cohort | Daily |
| **Frequency (F)** | orders in last 365 days | ≥3 for engaged users | Weekly |
| **Monetary (M)** | revenue in last 365 days | Top quintile = "VIP" | Weekly |
| **CLV (12-mo)** | Σ predicted revenue next 12 months | Growing QoQ | Monthly |
| **Repeat-purchase rate** | % of cohort with 2+ orders by D90 | >30% for e-com | Weekly |
| **% active customers** | unique buyers in last 30d / unique buyers in last 90d | 60%+ | Weekly |
| **Churn (predicted)** | P(no purchase next 90d) | <25% on top quintile | Monthly |

## RFM tier definitions *(common industry standard)*

| Tier | Recency | Frequency | Monetary |
|---|---|---|---|
| **VIP / Champion** | ≤30d | ≥6/yr | Top 20% |
| **Loyal** | ≤60d | ≥3/yr | Top 50% |
| **Promising** | ≤90d | 1–2/yr | Any |
| **At-risk** | 90–180d | Was Loyal+ | Was top 50% |
| **Lost** | >180d | — | — |

## What to do with each tier

- **VIPs** → exclusive perks, early access, manual retention if score drops.
- **Loyal** → cross-sell adjacent categories, loyalty-tier upgrades.
- **Promising** → onboarding nudges, second-purchase incentive.
- **At-risk** → win-back campaign (discount + apology email).
- **Lost** → exclude from acquisition reports; suppress paid retargeting after 1 year.

## SQL skeleton (using UCI Online Retail)

```sql
WITH per_customer AS (
  SELECT
    CustomerID,
    DATE_DIFF(CURRENT_DATE, MAX(DATE(InvoiceDate)), DAY) AS recency_days,
    COUNT(DISTINCT InvoiceNo)                            AS frequency,
    SUM(Quantity * UnitPrice)                            AS monetary
  FROM online_retail
  WHERE CustomerID IS NOT NULL AND Quantity > 0
  GROUP BY CustomerID
)
SELECT
  CustomerID,
  recency_days, frequency, monetary,
  NTILE(5) OVER (ORDER BY recency_days)  AS R_quintile,
  NTILE(5) OVER (ORDER BY frequency)     AS F_quintile,
  NTILE(5) OVER (ORDER BY monetary)      AS M_quintile
FROM per_customer;
```

## Quarterly review questions for the PM

1. Is **% active customers** trending up or down?
2. Is the **VIP tier** growing or shrinking?
3. Is the **lost** tier eating share faster than acquisition replenishes?
4. Are **at-risk** win-back campaigns producing >5% recovery?
5. Is **CLV-12** flat in real terms? (Inflate-adjust before reporting growth.)

## Pitfalls
- Counting by `CustomerID` when the unique identifier is `customer_unique_id` (Olist).
- Letting one wholesale customer with 1000-unit orders skew the M quintile cutoffs.
- Using calendar quarter for cohort grouping when promo cycles drive seasonality — use signup month.
