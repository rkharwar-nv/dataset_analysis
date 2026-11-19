# 11. Retail Transactions Dataset (Synthetic, Kaggle)

- **Link**: https://www.kaggle.com/datasets/prasad22/retail-transactions-dataset
- **License**: CC0 1.0 (public domain)
- **Sample in this repo**: None committed (synthetic, easily regenerated). Use [`scripts/fetch_samples.py`](../scripts/fetch_samples.py).

## From the dataset (paraphrased from Kaggle page)
> A synthetic retail transactions dataset tailored for **market basket analysis, customer segmentation, and other retail analytics tasks**.

## Why it exists
Real retail data is hard to get without licensing entanglements. This dataset is **machine-generated** to mimic the structure of real transactions, with realistic but **fictitious** customer IDs, product names, prices, and timestamps. Perfect for prototyping, interviews, demos, and training.

## Schema *(from Kaggle page)*
| Column | Type | Notes |
|---|---|---|
| Transaction_ID | int | Unique per transaction |
| Date | date | YYYY-MM-DD |
| Customer_Name | str | Synthetic |
| Product | list / str | Items in the basket (sometimes comma-separated) |
| Total_Items | int | |
| Total_Cost | float | |
| Payment_Method | str | Cash, Credit Card, Debit Card, etc. |
| City | str | |
| Store_Type | str | Online, Department, Grocery, Convenience, etc. |
| Discount_Applied | bool | |
| Customer_Category | str | Senior, Adult, etc. |
| Season | str | Spring/Summer/Fall/Winter |
| Promotion | str | BOGO, "Discount on Selected Items", etc. |

## Scale
- ~1M synthetic transactions across multiple cities and store types.

## Representative sample row *(General knowledge — schema-faithful)*
```
Transaction_ID=1001  Date=2024-03-12  Customer_Name="Jane Smith"
Product=["bread","jam","butter"]  Total_Items=3  Total_Cost=14.20
Payment_Method="Credit Card"  City="Chicago"  Store_Type="Grocery"
Discount_Applied=True  Customer_Category="Adult"
Season="Spring"  Promotion="Discount on Selected Items"
```

## Common analyses *(General knowledge)*
1. **Prototype dashboards** — build Tableau / Looker / Streamlit demos with zero PII exposure.
2. **Teaching and practice** — a clean dataset for SQL/Python exercises.
3. **Stand-in data** — placeholder data for testing BI tools and pipelines before real data is available.
4. **Market-basket exercises** — the `Product` field is list-shaped, designed for Apriori / FP-Growth practice.
5. **Demo segmentation models** — `Customer_Category` provides ground-truth labels to demonstrate accuracy.

## Gotchas
- **Synthetic** means: no real correlations, no real seasonality, no real customer journeys. Models that "work" on this dataset don't necessarily generalize.
- Insights derived from this data are **not** real consumer behavior — they should not be reported as such.
- The `Product` column is sometimes a Python list string `"['a','b','c']"` rather than properly-formatted JSON. Parse defensively.
- Date range / promotional logic is internally inconsistent (the generator doesn't model promo response).
