# 6. H&M Personalized Fashion Recommendations

- **Link**: https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations
- **License**: Kaggle / H&M competition rules — research and educational use only; no redistribution.
- **Sample in this repo**: None. Use [`scripts/fetch_samples.py`](../scripts/fetch_samples.py).

## From the dataset (paraphrased from Kaggle competition page)
> Two years of transactions from H&M, paired with detailed metadata for customers (age, club status, fashion-news subscription, postal area hash) and articles (product type, color, department, garment group, graphical appearance, plus images and text descriptions).

## Files & Schema *(from competition documentation)*
| File | Key columns |
|---|---|
| `transactions_train.csv` | `t_dat, customer_id, article_id, price, sales_channel_id` (1=offline store, 2=online) |
| `customers.csv` | `customer_id, FN, Active, club_member_status, fashion_news_frequency, age, postal_code` |
| `articles.csv` | `article_id, product_code, prod_name, product_type_no/name, product_group_name, graphical_appearance_no/name, colour_group_code/name, perceived_colour_value_id, perceived_colour_master_id, department_no/name, index_code/name, index_group_no/name, section_no/name, garment_group_no/name, detail_desc` |
| `images/` | One JPG per article, organized into subdirs by article_id prefix |

## Scale *(from competition data description)*
- ~31M transactions
- ~1.37M customers
- ~106K articles
- 2 years (2018-09-20 – 2020-09-22 in the public training set)
- Images dataset is ~22GB on its own.

## Representative sample row *(General knowledge — schema-faithful)*
```
transactions_train.csv:
t_dat=2020-09-22  customer_id=f1d3...e91  article_id=0568601043
price=0.0254207  sales_channel_id=2

customers.csv:
customer_id=f1d3...e91  FN=1  Active=1
club_member_status=ACTIVE  fashion_news_frequency=Regularly
age=34  postal_code=2c29ae...   (hashed/anonymized)

articles.csv:
article_id=0568601043  prod_name="Strap top"
product_type_name=Vest top  product_group_name=Garment Upper body
colour_group_name=Black  index_name=Ladieswear
section_name="Womens Everyday Basics"
garment_group_name="Jersey Basic"
detail_desc="Microfibre vest top with narrow shoulder straps."
```

## Common analyses *(General knowledge)*
1. **Multimodal recommenders** — combine images, text descriptions, and purchase behavior. The standard "real" benchmark beyond Movielens.
2. **Cold-start strategies** — new article_id with no purchases? Use image + detail_desc embedding for similarity-based candidate generation.
3. **Style affinity & seasonality** — track weekly purchase volume by section_name × week → identify trend onset (e.g. denim spikes in week 36).
4. **Channel attribution** — `sales_channel_id=1 vs 2` lets you study online → offline showrooming or vice versa per customer.
5. **Loyalty / club value quantification** — `club_member_status=ACTIVE` cohort vs inactive: lifetime value, purchase frequency, basket diversity.
6. **Markdown / price-position analysis** — `price` is normalized (0..1) per dataset, but relative price within a product_type still works for "luxury vs basic" splits.
7. **Fashion-specific KPIs** — sell-through rate, full-price ratio, average days-from-launch-to-purchase, color/size mix.

## Gotchas
- `price` is **normalized**, not in real currency. Don't compute revenue without rescaling.
- `postal_code` is hashed — same prefix doesn't imply geographic proximity.
- Many articles are seasonal: a model trained on summer transactions will fail in winter without temporal features.
- Image files use article_id prefix subdir convention (`0568/0568601043.jpg`) — flat ls will not work.
