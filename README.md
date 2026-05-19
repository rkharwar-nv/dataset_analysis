# Retail Datasets — A New PM's Field Guide

A curated, opinionated reference to the most widely used public retail datasets, written from a Product Manager's perspective. For each dataset you get: what it is, license, schema, a real sample row, and how a retail PM would actually use it.

## Quick navigation

- **[datasets/](datasets/)** — one deep-dive page per dataset
- **[scorecards/](scorecards/)** — PM scorecard templates (RFM, delivery SLA, promo lift, forecast accuracy)
- **[regulatory/](regulatory/)** — GDPR / CCPA / LGPD / PCI checklist for retail data
- **[samples/](samples/)** — small sample CSVs for the freely-licensed datasets
- **[scripts/](scripts/)** — fetch scripts for restricted datasets
- **[notebooks/](notebooks/)** — Jupyter quickstarts (load → profile → visualize)

## Master table

| # | Dataset | What it's about | License |
|---|---|---|---|
| 1 | [UCI Online Retail / II](datasets/01-uci-online-retail.md) | UK non-store online retailer, 2009–2011, ~1M invoice lines, gifts + wholesale | CC BY 4.0 |
| 2 | [Brazilian E-Commerce by Olist](datasets/02-olist-brazilian.md) | ~100K real BR orders 2016–2018, 9 relational tables incl. reviews & geo | CC BY-NC-SA 4.0 |
| 3 | [Instacart Online Grocery](datasets/03-instacart.md) | 3M+ grocery orders, 200K users, reorder patterns | Instacart Open Dataset (non-commercial, no redistribution) |
| 4 | [Amazon Customer Reviews](datasets/04-amazon-reviews.md) | 75GB+ product reviews & metadata across categories | Amazon CR License (research only) |
| 5 | [Walmart M5 Forecasting](datasets/05-walmart-m5.md) | Daily sales for 3,049 SKUs × 10 stores, CA/TX/WI | Kaggle Competition Rules |
| 6 | [H&M Personalized Fashion](datasets/06-hm-fashion.md) | 2yr fashion transactions + customer metadata + product images | H&M Competition Rules |
| 7 | [Dunnhumby — Complete Journey](datasets/07-dunnhumby.md) | 2yr household grocery transactions + promo + demographics | Dunnhumby Source Files (academic/non-commercial) |
| 8 | [Google Analytics Sample (GA4)](datasets/08-ga4-sample.md) | 3mo obfuscated event-level data, Google Merchandise Store | Google APIs ToS |
| 9 | [US Census Monthly Retail Trade](datasets/09-census-mrts.md) | Monthly/annual retail sales by NAICS, quarterly e-commerce | Public domain |
| 10 | [Kaggle E-Commerce Data (UK)](datasets/10-kaggle-uk-ecom.md) | 541K transactions from UK online retailer (mirror of UCI) | CC0 |
| 11 | [Retail Transactions (synthetic)](datasets/11-retail-transactions.md) | Synthetic transactions for basket/segmentation prototyping | CC0 |

## Suggested reading order for a new Retail PM

1. **[US Census MRTS](datasets/09-census-mrts.md)** — macro context, 30 min
2. **[UCI Online Retail](datasets/01-uci-online-retail.md)** — simplest schema, get hands-on
3. **[Olist](datasets/02-olist-brazilian.md)** — multi-table modeling + review/funnel signals
4. **[Instacart](datasets/03-instacart.md) + [Dunnhumby](datasets/07-dunnhumby.md)** — basket-level intuition
5. **[M5](datasets/05-walmart-m5.md) + [H&M](datasets/06-hm-fashion.md)** — forecasting & fashion-specific dynamics
6. **[GA4 sample](datasets/08-ga4-sample.md)** — read your own site's analytics fluently

## How attribution works in this repo

Each dataset page is split into:

- **From the dataset** — content verbatim or paraphrased from the source page, with link.
- **General knowledge** — my PM framing and use-case suggestions.

Both are clearly labeled inline.

## Licensing

The writeups, scorecards, checklists, and code in this repo are licensed under [CC BY 4.0](LICENSE). The datasets themselves are *not* — each retains its own license, reproduced on its page.

If you want to add a sample to `samples/`, the dataset must allow redistribution. When in doubt, use `scripts/fetch_samples.py` instead.
