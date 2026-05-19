# notebooks/

Quickstart notebooks that load → profile → visualize each freely-licensed dataset.

| Notebook | Dataset | What it shows |
|---|---|---|
| [01-uci-online-retail-quickstart.ipynb](01-uci-online-retail-quickstart.ipynb) | UCI Online Retail | Profiling, returns rate, RFM segmentation |
| [02-census-mrts-quickstart.ipynb](02-census-mrts-quickstart.ipynb) | US Census MARTS | YoY growth by NAICS category |

## Running

```bash
pip install pandas openpyxl matplotlib jupyter
jupyter notebook
```

The committed samples are tiny (500-row UCI sample, single-month Census file). Both notebooks state which scorecard they pair with.

For the other 9 datasets, run `python ../scripts/fetch_samples.py <name>` first, then adapt notebook 01 as a starting template.
