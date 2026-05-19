"""
fetch_samples.py — download small samples of retail datasets for local exploration.

The repo only commits samples for permissively-licensed datasets (UCI, US Census,
CC0 Kaggle). For datasets whose license prohibits redistribution, this script
shows you how to fetch them into a local, gitignored directory.

Usage:
    python scripts/fetch_samples.py uci          # CC BY 4.0, committed by default
    python scripts/fetch_samples.py census       # public domain, committed
    python scripts/fetch_samples.py olist        # requires Kaggle API
    python scripts/fetch_samples.py instacart    # requires Kaggle API
    python scripts/fetch_samples.py amazon       # via Hugging Face datasets
    python scripts/fetch_samples.py m5           # requires Kaggle API
    python scripts/fetch_samples.py hm           # requires Kaggle API
    python scripts/fetch_samples.py ga4          # requires gcloud + BigQuery
    python scripts/fetch_samples.py retail-syn   # CC0 — committed by default

All restricted-license downloads land in ./scratch/ (gitignored).
"""

from __future__ import annotations
import argparse
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRATCH = ROOT / "scratch"
SAMPLES = ROOT / "samples"
SCRATCH.mkdir(exist_ok=True)
SAMPLES.mkdir(exist_ok=True)


def fetch_uci() -> None:
    """UCI Online Retail — CC BY 4.0."""
    url = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
    out = SCRATCH / "online_retail.zip"
    print(f"Downloading {url} -> {out}")
    urllib.request.urlretrieve(url, out)
    subprocess.run(["unzip", "-o", str(out), "-d", str(SCRATCH)], check=True)
    print(f"Extracted to {SCRATCH}/Online Retail.xlsx")
    print(f"Sample (first 500 rows) is already committed at samples/uci-online-retail-sample.csv")


def fetch_census() -> None:
    """US Census MARTS — public domain."""
    url = "https://www2.census.gov/retail/releases/historical/marts/rs2604.xlsx"
    out = SAMPLES / "census-marts-apr2026.xlsx"
    print(f"Downloading {url} -> {out}")
    urllib.request.urlretrieve(url, out)
    print(f"Saved to {out} (also committed to repo)")


def fetch_olist() -> None:
    """Olist Brazilian E-Commerce — CC BY-NC-SA 4.0, no redistribution."""
    print("Olist requires the Kaggle API. Steps:")
    print("  1. pip install kaggle")
    print("  2. Get your token from kaggle.com/<user>/account → 'Create New Token'")
    print("  3. mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json && chmod 600 ~/.kaggle/kaggle.json")
    print(f"  4. cd {SCRATCH} && kaggle datasets download olistbr/brazilian-ecommerce --unzip")


def fetch_instacart() -> None:
    """Instacart Online Grocery — non-commercial, no redistribution."""
    print("Instacart requires the Kaggle API. Steps:")
    print("  1. pip install kaggle  (see Olist for token setup)")
    print(f"  2. cd {SCRATCH} && kaggle competitions download -c instacart-market-basket-analysis")
    print("  3. unzip instacart-market-basket-analysis.zip")
    print("Or via the community mirror:")
    print(f"  cd {SCRATCH} && kaggle datasets download yasserh/instacart-online-grocery-basket-analysis-dataset --unzip")


def fetch_amazon() -> None:
    """Amazon Reviews '23 — research only, via Hugging Face."""
    print("Amazon Reviews '23: best fetched via the Hugging Face datasets library.")
    print("  pip install datasets")
    print("  python -c \"from datasets import load_dataset;\\")
    print("    ds = load_dataset('McAuley-Lab/Amazon-Reviews-2023', 'raw_review_All_Beauty');\\")
    print("    ds['full'].select(range(1000)).to_csv('scratch/amazon_beauty_sample.csv')\"")


def fetch_m5() -> None:
    """Walmart M5 — competition rules, no redistribution."""
    print("Walmart M5 requires the Kaggle competitions API:")
    print(f"  cd {SCRATCH} && kaggle competitions download -c m5-forecasting-accuracy")
    print("  unzip m5-forecasting-accuracy.zip")


def fetch_hm() -> None:
    """H&M Personalized Fashion — competition rules, no redistribution."""
    print("H&M requires the Kaggle competitions API:")
    print(f"  cd {SCRATCH} && kaggle competitions download -c h-and-m-personalized-fashion-recommendations")
    print("  (Note: full dataset is ~22GB due to images. Skip images dir if you only need tabular.)")


def fetch_ga4() -> None:
    """GA4 Sample — via BigQuery."""
    print("GA4 Sample is BigQuery-only. Steps:")
    print("  1. Create a Google Cloud project, enable BigQuery API")
    print("  2. gcloud auth application-default login")
    print("  3. bq extract --destination_format=CSV \\")
    print("       'bigquery-public-data:ga4_obfuscated_sample_ecommerce.events_20201119' \\")
    print(f"       gs://your-bucket/ga4_sample_*.csv")
    print("Or pandas + pandas-gbq:")
    print("  pip install pandas-gbq")
    print("  pd.read_gbq('SELECT * FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_20201119` LIMIT 10000')")


def fetch_retail_syn() -> None:
    """Retail Transactions synthetic — CC0."""
    print("Retail Transactions (synthetic) is CC0:")
    print(f"  cd {SCRATCH} && kaggle datasets download prasad22/retail-transactions-dataset --unzip")


def fetch_kaggle_uk() -> None:
    """Kaggle UK e-commerce — CC0 (mirror of UCI)."""
    print("Kaggle UK e-commerce is CC0:")
    print(f"  cd {SCRATCH} && kaggle datasets download carrie1/ecommerce-data --unzip")


DISPATCH = {
    "uci": fetch_uci,
    "census": fetch_census,
    "olist": fetch_olist,
    "instacart": fetch_instacart,
    "amazon": fetch_amazon,
    "m5": fetch_m5,
    "hm": fetch_hm,
    "ga4": fetch_ga4,
    "retail-syn": fetch_retail_syn,
    "kaggle-uk": fetch_kaggle_uk,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", choices=list(DISPATCH.keys()) + ["all-free"])
    args = parser.parse_args()

    if args.dataset == "all-free":
        for k in ("uci", "census"):
            DISPATCH[k]()
            print()
        return 0

    DISPATCH[args.dataset]()
    return 0


if __name__ == "__main__":
    sys.exit(main())
