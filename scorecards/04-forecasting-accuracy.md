# Scorecard 4 — Forecasting Accuracy

> Measures whether your demand forecasts are good enough to plan inventory, staffing, and promotions.

## Source datasets
- [Walmart M5](../datasets/05-walmart-m5.md) — primary benchmark
- [US Census MRTS](../datasets/09-census-mrts.md) — macro anchor for category-level forecasts
- [UCI Online Retail](../datasets/01-uci-online-retail.md) — entry-level practice

## Metrics

| Metric | Formula | Good range | When to use |
|---|---|---|---|
| **MAPE** (Mean Absolute Percent Error) | mean(|actual − pred| / |actual|) | <10% category, <30% SKU | Smooth, non-zero series |
| **WAPE** (Weighted APE) | Σ|actual − pred| / Σ|actual| | <15% blended | Mix of high/low sellers |
| **SMAPE** | 2·mean(|a−p| / (|a|+|p|)) | <20% | Intermittent demand |
| **RMSE** | sqrt(mean((actual − pred)²)) | unit-scale; trend over time | Volume comparisons |
| **MASE** | MAE / naive-1-MAE | <1 means beats naive | Comparing across series |
| **Bias / MPE** | mean(pred − actual) / mean(actual) | ±2% | Detect systematic over/under |
| **Forecast value-add (FVA)** | improvement over statistical baseline | >0% | Justify model investment |
| **Hit rate** | % of SKUs within ±15% of actual | >60% | Service-level conversations |
| **WMAPE by hierarchy level** | WAPE at total → cat → store → SKU | tightens at higher levels | Hierarchical models |

## Forecast horizon targets

| Horizon | Typical use | MAPE target (food/grocery) |
|---|---|---|
| 1 day | replenishment, staffing | 8–12% |
| 1 week | promotion planning | 10–15% |
| 4 weeks | inventory buy | 15–20% |
| 13 weeks | category planning | 20–25% |
| 52 weeks | strategy, capex | 25–35% |

## Python skeleton (using M5)

```python
import numpy as np
import pandas as pd

def wape(actual, pred):
    return np.abs(actual - pred).sum() / np.abs(actual).sum()

def mase(actual, pred, train_actual):
    naive_error = np.abs(np.diff(train_actual)).mean()
    forecast_error = np.abs(actual - pred).mean()
    return forecast_error / naive_error

# Compute hierarchical WAPE
hierarchy = ['total','state_id','store_id','cat_id','dept_id','item_id']
results = {}
for level in hierarchy:
    agg_actual = df.groupby(level)['actual'].sum()
    agg_pred   = df.groupby(level)['pred'].sum()
    results[level] = wape(agg_actual, agg_pred)
```

## Quarterly review questions

1. Is **WAPE trending down** quarter over quarter? If flat, model investment isn't paying off.
2. Where is **bias non-zero** — chronic over-forecasting kills margin via overstock; under-forecasting kills sales via OOS.
3. Are **promo-week forecasts** as accurate as non-promo? If not, your model isn't learning promotions.
4. What's our **FVA** vs naive seasonal baseline? If <5%, the team is over-engineering.
5. Are **new-SKU forecasts** within tolerance, or are we over-buying every launch?

## Pitfalls
- Using **MAPE** on zero-sales days → inf or massive values. Switch to SMAPE or WAPE.
- Reporting **point accuracy** only — production needs **prediction intervals** for safety stock.
- Backtesting on **non-time-respecting** splits (random shuffle) — overstates accuracy.
- Forecasting on **historical sales** instead of **historical demand** — sales = min(demand, inventory), so OOS days are censored data.
- Ignoring **hierarchical reconciliation** — top-down often gives different numbers than bottom-up, which confuses stakeholders.
- Confusing **forecast bias** (which compounds week-over-week) with **forecast noise** (which doesn't).
