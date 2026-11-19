# 8. Google Analytics Sample (GA4 Obfuscated Ecommerce)

- **Link**: https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset
- **BigQuery table**: `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
- **License**: Google APIs Terms of Service; sample dataset usable via BigQuery Sandbox (no credit card).
- **Sample in this repo**: None — BigQuery-resident. Use [`scripts/fetch_samples.py`](../scripts/fetch_samples.py) to export ~10K rows.

## From the dataset (verbatim from Google Developers page)
> "A sample of obfuscated Google Analytics BigQuery event export data for three months from the Google Merchandise Store."

## Coverage *(from documentation)*
- **Time period**: 2020-11-01 → 2021-01-31 (3 months).
- **Tables**: One `events_YYYYMMDD` table per day. Wildcard table `events_*` aggregates all days.
- **Site**: Google Merchandise Store — a real e-commerce site selling Google-branded swag.

## Schema highlights *(from BigQuery export docs)*
Each row is one **event** for one user. Selected columns:

| Path | Type | Notes |
|---|---|---|
| `event_date` | str (YYYYMMDD) | |
| `event_timestamp` | int64 µs | |
| `event_name` | str | `page_view, view_item, add_to_cart, begin_checkout, purchase, …` |
| `user_pseudo_id` | str | Stable per-device ID (cookie-like) |
| `user_id` | str | Logged-in ID (often null on this dataset) |
| `device.category` | str | desktop / mobile / tablet |
| `geo.country, geo.city` | str | |
| `traffic_source.{source, medium, name}` | str | |
| `items[]` | repeated struct | `item_id, item_name, item_category, price, quantity, item_brand, item_variant` |
| `event_params[]` | repeated struct | Key-value pairs for the event |
| `ecommerce.purchase_revenue` | float | On `purchase` events |
| `session_traffic_source_last_click.*` | struct | Attribution |

## Representative sample row *(General knowledge — schema-faithful)*
```sql
-- One row from events_20201119:
event_date=20201119  event_timestamp=1605794520123456
event_name=add_to_cart
user_pseudo_id=12345.6789012345
device.category=mobile  device.operating_system=Android
geo.country=United States  geo.city=New York
traffic_source.source=google  traffic_source.medium=organic
items=[{item_id:"GGOEAFKQ020699",
        item_name:"YouTube Pullover Hoodie",
        item_category:"Apparel",
        price:55.0, quantity:1, item_brand:"YouTube"}]
```

## Common analyses *(General knowledge)*
1. **Funnel diagnostics** — `view_item → add_to_cart → begin_checkout → purchase`. Compute per-step drop-off; segment by device, traffic source, country.
2. **Channel attribution** — first-touch vs last-touch (`traffic_source` vs `session_traffic_source_last_click`). Different spend allocations follow.
3. **Search-term → revenue** — extract `q=` or search_term from event_params and join to subsequent purchases. Powers "what searches actually drive sales" reports.
4. **Cohort analysis by acquisition channel** — group users by their first-session traffic source; measure 30/60/90-day repurchase rate.
5. **Product affinity from view sequences** — co-view patterns within a session feed PDP "you may also like."
6. **Mobile vs desktop CVR gap** — almost always mobile lags; quantifying the gap on this dataset is a free benchmark.
7. **Cart abandonment** — sessions with `add_to_cart` but no `purchase` within 7 days → email/retargeting target list.

## Gotchas
- Data is **obfuscated** — some values are placeholders, internal consistency is limited. Good for learning queries; not for absolute business numbers.
- `user_id` is mostly null; rely on `user_pseudo_id` for behavior analysis (device-bound).
- Each event is a row, but `items[]` and `event_params[]` are repeated structs — you must `UNNEST` to flatten.
- The dataset stops in Jan 2021. Live GA4 exports use the same schema; revenue can be reconstructed from `ecommerce.purchase_revenue` × USD.
