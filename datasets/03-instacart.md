# 3. Instacart Online Grocery Basket Analysis

- **Link**: https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset (mirror) / https://www.kaggle.com/c/instacart-market-basket-analysis (original competition)
- **License**: Instacart Open Dataset License — non-commercial, no redistribution
- **Sample in this repo**: None — license forbids redistribution. Use [`scripts/fetch_samples.py`](../scripts/fetch_samples.py).

## From the dataset (paraphrased from Instacart's release announcement)
> Anonymized data on 3+ million grocery orders from 200K+ Instacart users. Released to support research on consumer behavior, market basket analysis, and recommender systems.

## Files
| File | Key columns |
|---|---|
| `orders.csv` | order_id, user_id, eval_set ("prior"/"train"/"test"), order_number, order_dow (day-of-week), order_hour_of_day, days_since_prior_order |
| `order_products__prior.csv` | order_id, product_id, add_to_cart_order, reordered |
| `order_products__train.csv` | same schema, for the user's most recent order |
| `products.csv` | product_id, product_name, aisle_id, department_id |
| `aisles.csv` | aisle_id, aisle (134 aisles) |
| `departments.csv` | department_id, department (21 departments) |

## Scale *(from Instacart documentation)*
- ~3.4M orders, ~206K users, ~50K products, 134 aisles, 21 departments.
- Each user has 4–100 prior orders.

## Representative sample row *(General knowledge — schema-faithful)*
```
orders.csv:
order_id=2539329  user_id=1  eval_set=prior
order_number=1  order_dow=2  order_hour_of_day=8  days_since_prior_order=NaN

order_products__prior.csv (for order 2539329):
product_id=196   add_to_cart_order=1   reordered=0   → "Soda"
product_id=14084 add_to_cart_order=2   reordered=0   → "Organic Unsweetened Vanilla Almond Milk"
product_id=12427 add_to_cart_order=3   reordered=0   → "Original Beef Jerky"
product_id=26088 add_to_cart_order=4   reordered=0   → "Aged White Cheddar Popcorn"
```

## Common analyses *(General knowledge)*
1. **Reorder prediction** — the original Kaggle competition. Predict which prior products a user will reorder in their next basket. The basis for "buy again" recommendations.
2. **Market-basket affinity** — Apriori / FP-Growth on order_products. Output: "bananas → strawberries" rules with lift/support/confidence.
3. **Day-of-week & hour-of-day demand** — order_dow + order_hour_of_day → shopper-supply forecasting. Useful for dispatch planning.
4. **Aisle / department adjacency** — if "frozen pizza" and "ice cream" co-occur in baskets, that's a freezer-section adjacency case.
5. **Repurchase cadence per category** — `days_since_prior_order` aggregated by product → expected refill interval. 
6. **New vs reorder mix** — what fraction of a typical basket is `reordered=1`? Higher = sticky user. 
7. **Cold-start product seeding** — products with low reorder rate but high `add_to_cart_order` position (top of cart) are usually "considered but abandoned" .

## Gotchas
- The dataset only contains order **composition**, no prices and no actual delivery info. Revenue / margin analysis is not possible without joining external pricing.
- `eval_set='test'` rows have no product list — they're for competition submission only.
- `days_since_prior_order` is capped at 30 (anything longer = 30).
