# scripts/

## `fetch_samples.py`

Downloads or prints fetch instructions for each dataset, depending on its license.

| Dataset | Command | Behavior |
|---|---|---|
| UCI Online Retail | `python scripts/fetch_samples.py uci` | Downloads zip to `scratch/` |
| US Census | `python scripts/fetch_samples.py census` | Downloads xlsx to `samples/` |
| Olist | `python scripts/fetch_samples.py olist` | Prints Kaggle API steps |
| Instacart | `python scripts/fetch_samples.py instacart` | Prints Kaggle API steps |
| Amazon Reviews | `python scripts/fetch_samples.py amazon` | Prints HuggingFace steps |
| Walmart M5 | `python scripts/fetch_samples.py m5` | Prints Kaggle steps |
| H&M | `python scripts/fetch_samples.py hm` | Prints Kaggle steps |
| GA4 | `python scripts/fetch_samples.py ga4` | Prints BigQuery steps |
| Retail Transactions (syn) | `python scripts/fetch_samples.py retail-syn` | Prints Kaggle steps |
| Kaggle UK e-com | `python scripts/fetch_samples.py kaggle-uk` | Prints Kaggle steps |
| All free | `python scripts/fetch_samples.py all-free` | Downloads UCI + Census |

## Prerequisites

```bash
pip install pandas openpyxl                  # for UCI / Census
pip install kaggle                           # for Kaggle datasets
pip install datasets                         # for HuggingFace (Amazon Reviews)
pip install google-cloud-bigquery pandas-gbq # for GA4
```

For Kaggle API:
1. Sign up at kaggle.com.
2. Account → Create New Token → downloads `kaggle.json`.
3. `mkdir -p ~/.kaggle && mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json && chmod 600 ~/.kaggle/kaggle.json`.
4. For competition data, also accept the competition's rules on the Kaggle website first.

## License-safe rules

- `samples/` is committed to the repo. Only put data here from CC0 / CC BY / public-domain sources.
- `scratch/` is `.gitignored`. Restricted-license datasets land here.
- If unsure about a license, default to `scratch/`.
