# Scorecard 3 — Promotional Effectiveness

> Metrics for whether discounts and campaigns generate **incremental** profit, not just sales-shift.

## Source datasets
- [Dunnhumby Complete Journey](../datasets/07-dunnhumby.md) — gold standard, has `causal_data` for display/mailer
- [Walmart M5](../datasets/05-walmart-m5.md) — `sell_prices` + calendar events
- [Olist Brazilian](../datasets/02-olist-brazilian.md) — payment installments as a soft promo lever

## Metrics

| Metric | Formula | Target | Cadence |
|---|---|---|---|
| **Promo lift** | (sales during promo − baseline) / baseline | >20% per campaign | Per campaign |
| **Incrementality** | lift adjusted for forward-buy & cannibalization | >50% of headline lift | Per campaign |
| **Promo ROI** | (incremental margin − promo cost) / promo cost | >0 (positive) | Per campaign |
| **Cannibalization rate** | % of promo sales pulled from full-price SKUs | <30% | Per campaign |
| **Forward-buy rate** | % of promo sales that pulled demand from future | <40% | 4w post-campaign |
| **Promo penetration** | % of total revenue sold at any discount | 25–45% (depends on category) | Monthly |
| **Discount depth** | avg (1 − sell_price / list_price) | varies; track YoY drift | Monthly |
| **Margin-after-promo** | gross margin including promo discounts | flat or up YoY | Monthly |

## Baseline definition

Three common baseline methods, in order of rigor:

1. **Same period prior year** — simple, ignores trend.
2. **Synthetic control** — weighted average of non-promoted comparable SKUs (preferred).
3. **Causal inference** (CausalImpact, DiD, uplift modeling) — best when promotion eligibility is randomized.

Dunnhumby's `causal_data` table is built for method #3: it has explicit display/mailer flags by store/week.

## SQL skeleton (using Dunnhumby)

```sql
-- True incremental lift via display flag
WITH base AS (
  SELECT t.PRODUCT_ID, t.STORE_ID, t.WEEK_NO,
         SUM(t.SALES_VALUE)       AS revenue,
         SUM(t.QUANTITY)          AS units,
         MAX(c.display)           AS on_display,
         MAX(c.mailer)            AS in_mailer
  FROM transaction_data t
  LEFT JOIN causal_data c
    ON t.PRODUCT_ID = c.PRODUCT_ID
   AND t.STORE_ID   = c.STORE_ID
   AND t.WEEK_NO    = c.WEEK_NO
  GROUP BY 1,2,3
)
SELECT
  PRODUCT_ID,
  AVG(CASE WHEN on_display = 1 THEN units END) AS units_with_display,
  AVG(CASE WHEN on_display = 0 THEN units END) AS units_no_display,
  AVG(CASE WHEN on_display = 1 THEN units END)
    / NULLIF(AVG(CASE WHEN on_display = 0 THEN units END), 0) - 1 AS display_lift
FROM base
GROUP BY PRODUCT_ID
HAVING COUNT(*) >= 20;
```

## Questions these metrics answer

1. Which **campaigns ROI-positive** after incrementality adjustment?
2. What's our **forward-buy rate** on top-promoted SKUs — are we stockpiling-trained our customers?
3. Is **promo penetration** drifting up YoY? (Rising penetration indicates growing dependence on discounts.)
4. Which **categories have the highest cannibalization** — those are candidates for promo reduction.
5. Are we measuring **margin-after-promo** correctly, or just gross revenue?

## Pitfalls
- Reporting "lift" without baseline definition is meaningless — always state the baseline method.
- Treating BOGO as "50% off" — economically true, but customers respond differently.
- Ignoring **stockpiling**: a 4-week lift followed by a 4-week dip is zero net.
- Forgetting **cross-channel cannibalization** — online promo pulling from store, or vice versa.
- Confusing **promo effectiveness** (sales metric) with **promo profitability** (margin metric). Always run both.
