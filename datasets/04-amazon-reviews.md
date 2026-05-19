# 4. Amazon Customer Reviews (Amazon Reviews '23, McAuley Lab)

- **Link**: https://amazon-reviews-2023.github.io/
- **License**: Research-only; redistribution restricted. Each user must download from McAuley Lab / Hugging Face.
- **Sample in this repo**: None. Use [`scripts/fetch_samples.py`](../scripts/fetch_samples.py).

## From the dataset (verbatim from amazon-reviews-2023.github.io)
> "Large-scale Amazon Reviews dataset, collected in 2023 by the McAuley Lab, contains 571.54M reviews, 245.2M users, 48.19M items, and 30.14B review tokens. Covers May 1996 to September 2023."

## Files & Schema *(from dataset documentation)*
Two parallel files per category, gzipped JSONL:

**Reviews** (`<Category>.jsonl.gz`):
| Field | Type | Description |
|---|---|---|
| rating | float | 1.0 – 5.0 stars |
| title | str | Review title |
| text | str | Review body |
| images | list | Embedded image URLs |
| asin | str | Item ID |
| parent_asin | str | Group ID (variants share parent) |
| user_id | str | Reviewer ID |
| timestamp | int | Unix milliseconds |
| verified_purchase | bool | Verified buyer flag |
| helpful_vote | int | "Was this helpful" upvotes |

**Metadata** (`meta_<Category>.jsonl.gz`):
- `main_category, title, average_rating, rating_number, features, description, price, images, videos, store, categories, details, parent_asin, bought_together`

## Scale *(from documentation)*
- 33 product categories: All_Beauty, Amazon_Fashion, Books, Electronics, Home_and_Kitchen, etc.
- 571.54M reviews, 48.19M items, 54.51M users, ~30B tokens of text.
- Categories range from <1M (All_Beauty) to >50M reviews (Books, Electronics).

## Representative sample row *(General knowledge — schema-faithful)*
```json
{
  "rating": 5.0,
  "title": "Worth every penny",
  "text": "Sound is surprisingly full for the size. Alexa picks up my voice from the next room.",
  "asin": "B07FZ8S74R",
  "parent_asin": "B07FZ8S74R",
  "user_id": "AGKHLEW2SOWHNMFQIJGBECAF7INQ",
  "timestamp": 1697822400000,
  "verified_purchase": true,
  "helpful_vote": 27,
  "images": []
}
```

## How a Retail PM uses this *(General knowledge)*
1. **Voice-of-customer themes per category** — topic modeling (BERTopic / LDA) on review text → roadmap signal ("what do shoppers complain about for kitchen knives?").
2. **Aspect-based sentiment** — extract aspect–opinion pairs ("battery life: short", "fit: runs small") to feed PDP improvements and supplier-quality conversations.
3. **Competitor benchmarking** — pull reviews for competing SKUs (same parent_asin grouping or same category) and compare complaint clusters quantitatively.
4. **Review-quality / fake-review detection** — `verified_purchase=False` reviews with extreme polarity are the easy training set; production models add temporal burst and user-graph signals.
5. **Image-text alignment** — review images + text → multimodal model fine-tuning for visual search.
6. **Pricing perception** — match `price` in metadata to review sentiment over time; quantify the "price-up complaint" effect.
7. **Star-rating drift** — `average_rating` is point-in-time; reconstruct true rating curves from review timestamps to detect quality regressions.

## Gotchas
- **No PII**, but `user_id` is consistent across reviews — re-identification risk if cross-joined with other Amazon data. Don't ship to third parties.
- Item metadata is **scraped at a single point in time**; prices and titles may be stale relative to the reviews.
- Books and Electronics categories dominate. Be careful generalizing tone/length stats across categories.
- The 2023 version supersedes the older 2018 release; columns are similar but not identical.
