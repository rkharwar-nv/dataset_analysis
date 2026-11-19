# 7. Dunnhumby — The Complete Journey (and siblings)

- **Link**: https://www.dunnhumby.com/source-files/
- **License**: Dunnhumby Source Files Terms of Use — academic / non-commercial; access via registration.
- **Sample in this repo**: None. Users register and download themselves.

## From the dataset (verbatim from dunnhumby.com/source-files)
> "(Nearly) Real-world data for data enthusiasts, academics, and professionals to practice analytics techniques."

Four datasets are offered; **The Complete Journey** is the flagship:

| Dataset | Type | Content |
|---|---|---|
| **The Complete Journey** | Relational | Household-level transactions over 2 years for 2,500 frequent-shopper households. Includes direct marketing contact history and demographics. All categories. |
| Breakfast at the Frat | Time series | 156 weeks of sales for 5 products across 4 categories (mouthwash, pretzels, pizza, cereal). Unit sales, base price, shelf price, promo details. |
| Carbo-Loading | Relational | 2 years of household transactions in 4 categories (pasta, sauce, syrup, pancake mix). |
| Let's Get Sort-of-Real | Dummy | 117 weeks, 300M transactions, ~500K customers, ~5K products. |

## The Complete Journey — tables *(from documentation)*
- `transaction_data` — `household_key, BASKET_ID, DAY, PRODUCT_ID, QUANTITY, SALES_VALUE, STORE_ID, RETAIL_DISC, TRANS_TIME, WEEK_NO, COUPON_DISC, COUPON_MATCH_DISC`
- `hh_demographic` — household age, marital status, income bracket, household composition, kid category
- `product` — `PRODUCT_ID, DEPARTMENT, COMMODITY_DESC, SUB_COMMODITY_DESC, MANUFACTURER, BRAND, CURR_SIZE_OF_PRODUCT`
- `campaign_desc` — campaign date ranges
- `campaign_table` — which household received which campaign
- `coupon` — which products each coupon was valid for
- `coupon_redempt` — which coupons each household redeemed
- `causal_data` — when a product was on display / in mailer at a given store/week

## Representative sample row *(General knowledge — schema-faithful)*
```
transaction_data:
household_key=24  BASKET_ID=2659...  DAY=540
PRODUCT_ID=1027524  QUANTITY=2  SALES_VALUE=4.50
STORE_ID=32  RETAIL_DISC=-0.50  COUPON_DISC=-1.00
COUPON_MATCH_DISC=0  TRANS_TIME=1422  WEEK_NO=78

hh_demographic:
household_key=24  AGE_DESC="35-44"  MARITAL_STATUS_CODE=A
INCOME_DESC="50-74K"  HH_COMP_DESC="2 Adults Kids"
KID_CATEGORY_DESC="1"

product:
PRODUCT_ID=1027524  DEPARTMENT=KIOSK-GAS  COMMODITY_DESC=DIAPERS
SUB_COMMODITY_DESC=DIAPER  MANUFACTURER=...  BRAND="HUGGIES"
```

## Common analyses *(General knowledge)*
1. **True promo incrementality** — `causal_data` tells you when a product was on display or in a mailer. Difference-in-differences vs non-displayed periods gives clean incremental lift, not just promo-week sales.
2. **Coupon targeting effectiveness** — `campaign_table` × `coupon_redempt` → redemption rate by campaign type, by demographic.
3. **Household CLV with demographics** — most public retail datasets have no demographics. Here you can build CLV stratified by income, kids-at-home, life stage.
4. **Category role** — destination (toilet paper), routine (milk), occasional (decoration), seasonal. Aggregate purchase frequency and basket attachment per category.
5. **Coupon stacking & forward-buy detection** — high `COUPON_MATCH_DISC` baskets often signal stockpiling. Useful for inventory-impact modeling.
6. **Channel-of-acquisition × LTV** — link `campaign_desc` → first-purchase → 2yr CLV by acquisition campaign.
7. **Private-label affinity** — `BRAND="Private"` flag (when present in product table) lets you study which households trade up to private-label and which trade down to it.

## Gotchas
- "Day" is an integer offset from a baseline, **not a real date**. You can't join with macro data unless you anchor day=1.
- 2,500 households is small. Model variance is high; report confidence intervals.
- The Complete Journey is from a single US grocer — assortment generalization to mass merch (Walmart, Target) is weak.
- "Big Data" framing on the Dunnhumby page is dated; The Complete Journey is ~250MB, fits in memory.
