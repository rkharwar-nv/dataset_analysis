# 2. Brazilian E-Commerce Public Dataset by Olist

- **Link**: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- **License**: CC BY-NC-SA 4.0 (non-commercial, share-alike, attribution required)
- **Sample in this repo**: None — license forbids redistribution to a permissive-licensed public repo. Use [`scripts/fetch_samples.py`](../scripts/fetch_samples.py).

## From the dataset (paraphrased from Olist's Kaggle page)
> Information of 100K orders from 2016 to 2018 made at multiple marketplaces in Brazil. Lets you view an order from order status, price, payment and freight performance to customer location, product attributes, and reviews written by customers.

## Files (verbatim, 9 CSVs)
| File | What it contains |
|---|---|
| `olist_orders_dataset.csv` | Core orders table — status, timestamps, customer_id |
| `olist_order_items_dataset.csv` | Line items, prices, freight per item |
| `olist_order_payments_dataset.csv` | Payment type (credit/boleto/voucher), installments, value |
| `olist_order_reviews_dataset.csv` | Review scores (1–5), titles, comments |
| `olist_customers_dataset.csv` | Customer ID + unique customer_unique_id + zip |
| `olist_products_dataset.csv` | Product attributes (size, weight, photo count, description length) |
| `olist_sellers_dataset.csv` | Seller location + ID |
| `olist_geolocation_dataset.csv` | Brazilian zip codes → lat/lng |
| `product_category_name_translation.csv` | Portuguese → English category names |

## Scale *(from Olist documentation)*
- ~100K unique orders, ~99K customers, ~3K sellers, ~32K products, 71 product categories.
- Time period: Sep 2016 – Oct 2018.

## Representative sample row *(General knowledge — schema-faithful illustrative example)*
```
order_id: e481f51cbdc54678b7cc49136f2d6af7
customer_id: 9ef432eb6251297304e76186b10a928d  (in São Paulo, zip prefix 14409)
order_status: delivered
order_purchase_timestamp: 2017-10-02 10:56:33
order_estimated_delivery_date: 2017-10-18
order_delivered_customer_date: 2017-10-10
order_items: 2 (seller=df560393, freight R$ 13.29, price R$ 49.90 each)
payment_type: credit_card  installments: 3  payment_value: R$ 113.09
review_score: 5  review_comment: "Produto chegou antes do prazo!"
```

## Common analyses *(General knowledge)*
1. **Delivery SLA & NPS link** — join `orders` × `order_reviews` on `order_id`; correlate delivery-vs-estimate gap with review_score. This is the canonical "logistics impact on satisfaction" study.
2. **Seller scorecards** — aggregate review scores, cancellation rate, and on-time delivery per seller_id. Identify the long-tail of underperforming sellers driving complaints.
3. **Marketplace mix & basket size** — orders with multiple sellers vs single-seller; freight cost as % of order value.
4. **Geographic demand maps** — zip → lat/lng table lets you produce demand heat maps by metro area.
5. **Payment-method retention** — boleto users (Brazilian bank slip) vs credit-card users — different repurchase patterns.
6. **NLP on Portuguese reviews** — fine-tune a multilingual sentiment model; extract aspect-based complaints ("amassado", "atrasou").
7. **Category translation** — the `product_category_name_translation` table maps Portuguese category names to English.

## Gotchas
- `customer_id` is **per-order**; the stable identifier is `customer_unique_id`. Joining wrong = wrong CLV.
- ~10% of orders never reach `delivered` — filter status appropriately for revenue analysis.
- Reviews can be submitted multiple times per order — dedupe by latest review_creation_date.
