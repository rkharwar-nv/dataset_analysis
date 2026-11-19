# Retail Datasets

A curated index of public retail and e-commerce datasets and leaderboards: transaction logs, relational databases, recommendation and search benchmarks, demand forecasting, product catalogs, LLM and shopping-agent evals, competition datasets, and product, fashion and in-store vision. Each entry lists the source, scale, license and how to access it.

> Hugging Face IDs and licenses were checked against the Hub API on **2026-11-18**. Licenses change, so check the source before you redistribute or use a dataset commercially.

## Contents

- [Leaderboards](#leaderboards)
- [Stanford datasets](#stanford-datasets)
- [Hugging Face datasets](#hugging-face-datasets)
  - [LLM and shopping-agent benchmarks](#llm-and-shopping-agent-benchmarks)
  - [Product search and retrieval](#product-search-and-retrieval)
  - [Recommendation and behavior logs](#recommendation-and-behavior-logs)
  - [Demand forecasting](#demand-forecasting)
  - [Catalogs, taxonomy and pretraining corpora](#catalogs-taxonomy-and-pretraining-corpora)
  - [Product, fashion and in-store vision](#product-fashion-and-in-store-vision)
- [Competition and challenge datasets](#competition-and-challenge-datasets)
- [Classic transactional datasets](#classic-transactional-datasets) (with deep-dive pages)
- [Choosing by task](#choosing-by-task)
- [Loading snippets](#loading-snippets)
- [Repo layout](#repo-layout)
- [Licensing](#licensing)

---

## Leaderboards

Live leaderboards with retail or e-commerce tasks. Rankings change frequently, so follow the link for current results.

| Leaderboard | Task | Underlying data | Link |
|---|---|---|---|
| **RelBench** | Relational deep learning: churn, sales, LTV, recommendation on `rel-amazon`, `rel-hm`, `rel-avito` and others | RelBench v1/v2 | [relbench.stanford.edu/leaderboard](https://relbench.stanford.edu/leaderboard) |
| **STaRK** | Semi-structured product retrieval (Hit@1, MRR) on STaRK-Amazon | STaRK | [HF Space: snap-stanford/stark-leaderboard](https://huggingface.co/spaces/snap-stanford/stark-leaderboard) |
| **OGB node property** | `ogbn-products` node classification accuracy | Amazon co-purchase graph | [ogb.stanford.edu/docs/leader_nodeprop](https://ogb.stanford.edu/docs/leader_nodeprop/) |
| **Shopping MMLU** | 57 shopping tasks across concept understanding, reasoning, user behavior, multilinguality | Shopping MMLU (Amazon, NeurIPS 2024 D&B) | [HF Space: KL4805/shopping_mmlu_leaderboard](https://huggingface.co/spaces/KL4805/shopping_mmlu_leaderboard) |
| **Amazon KDD Cup 2024** | Multi-task online shopping challenge for LLMs (ShopBench) | ShopBench / Shopping MMLU | [AIcrowd](https://www.aicrowd.com/challenges/amazon-kdd-cup-2024-multi-task-online-shopping-challenge-for-llms) |
| **τ²-bench (retail domain)** | Tool-using customer-service agent: orders, returns, exchanges under policy | τ²-bench retail DB ([`HuggingFaceH4/tau2-bench-data`](https://huggingface.co/datasets/HuggingFaceH4/tau2-bench-data)) | [taubench.com](https://taubench.com) · [github](https://github.com/sierra-research/tau2-bench) |
| **fev-bench** | Time-series foundation-model forecasting; retail series include M5, Favorita, Rossmann, Walmart, Rohlik and hierarchical sales | [`autogluon/fev_datasets`](https://huggingface.co/datasets/autogluon/fev_datasets) | [HF Space: autogluon/fev-bench](https://huggingface.co/spaces/autogluon/fev-bench) |
| **GIFT-Eval** | General time-series forecasting; retail series include hierarchical sales, car parts and restaurant visits | GIFT-Eval | [HF Space: Salesforce/GIFT-Eval](https://huggingface.co/spaces/Salesforce/GIFT-Eval) |
| **TREC Product Search & Recommendation** | Annual product ranking and recommendation track (2023–2025) | ESCI, Amazon-M2 derived | [trec-product-search.github.io](https://trec-product-search.github.io/) |
| **Kaggle (closed, leaderboards archived)** | Forecasting, recommendation, matching, search relevance | M5, Favorita, Rossmann, Walmart, OTTO, H&M, Instacart, Shopee, Home Depot | see [Competition and challenge datasets](#competition-and-challenge-datasets) |

Benchmarks with published results tables but no hosted leaderboard: ShoppingBench, ShoppingComp, DeepShop, WebMall, EcomBench, EcomEval, OxyEcomBench, ChineseEcomQA. See [LLM and shopping-agent benchmarks](#llm-and-shopping-agent-benchmarks).

---

## Stanford datasets

These come from Stanford groups: STAR / SNAP (Jure Leskovec), OGB, CVGL and Stanford NLP. Most retail content is Amazon or H&M data repackaged for graph learning, relational learning or retrieval.

| Dataset | Group | What it is | Retail content | License | Access |
|---|---|---|---|---|---|
| **RelBench v1** | STAR | Benchmark for deep learning on relational databases (NeurIPS 2024) | `rel-amazon` (users, products, reviews; ~15M rows; churn, LTV, rating, recommendation tasks), `rel-hm` (H&M customers, articles, transactions; sales, churn, purchase tasks), `rel-avito` (classified ads) | Per-DB upstream license; STAR conversions, tasks and splits CDLA-Permissive-2.0 | [`stanford-star/relbench-v1`](https://huggingface.co/datasets/stanford-star/relbench-v1) · `pip install relbench` |
| **RelBench v2** | STAR | Adds 4 databases and 36 tasks, including autocomplete tasks on the v1 DBs (ICLR 2026 DATA-FM workshop, [arXiv:2602.12606](https://arxiv.org/abs/2602.12606)) | `rel-salt` (SAP ERP sales orders), `rel-ratebeer` (consumer ratings), plus new tasks on `rel-amazon` and `rel-hm` | Per-DB upstream | [`stanford-star/relbench-v2-extra`](https://huggingface.co/datasets/stanford-star/relbench-v2-extra) |
| **The Join** | STAR | Large pretraining corpus of real relational DBs in RelBench format, released with the RT-J relational transformer (NeurIPS 2026) | `join-amazon-*` (27 Amazon Reviews 2023 categories), `join-online-retail` (UCI II), `join-iowa-liquor`, `join-open-food-facts`, `join-bird-retails`, `join-bird-sales-in-weather`, `join-bird-superstore`, `join-salesdb`, `join-gosales`, Northwind, AdventureWorks | Per-DB upstream (listed in `STATS/databases.parquet`) | [`stanford-star/the-join`](https://huggingface.co/datasets/stanford-star/the-join) |
| **STaRK** | SNAP | Semi-structured retrieval benchmark over textual and relational knowledge bases (NeurIPS 2024 D&B) | **STaRK-Amazon**: product KB with brands, categories, co-purchase links and reviews; synthesized and human-written natural-language product queries | CC BY 4.0 | [`snap-stanford/stark`](https://huggingface.co/datasets/snap-stanford/stark) · [stark.stanford.edu](https://stark.stanford.edu/) |
| **AmazonQAC** | Amazon + Stanford NLP (C. Potts) | Query-autocomplete dataset built from real Amazon search logs (EMNLP 2024) | 395M training samples (prefix sequences → final query), 20K test samples | CDLA-Permissive-2.0 | [`amazon/AmazonQAC`](https://huggingface.co/datasets/amazon/AmazonQAC) |
| **ogbn-products** | OGB | Node classification on the Amazon co-purchase graph | 2.4M products, 61.9M co-purchase edges, 47 categories | Amazon license (see OGB) | [ogb.stanford.edu](https://ogb.stanford.edu/docs/nodeprop/#ogbn-products) · `pip install ogb` |
| **SNAP Amazon collections** | SNAP | Older graph and review dumps | `amazon0302`–`amazon0601` co-purchase graphs, `amazon-meta` (548K products), `web-FineFoods` (568K food reviews), `web-Amazon` reviews | Research use | [snap.stanford.edu/data](https://snap.stanford.edu/data/#amazon) |
| **Stanford Online Products (SOP)** | CVGL | Deep-metric-learning and image-retrieval benchmark (CVPR 2016) | 120,053 eBay listing images, 22,634 products, 12 categories | Research use | [cvgl.stanford.edu](https://cvgl.stanford.edu/projects/lifted_struct/) |

Related, but not from Stanford: **Amazon Reviews 2023** (UCSD McAuley Lab) is the upstream source for The Join's Amazon DBs and for many benchmarks below. It is listed under [Recommendation and behavior logs](#recommendation-and-behavior-logs).

---

## Hugging Face datasets

### LLM and shopping-agent benchmarks

| Dataset | Released | What it is | Size | License |
|---|---|---|---|---|
| [`amazon/ShoppingReasoningBench`](https://huggingface.co/datasets/amazon/ShoppingReasoningBench) | 2026-06 | Expert-written missions for conversational shopping assistants, scored with weighted binary rubrics | 525 missions (232 single-turn, 293 multi-turn), ~10.9K rubrics | CC BY-NC 4.0 (gated) |
| [`huaixiao/ShoppingComp`](https://huggingface.co/datasets/huaixiao/ShoppingComp) | 2026-02 | Open-world shopping-agent eval: web retrieval, multi-constraint checking and safety traps, in English and Chinese ([arXiv:2511.22978](https://arxiv.org/abs/2511.22978)) | 97 ground-truth tasks + 48 safety traps (current release) | MIT |
| [`Alibaba-NLP/EcomBench`](https://huggingface.co/datasets/Alibaba-NLP/EcomBench) | 2025-12 | Agent benchmark of real e-commerce operational tasks requiring domain knowledge, multi-step reasoning and tool use, across 7 task categories | — | MIT |
| [`DeepShop/DeepShop`](https://huggingface.co/datasets/DeepShop/DeepShop) | 2025-06 | Online "deep research" shopping-agent queries across 5 domains with attribute, filter and sort constraints at 3 difficulty levels ([arXiv:2506.02839](https://arxiv.org/abs/2506.02839)) | — | CC BY 4.0 |
| WebMall | 2025-08 | Offline benchmark with 4 simulated shops populated from Common Crawl offers; cross-shop search, price comparison, cart and checkout ([arXiv:2508.13024](https://arxiv.org/abs/2508.13024)) | 91 tasks | see paper |
| Shopping MMLU / ShopBench ([github](https://github.com/KL4805/ShoppingMMLU)) | 2024-10 | Multi-task shopping knowledge and reasoning benchmark, used for Amazon KDD Cup 2024 ([arXiv:2410.20745](https://arxiv.org/abs/2410.20745)) | 57 tasks | see repo |
| [`NingLab/EcomMMMU`](https://huggingface.co/datasets/NingLab/EcomMMMU) | 2025 | Multimodal, multi-task e-commerce understanding with a vision-salient subset where text alone is insufficient | 406K samples, ~9M images, 34 categories | CC BY 4.0 |
| [`OpenStellarTeam/Chinese-EcomQA`](https://huggingface.co/datasets/OpenStellarTeam/Chinese-EcomQA) | 2025-02 | Chinese QA benchmark on fundamental e-commerce concepts ([arXiv:2502.20196](https://arxiv.org/abs/2502.20196)) | — | CC BY-NC-SA 4.0 |
| EcomEval ([github](https://github.com/ShopeeLLM/EcomEval)) | 2025-10 | Multilingual, multimodal e-commerce eval from real customer queries and transaction logs; 7 languages incl. 5 Southeast Asian ([arXiv:2510.20632](https://arxiv.org/abs/2510.20632)) | 37 tasks | see repo |
| OxyEcomBench | 2026-05 | Bilingual (ZH/EN) multimodal benchmark covering platform, merchant and customer roles ([arXiv:2605.13173](https://arxiv.org/abs/2605.13173)) | ~6.3K instances, 29 tasks | CC BY 4.0 (paper) |
| τ²-bench retail ([`HuggingFaceH4/tau2-bench-data`](https://huggingface.co/datasets/HuggingFaceH4/tau2-bench-data)) | 2025 | Retail customer-service domain (orders, returns, exchanges) for tool-calling agents; successor to τ-bench | — | MIT |
| ShoppingBench | 2025-08 | Intent-grounded agent tasks (vouchers, budgets, multi-product) in a sandbox of 2.5M+ real products ([arXiv:2508.04266](https://arxiv.org/abs/2508.04266)) | — | see paper |
| [`arcada-labs/grocery-bench`](https://huggingface.co/datasets/arcada-labs/grocery-bench) | 2026-03 | 30-turn speech-to-speech grocery-ordering eval with tool calls (cart edits, quantity math, homophones) | 30 turns | MIT |
| [`NingLab/ECInstruct`](https://huggingface.co/datasets/NingLab/ECInstruct) | 2024 | Instruction-tuning and eval set covering 10 e-commerce tasks (eCeLLM) | 116,528 examples | CC BY 4.0 |
| [`bitext/Bitext-retail-ecommerce-llm-chatbot-training-dataset`](https://huggingface.co/datasets/bitext/Bitext-retail-ecommerce-llm-chatbot-training-dataset) | 2024 | Synthetic customer-service intents and responses for retail chatbots | — | CDLA-Sharing-1.0 |
| WebShop mirrors (e.g. [`HongbangYuan/webshop`](https://huggingface.co/datasets/HongbangYuan/webshop)) | — | Trajectories and evals for the WebShop simulated store, widely used for agent RL | — | check mirror |
| [`Novice-ninja/retail-merchbench`](https://huggingface.co/datasets/Novice-ninja/retail-merchbench) | 2026-06 | MerchBench: merchandise-planning tasks for routing between models. Its authors warn against using it as the sole basis for buying, allocation, pricing or markdown decisions. **Take:** niche and tiny, but one of few benchmarks aimed at merchandising rather than shopper-side tasks. Treat as a probe, not a leaderboard. | n<1K | CC BY 4.0 |
| [`lainmn/AgentDS-Commerce`](https://huggingface.co/datasets/lainmn/AgentDS-Commerce) | 2025-11 | Commerce slice of the AgentDS human-AI data-science benchmark ([arXiv:2603.19005](https://arxiv.org/abs/2603.19005)): store-SKU demand forecasting, personalized recommendation, coupon redemption prediction. Tagged synthetic. **Take:** useful for testing data-science agents end to end; don't draw business conclusions from synthetic data. | — | CC BY-NC-SA 4.0 |

### Product search and retrieval

| Dataset | What it is | Size | License |
|---|---|---|---|
| Amazon ESCI / Shopping Queries ([`tasksource/esci`](https://huggingface.co/datasets/tasksource/esci), official: [amazon-science/esci-data](https://github.com/amazon-science/esci-data)) | Query–product relevance labels (Exact / Substitute / Complement / Irrelevant) in US, ES and JP locales | ~130K queries, ~2.6M judgments | Apache-2.0 |
| [`crossingminds/shopping-queries-image-dataset`](https://huggingface.co/datasets/crossingminds/shopping-queries-image-dataset) (SQID) | ESCI enriched with product image URLs and CLIP image/text embeddings | ~190K products | MIT |
| [`trec-product-search/product-recommendation-2025`](https://huggingface.co/datasets/trec-product-search/product-recommendation-2025) | TREC 2025 Product Search & Recommendation track data, derived from ESCI and Amazon-M2. See also the `trec-product-search/*` corpora, queries and qrels | — | Apache-2.0 |
| WANDS — Wayfair ANnotation DataSet ([`tasksource/wands`](https://huggingface.co/datasets/tasksource/wands), official: [wayfair/WANDS](https://github.com/wayfair/WANDS)) | Furniture/home-goods search relevance with 3-grade labels (exact / partial / irrelevant) | ~43K products, 480 queries, ~233K judgments | MIT |
| Home Depot Product Search Relevance ([Kaggle](https://www.kaggle.com/competitions/home-depot-product-search-relevance)) | Query–product relevance scores (1–3) with product attributes | ~74K training pairs | competition rules |
| [`McAuley-Lab/Amazon-C4`](https://huggingface.co/datasets/McAuley-Lab/Amazon-C4) | Complex, context-rich product queries for retrieval (from the BLaIR paper) | 21,223 queries over ~1.06M items | see card |
| [`Marqo/marqo-GS-10M`](https://huggingface.co/datasets/Marqo/marqo-GS-10M) | Multimodal Google Shopping query–product ranking data | ~10M pairs | Apache-2.0 |
| [`Marqo/google-shopping-general-eval`](https://huggingface.co/datasets/Marqo/google-shopping-general-eval) | GoogleShopping-1m eval set for e-commerce embedding models (an AmazonProducts-3m set is also available) | 1M | see card |
| [`opdullah/turkish-product-matching-706k`](https://huggingface.co/datasets/opdullah/turkish-product-matching-706k) | Turkish product matching: offers grouped into the same product, with group-safe train/validation/test splits. **Take:** rare non-English entity-matching set at useful scale, but the license is a custom research-only attribution terms file, so read it before any commercial use. | 1M–10M rows | custom (research-only, attribution) |

### Recommendation and behavior logs

| Dataset | What it is | Size | License |
|---|---|---|---|
| [`McAuley-Lab/Amazon-Reviews-2023`](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) | Reviews, ratings and rich item metadata (May 1996 – Sep 2023), across 33 categories. The default source for recommender systems and review modelling | ~571M reviews, ~48M items | Code MIT; Amazon terms apply to data |
| [`TaoBao-MM/Taobao-MM`](https://huggingface.co/datasets/TaoBao-MM/Taobao-MM) | Taobao interaction logs with behavior sequences of up to 1,000 items plus multimodal item embeddings, for long-sequence recommendation | large-scale | Apache-2.0 |
| Synerise / RecSys Challenge 2025 ([recsys.synerise.com](https://recsys.synerise.com/)) | Six months of online-retailer events: buys, add/remove cart, page visits, search queries; task is universal behavioral profiles | large, sparse | see site |
| [`t-tech/T-ECD`](https://huggingface.co/datasets/t-tech/T-ECD) | Cross-domain interactions (marketplace, retail delivery, payments, offers, reviews) from T-Bank's ecosystem (KDD 2026) | large-scale, anonymized | CC BY-NC-SA 4.0 |
| [`einrafh/hnm-fashion-recommendations-data`](https://huggingface.co/datasets/einrafh/hnm-fashion-recommendations-data) | Mirror of the H&M Personalized Fashion Kaggle data (transactions, customers, articles) | ~31M transactions | H&M competition rules |
| [`kevykibbz/ecommerce-behavior-data-from-multi-category-store_oct-nov_2019`](https://huggingface.co/datasets/kevykibbz/ecommerce-behavior-data-from-multi-category-store_oct-nov_2019) | REES46 / Open CDP clickstream: view, cart, remove_from_cart and purchase events | 285M events | see upstream |
| [`DanielKiani/RetailRocket-Recommender-Data`](https://huggingface.co/datasets/DanielKiani/RetailRocket-Recommender-Data) | RetailRocket session events, item properties and category tree | ~2.7M events (upstream Kaggle release) | check upstream Kaggle license |
| [`HariJha/FreeEcommerceTwin14M`](https://huggingface.co/datasets/HariJha/FreeEcommerceTwin14M) | Fully synthetic, seven linked tables (customers, orders, returns, tickets), suitable for SQL and analytics prototyping | 14M rows | CC BY-NC 4.0 |
| [`while-ai/ecommerce-intent`](https://huggingface.co/datasets/while-ai/ecommerce-intent) | E-commerce purchase-intent data. **Take:** the card is thin and I did not inspect the data; verify provenance and label definitions before relying on it. | 10K–100K rows | CC BY 4.0 |
| [`trucmtnguyen/multimodal-product-reviews-lazada`](https://huggingface.co/datasets/trucmtnguyen/multimodal-product-reviews-lazada) | Lazada product reviews with images, for multimodal review analysis. **Take:** good Southeast Asian coverage that Amazon-centric sets lack, but the NC-ND license blocks derivatives, so it is fine for evaluation only. | 10K–100K | CC BY-NC-ND 4.0 |

### Demand forecasting

| Dataset | What it is | Size | License |
|---|---|---|---|
| [`Dingdong-Inc/FreshRetailNet-50K`](https://huggingface.co/datasets/Dingdong-Inc/FreshRetailNet-50K) | Hourly fresh-grocery sales with organically occurring stockouts (~20%), for censored-demand estimation ([arXiv:2505.16319](https://arxiv.org/abs/2505.16319)) | 50K store–product series × 90 days, 898 stores, 18 cities | CC BY 4.0 |
| [`Dingdong-Inc/FreshRetailNet-LT`](https://huggingface.co/datasets/Dingdong-Inc/FreshRetailNet-LT) | Longer-horizon companion to FreshRetailNet-50K | 20K+ series | CC BY 4.0 |
| [`autogluon/fev_datasets`](https://huggingface.co/datasets/autogluon/fev_datasets) | Forecasting benchmark collection in a common format; retail configs include `m5_*`, `favorita_*`, `rossmann_*`, `walmart`, `rohlik_sales_*`, `hierarchical_sales_*`, `restaurant` | 100 configs | per-dataset |
| VN1 Forecasting Competition ([Nixtla walkthrough](https://nixtla.github.io/nixtlar/articles/vn1-forecasting-competition.html)) | Weekly sales from 46 retailers across 328 warehouses, 2020–2024 (2024 competition by Flieber, Syrup Tech, SupChains) | ~15K products | competition terms |
| Walmart M5 · Corporación Favorita · Rossmann · Walmart Store Sales | Kaggle forecasting competitions | see [Competition and challenge datasets](#competition-and-challenge-datasets) | competition rules |
| [`t4tiana/store-sales-time-series-forecasting`](https://huggingface.co/datasets/t4tiana/store-sales-time-series-forecasting) | Mirror of Kaggle's Favorita store sales data (Ecuador): product-family sales by store with promo counts, oil prices and holidays. **Take:** a good promo-aware forecasting teaching set, but it is an unofficial mirror with no license on the card, so use the Kaggle terms. Favorita is also in `fev_datasets`. | — | none on card; Kaggle rules |
| Kilts Center Retail Scanner Data / Dominick's ([Kilts Center](https://www.chicagobooth.edu/research/kilts/research-data), [Dominick's](https://www.chicagobooth.edu/research/kilts/research-data/dominicks)) | Weekly grocery scanner data used in price and promotion elasticity research, e.g. [arXiv:2606.17941](https://arxiv.org/html/2606.17941). **Take:** the real option for pricing and promo-lift work, since open pricing data is scarce. Dominick's (1989–97) is dated; Kilts needs a data-use agreement. | large | access-restricted (check terms) |

### Catalogs, taxonomy and pretraining corpora

| Dataset | What it is | Size | License |
|---|---|---|---|
| [`Shopify/product-catalogue`](https://huggingface.co/datasets/Shopify/product-catalogue) | "The Catalogue": a multimodal product-taxonomy classification benchmark (image, title, description, brand → Shopify taxonomy node) | 48,289 products, 10,476 categories | Apache-2.0 |
| [`thebajajra/Ecom-niverse`](https://huggingface.co/datasets/thebajajra/Ecom-niverse) | E-commerce-filtered web text from FineFineWeb, used to train the RexBERT encoders | ~350B tokens | Apache-2.0 |
| [`retail-product-promotion/mSOP-765k`](https://huggingface.co/datasets/retail-product-promotion/mSOP-765k) | Product crops from retail ad leaflets, labeled with brand, category, GTIN, weight, price, regular price and discount, plus OCR text | ~765K | CC BY-NC-ND 4.0 |
| [`Qdrant/hm_ecommerce_products`](https://huggingface.co/datasets/Qdrant/hm_ecommerce_products) | H&M product catalog prepared for vector search | — | CC BY 4.0 |

### Product, fashion and in-store vision

| Dataset | What it is | Size | License |
|---|---|---|---|
| [`huggingface/amazon-berkeley-objects`](https://huggingface.co/datasets/huggingface/amazon-berkeley-objects) | Amazon Berkeley Objects (ABO): product listings with catalog images, multilingual metadata and artist-made 3D models (GLB) | ~147K listings, ~8K 3D models | CC BY 4.0 |
| [`nyris/products10k-v1`](https://huggingface.co/datasets/nyris/products10k-v1) | Products-10K: real-world product recognition and retrieval under varied lighting, occlusion and backgrounds | 197,307 images, 9,691 products | see card |
| SKU-110K (e.g. [`Voxel51/sku110k_test`](https://huggingface.co/datasets/Voxel51/sku110k_test), official: [eg4000/SKU110K_CVPR19](https://github.com/eg4000/SKU110K_CVPR19)) | Densely packed retail-shelf object detection (CVPR 2019) | ~11.7K shelf images, ~1.7M boxes | research use |
| [`mvasil/polyvore-outfits`](https://huggingface.co/datasets/mvasil/polyvore-outfits) | Polyvore outfit compatibility and fill-in-the-blank | ~68K outfits | see card |
| DeepFashion2 (e.g. [`sahirp/deepfashion2`](https://huggingface.co/datasets/sahirp/deepfashion2)) | Clothing detection, segmentation, landmarks and consumer-to-shop retrieval | ~491K images | research use |
| Fashion-IQ (e.g. [`Plachta/FashionIQ`](https://huggingface.co/datasets/Plachta/FashionIQ)) | Composed image retrieval: reference image + text modification → target product | ~77K images | research use |
| [`standard-cognition/RetailAction`](https://huggingface.co/datasets/standard-cognition/RetailAction) | Multi-view ceiling-camera clips with point-labeled take, put and touch interactions (ICCV 2025 Retail Vision workshop) | 21K samples, ~41h, 10 US stores | see card |
| [`amazon/armbench-*`](https://huggingface.co/amazon) | Warehouse robotic pick-and-stow: segmentation, object ID, defect detection | multiple subsets | see cards |
| [`prcvlabs/multiview-retail-tracking`](https://huggingface.co/datasets/prcvlabs/multiview-retail-tracking) | Multi-camera shopper tracking | — | see card |
| [`benjamintli/retail-product-checkout`](https://huggingface.co/datasets/benjamintli/retail-product-checkout) | Mirror of RPC, an automatic-checkout product recognition dataset | — | see card |
| [`shelfwise-by-form/SKUs_on_shelves_PL`](https://huggingface.co/datasets/shelfwise-by-form/SKUs_on_shelves_PL) | Polish retail shelf images with SKU-level annotations. **Take:** best-licensed shelf-recognition set found here (CC BY 4.0) and a more commercial-friendly alternative to SKU-110K. | 1M–10M annotations | CC BY 4.0 |
| [`UniDataPro/grocery-shelves`](https://huggingface.co/datasets/UniDataPro/grocery-shelves) | Grocery shelf images. **Take:** small sample from a data vendor; NC-ND license limits it to evaluation. | 1K–10K | CC BY-NC-ND 4.0 |
| [`Marqo/fashion200k`](https://huggingface.co/datasets/Marqo/fashion200k) | Fashion image-text pairs for retrieval and embedding evals. **Take:** easy, permissively licensed benchmark for fashion embeddings. | ~200K | Apache-2.0 |
| [`detection-datasets/fashionpedia`](https://huggingface.co/datasets/detection-datasets/fashionpedia) | Fashionpedia: garment detection, segmentation and attribute labels. **Take:** richer attributes than DeepFashion2 and CC BY 4.0, so a better default for fashion detection. | 10K–100K images | CC BY 4.0 |
| [`Voxel51/MERL_Shopping_Dataset`](https://huggingface.co/datasets/Voxel51/MERL_Shopping_Dataset), [`Voxel51/retail_gaze`](https://huggingface.co/datasets/Voxel51/retail_gaze) | FiftyOne mirrors of MERL Shopping (shopper action videos) and Retail Gaze. **Take:** only ~41 samples each and no license on the Hub, so demo-scale; use the original sources. (Voxel51's RetailAction mirror duplicates the Standard Cognition entry above, so I skipped it.) | ~41 samples each | none on card; see upstream |

---

## Competition and challenge datasets

Datasets released through competitions. Most have archived leaderboards that serve as reference scores.

| Competition | Year | Task | Data | Link |
|---|---|---|---|---|
| RecSys Challenge 2025 (Synerise) | 2025 | Universal behavioral profiles from e-commerce event logs | 6 months of buys, cart events, page visits, searches | [recsys.synerise.com](https://recsys.synerise.com/) |
| Amazon KDD Cup 2024 | 2024 | Multi-task online shopping for LLMs | ShopBench | [AIcrowd](https://www.aicrowd.com/challenges/amazon-kdd-cup-2024-multi-task-online-shopping-challenge-for-llms) |
| Amazon KDD Cup 2023 — Amazon-M2 | 2023 | Multilingual next-product prediction from sessions (6 locales) | ~3.6M sessions | [kddcup23.github.io](https://kddcup23.github.io/) |
| Amazon KDD Cup 2022 — ESCI | 2022 | Query–product ranking, ESCI classification, substitute detection | Shopping Queries dataset | [github](https://github.com/amazon-science/esci-data) |
| OTTO Multi-Objective Recommender | 2022–23 | Predict clicks, cart additions and orders per session | ~12M sessions, ~220M events (German retailer) | [Kaggle](https://www.kaggle.com/competitions/otto-recommender-system) |
| H&M Personalized Fashion Recommendations | 2022 | Predict next-week purchases | 31M transactions + images | [Kaggle](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations) |
| Shopee — Price Match Guarantee | 2021 | Multimodal product matching (image + title) | ~34K listings | [Kaggle](https://www.kaggle.com/competitions/shopee-product-matching) |
| SIGIR eCom Data Challenges (e.g. Coveo 2021) | 2017– | Session recommendation, cart abandonment, query classification | Coveo browsing + search sessions | [sigir-ecom.github.io](https://sigir-ecom.github.io/) · [Coveo data](https://github.com/coveooss/SIGIR-ecom-data-challenge) |
| M5 Forecasting — Accuracy / Uncertainty | 2020 | Hierarchical daily unit-sales forecasting | Walmart, 3,049 SKUs × 10 stores | [Kaggle](https://www.kaggle.com/competitions/m5-forecasting-accuracy) |
| Corporación Favorita Grocery Sales | 2017–18 | Daily item-store sales forecasting with promotions and oil prices | Ecuador grocery, ~125M rows | [Kaggle](https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting) |
| Instacart Market Basket Analysis | 2017 | Predict reordered products | 3M+ orders | [Kaggle](https://www.kaggle.com/competitions/instacart-market-basket-analysis) |
| Home Depot Product Search Relevance | 2016 | Predict query–product relevance | ~74K pairs | [Kaggle](https://www.kaggle.com/competitions/home-depot-product-search-relevance) |
| CIKM Cup 2016 — DIGINETICA | 2016 | Session-based recommendation and search personalization | ~1.2M sessions | [competitions.codalab.org](https://competitions.codalab.org/competitions/11161) |
| Rossmann Store Sales | 2015 | Daily store-level sales forecasting | 1,115 German drugstores | [Kaggle](https://www.kaggle.com/competitions/rossmann-store-sales) |
| RecSys Challenge 2015 — YOOCHOOSE | 2015 | Predict purchase within click sessions | ~9M sessions | [recsys.acm.org](https://recsys.acm.org/recsys15/challenge/) |
| Walmart Recruiting — Store Sales | 2014 | Weekly department sales with holiday markdowns | 45 stores | [Kaggle](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting) |
| Tmall / Taobao user behavior (Alibaba Tianchi) | — | Repeat-buyer prediction; click/cart/fav/buy logs | ~100M behaviors (Taobao UserBehavior) | [tianchi.aliyun.com](https://tianchi.aliyun.com/dataset/649) |

---

## Classic transactional datasets

These are the long-standing public datasets. Each has a deep-dive page with schema, verified stats and sample rows.

| # | Dataset | Contents | License |
|---|---|---|---|
| 1 | [UCI Online Retail / II](datasets/01-uci-online-retail.md) | UK online gift retailer, 2009–2011, ~1M invoice lines | CC BY 4.0 |
| 2 | [Olist Brazilian E-Commerce](datasets/02-olist-brazilian.md) | ~100K orders 2016–2018, 9 relational tables with reviews and geo data | CC BY-NC-SA 4.0 |
| 3 | [Instacart Online Grocery](datasets/03-instacart.md) | 3M+ orders, 200K users, reorder sequences | Non-commercial, no redistribution |
| 4 | [Amazon Customer Reviews](datasets/04-amazon-reviews.md) | Product reviews and metadata across categories | Research only |
| 5 | [Walmart M5](datasets/05-walmart-m5.md) | Daily unit sales for 3,049 SKUs × 10 stores, with prices and calendar | Kaggle competition rules |
| 6 | [H&M Personalized Fashion](datasets/06-hm-fashion.md) | 2 years of transactions, customer metadata, product images | H&M competition rules |
| 7 | [Dunnhumby Complete Journey](datasets/07-dunnhumby.md) | 2 years of household grocery baskets with promotions and demographics | Academic / non-commercial |
| 8 | [Google Analytics 4 sample](datasets/08-ga4-sample.md) | 3 months of obfuscated event-level data from the Google Merchandise Store (BigQuery) | Google APIs ToS |
| 9 | [US Census Monthly Retail Trade](datasets/09-census-mrts.md) | Monthly retail sales by NAICS, plus quarterly e-commerce | Public domain |
| 10 | [Kaggle E-Commerce Data (UK)](datasets/10-kaggle-uk-ecom.md) | 541K rows, a mirror of UCI Online Retail | CC0 |
| 11 | [Retail Transactions (synthetic)](datasets/11-retail-transactions.md) | Synthetic baskets for prototyping | CC0 |

---

## Choosing by task

| Task | Start with |
|---|---|
| Demand forecasting | M5, Favorita, Rossmann, VN1, `fev_datasets`, `rel-hm` item-sales, Census MRTS |
| Stockouts / censored demand | FreshRetailNet-50K, FreshRetailNet-LT |
| Churn / LTV / purchase prediction | RelBench `rel-amazon` and `rel-hm`, Dunnhumby, Olist |
| Sequential and session recommendation | Amazon Reviews 2023, OTTO, Amazon-M2, Taobao-MM, Synerise, H&M, REES46, RetailRocket, DIGINETICA, YOOCHOOSE, T-ECD |
| Basket / market-basket analysis | Instacart, Dunnhumby, UCI Online Retail |
| Product search and ranking | ESCI, WANDS, Home Depot, SQID, Marqo-GS-10M, Amazon-C4, TREC Product Search |
| Query autocomplete | AmazonQAC |
| Retrieval over structured + text KBs | STaRK-Amazon |
| Relational deep learning / tabular foundation models | RelBench v1/v2, The Join |
| Graph learning | ogbn-products, SNAP Amazon co-purchase |
| Product classification / attribute extraction | Shopify Catalogue, mSOP-765k, ABO |
| Product matching | Shopee Price Match |
| E-commerce knowledge for LLMs | Shopping MMLU, EcomMMMU, ChineseEcomQA, EcomEval, OxyEcomBench, ECInstruct |
| Shopping and customer-service agents | τ²-bench retail, EcomBench, DeepShop, WebMall, ShoppingBench, ShoppingComp, ShoppingReasoningBench, WebShop, grocery-bench |
| Domain-adaptive pretraining | Ecom-niverse, ECInstruct |
| Image retrieval / recognition | Stanford Online Products, Products-10K, ABO, SQID, Marqo GoogleShopping |
| Shelf detection | SKU-110K |
| Fashion | H&M, DeepFashion2, Fashion-IQ, Polyvore Outfits |
| In-store video | RetailAction |

---

## Loading snippets

```python
# Hugging Face (most entries above)
from datasets import load_dataset
reviews = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_All_Beauty", split="full", trust_remote_code=True)
esci    = load_dataset("tasksource/esci", split="train")
catalog = load_dataset("Shopify/product-catalogue", split="train")
```

```python
# RelBench (loads from the stanford-star HF repos)
import relbench
ds   = relbench.load_dataset("rel-hm")
task = ds.load_task("user-churn")
train, val, test = task.get_table("train"), task.get_table("val"), task.get_table("test")
```

```python
# STaRK
from stark_qa import load_qa, load_skb
qa  = load_qa("amazon")
skb = load_skb("amazon", download_processed=True)
```

```python
# OGB
from ogb.nodeproppred import PygNodePropPredDataset
ds = PygNodePropPredDataset(name="ogbn-products")
```

For Kaggle, BigQuery and UCI sources, see [`scripts/fetch_samples.py`](scripts/fetch_samples.py).

---

## Repo layout

| Path | Contents |
|---|---|
| [`datasets/`](datasets/) | Deep-dive page for each classic dataset: schema, verified stats, sample rows, citation |
| [`notebooks/`](notebooks/) | Load → profile → visualize quickstarts (UCI Online Retail, Census MRTS) |
| [`samples/`](samples/) | Small committed samples, only from CC0, CC BY or public-domain sources |
| [`scripts/`](scripts/) | `fetch_samples.py`: downloads open datasets, prints access steps for gated ones |
| [`scorecards/`](scorecards/) | Metric definitions: RFM, delivery SLA, promo lift, forecast accuracy |
| [`regulatory/`](regulatory/data-privacy-reference.md) | Privacy regulations (GDPR, CCPA, LGPD, PCI-DSS) and per-dataset license / PII notes |

## Licensing

The writeups, metric definitions, checklists and code in this repo are licensed under [CC BY 4.0](LICENSE). The datasets are not covered by that license; each keeps its own license, as listed above and on its page.

Only add data to `samples/` if its license allows redistribution. Restricted datasets go in `scratch/`, which is git-ignored.
