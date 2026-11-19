# 5. Walmart M5 Forecasting

- **Link**: https://www.kaggle.com/competitions/m5-forecasting-accuracy
- **License**: Kaggle competition rules — research/competition use only; redistribution restricted.
- **Sample in this repo**: None. Use [`scripts/fetch_samples.py`](../scripts/fetch_samples.py).

## From the dataset (paraphrased from Kaggle competition page)
> Hierarchical sales data from Walmart for ~5 years (Jan 2011 – June 2016), covering 3,049 products in 3 categories (Hobbies, Foods, Household) across 10 stores in California (4), Texas (3), and Wisconsin (3). Total: 30,490 time series.

## Files & Schema *(from M5 documentation)*
| File | Columns |
|---|---|
| `sales_train_validation.csv` / `sales_train_evaluation.csv` | `id, item_id, dept_id, cat_id, store_id, state_id, d_1…d_1941` (one column per day) |
| `sell_prices.csv` | `store_id, item_id, wm_yr_wk, sell_price` (weekly) |
| `calendar.csv` | `date, wm_yr_wk, weekday, wday, month, year, event_name_1, event_type_1, event_name_2, event_type_2, snap_CA, snap_TX, snap_WI` |
| `sample_submission.csv` | 28-day forecast format |

## Hierarchy *(from documentation)*
12 aggregation levels: Total → State → Store → Category → Department → Item × Store. The competition was scored on all 12 levels simultaneously.

## Representative sample row *(General knowledge — schema-faithful)*
```
sales_train_evaluation.csv (wide format):
id=FOODS_3_090_CA_1_evaluation  item_id=FOODS_3_090  dept_id=FOODS_3
cat_id=FOODS  store_id=CA_1  state_id=CA
d_1=2  d_2=0  d_3=0  d_4=1  d_5=4 …

calendar.csv:
date=2016-02-07  wm_yr_wk=11502  weekday=Sunday  wday=1
event_name_1=SuperBowl  event_type_1=Sporting
snap_CA=0  snap_TX=0  snap_WI=0

sell_prices.csv:
store_id=CA_1  item_id=FOODS_3_090  wm_yr_wk=11502  sell_price=2.98
```

## Common analyses *(General knowledge)*
1. **Hierarchical demand forecasting benchmark** — the de-facto public benchmark; the M5 leaderboard provides strong reference scores for new methods.
2. **Promo lift / price elasticity** — `sell_prices` weekly changes vs daily sales = clean elasticity training set per SKU.
3. **Event impact quantification** — SNAP days (food-stamp disbursement) and event_name_1 (Super Bowl, Easter, Thanksgiving) drive measurable lift. Separate baseline from event lift.
4. **Intermittent demand** — many SKUs have 0 sales on most days. Standard benchmark for Croston, TSB, ADIDA, GluonTS DeepAR.
5. **Hierarchical reconciliation** — top-down vs bottom-up vs MinT reconciliation. Determines whether forecasts are coherent across store, state, category and total levels.
6. **State-level vs national rollouts** — CA differs notably from TX and WI for many SKUs. Useful for studying regional heterogeneity in demand.

## Gotchas
- Sales are **unit sales**, not revenue. Multiply by `sell_price` (joined on wm_yr_wk) for revenue.
- Some items have `sell_price = NaN` for weeks they weren't carried in that store — those are not zeros, they're "not sold."
- The Walmart fiscal week starts **Saturday**, not Sunday — `wm_yr_wk` reflects this. Don't mix it with calendar weeks.
- The dataset ends June 2016. Newer macro events (pandemic, inflation) aren't covered.
