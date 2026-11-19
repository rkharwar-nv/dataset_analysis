# Scorecard 2 — Delivery SLA & Logistics Quality

> Metrics for whether deliveries arrive within the promised window.

## Source datasets
- [Olist Brazilian](../datasets/02-olist-brazilian.md) — best example with estimated vs actual delivery + reviews
- [GA4 Sample](../datasets/08-ga4-sample.md) — for order-tracking page engagement
- Internal WMS/TMS — first-party fulfillment data

## Metrics

| Metric | Formula | Target | Frequency |
|---|---|---|---|
| **On-time delivery rate** | % of orders `delivered_date ≤ estimated_date` | ≥95% | Daily |
| **Early delivery rate** | % of orders delivered ≥2d early | 30–50% (cushion) | Weekly |
| **Late delivery rate** | % delivered ≥1d late | <5% | Daily |
| **Avg delivery delta** | mean(`delivered_date − estimated_date`) days | ≤0 (early on avg) | Weekly |
| **Promise accuracy** | StdDev of delivery delta | Decreasing over time | Monthly |
| **NPS / review impact** | mean review_score on on-time vs late orders | Gap <0.5 stars | Monthly |
| **Lost / undelivered rate** | % of orders never reaching `delivered` | <0.5% | Weekly |
| **Returns-due-to-damage** | % of returns flagged "damaged in transit" | <1% | Monthly |

## Tiered SLA targets

SLAs are typically set per **shipping option**:

| Shipping option | Promise window | Target on-time |
|---|---|---|
| Same-day | by 9pm same day | 99% |
| Next-day | by 8pm next day | 98% |
| Standard (2–5d) | within 5 business days | 95% |
| Economy (7–10d) | within 10 business days | 92% |
| International | within 21 days | 85% |

## SQL skeleton (using Olist)

```sql
SELECT
  COUNT(*) AS orders,
  AVG(DATE_DIFF(order_delivered_customer_date,
                order_estimated_delivery_date, DAY))  AS avg_delta_days,
  AVG(CASE WHEN order_delivered_customer_date
              <= order_estimated_delivery_date THEN 1.0 ELSE 0 END) AS on_time_rate,
  AVG(CASE WHEN order_status = 'delivered' THEN 1.0 ELSE 0 END)     AS delivered_rate,
  AVG(review_score) AS avg_review_score
FROM olist_orders o
LEFT JOIN olist_order_reviews r USING (order_id)
WHERE order_status IN ('delivered','canceled','unavailable');
```

## Questions these metrics answer

1. Where are **late deliveries** concentrated — region? Seller? Carrier?
2. Is **review score on late deliveries** dragging overall NPS?
3. Are we **over-promising** in any zone (promise window too tight) or **under-promising** (cushioning too much, losing conversions)?
4. Which **carrier** has the worst variance? Time to renegotiate?
5. Do **damaged-return** flags cluster on a specific warehouse?

## Pitfalls
- Comparing **calendar-day** to **business-day** SLAs (always normalize).
- Forgetting **carrier handoff time** when attributing late deliveries — sometimes it's the warehouse, not the carrier.
- Using **median** instead of **p95** — long-tail late deliveries don't move the median much but kill NPS.
- Ignoring **return delivery** SLA — customers care about how fast their refund-eligible item moves back too.
