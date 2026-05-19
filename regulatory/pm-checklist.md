# Regulatory Checklist for Retail PMs

A one-pager you can paste into your PRD before shipping any feature that uses customer data. Each rule is followed by a "what this means for you" note.

> *(General knowledge throughout, unless explicitly quoted.)*

---

## 1. Major regulations that apply

| Law | Scope | Applies if you… |
|---|---|---|
| **GDPR** (General Data Protection Regulation, EU) | Any data on EU residents | Have EU customers, even one. Penalties up to 4% of global revenue. |
| **CCPA / CPRA** (California) | Personal info of CA residents | >$25M annual revenue, OR process 100K+ CA residents/devices, OR derive ≥50% revenue from selling data. |
| **LGPD** (Brazil) | Brazilian residents | You touch Olist data, or any other Brazilian dataset. Mirrors GDPR closely. |
| **PIPEDA** (Canada) | Canadian residents | You sell into Canada. |
| **PCI-DSS** | Cardholder data (PAN, CVV) | You store, process, or transmit credit-card numbers. |
| **HIPAA** | Health data | You sell health-related products with linked diagnoses (rare in retail). |
| **COPPA** | Children under 13 | You knowingly market to kids. |

---

## 2. Six steps before using a dataset for a feature

Run through these in order. If you can't tick one, stop and talk to legal.

1. **Read the license.** Confirm: (a) commercial use allowed? (b) redistribution allowed? (c) attribution required? Record in your PRD.
2. **Identify PII.** Any column that could re-identify a person: name, email, phone, IP, device ID, postal code (especially when combined with age + gender), purchase history at granular timestamps.
3. **Establish lawful basis** *(GDPR Art. 6)*. Choose one: consent, contract, legal obligation, vital interests, public task, legitimate interest. Document which.
4. **Document the purpose** — narrow and specific. "Customer-experience optimization" is too vague. "Predict next-day reorder probability to power Buy Again carousel" is concrete.
5. **Plan for data-subject rights** — access, rectification, deletion, portability, opt-out of sale, opt-out of profiling. Your data pipeline must support targeted deletion.
6. **Vendor/sub-processor check** — if you ship the data to a third party (ML hosting, analytics, recommendation API), they need a Data Processing Agreement.

---

## 3. Per-dataset compliance notes

| # | Dataset | PII level | Commercial use? | Watch out for |
|---|---|---|---|---|
| 1 | UCI Online Retail | CustomerID (pseudonymous) | ✅ Yes (CC BY 4.0) | Re-identification possible via invoice patterns; treat as pseudonymous personal data under GDPR. |
| 2 | Olist Brazilian | customer_unique_id + zip prefix | ❌ Non-commercial only | LGPD applies. Zip + age combo is re-identifying. Strip before any cross-dataset join. |
| 3 | Instacart | user_id (pseudonymous) | ❌ Non-commercial; no redistribution | License explicitly forbids embedding in commercial products. |
| 4 | Amazon Reviews | user_id (pseudonymous) | ❌ Research only | Joining with other Amazon data → re-identification. Don't share derived models with third parties. |
| 5 | Walmart M5 | None (SKU + store only) | ❌ Competition use | Forecast outputs are fine to use; raw data redistribution is not. |
| 6 | H&M | customer_id + postal hash + age | ❌ Research only | Age + postal_code hash is borderline-identifying. Aggregate before sharing. |
| 7 | Dunnhumby | household_key + demographics | ❌ Academic/non-commercial | Requires registration; T&Cs cover specific deliverables. |
| 8 | GA4 Sample | user_pseudo_id (obfuscated) | ✅ Allowed via Google APIs ToS | Real GA4 export of your own site IS subject to GDPR/CCPA. |
| 9 | US Census MRTS | None (aggregate $) | ✅ Public domain | No PII concerns at all. |
| 10 | Kaggle UK e-com (CC0) | CustomerID | ✅ CC0 — fully open | Still GDPR if you re-identify; CC0 is a *license* status, not a regulatory exemption. |
| 11 | Retail Transactions (synth) | Synthetic | ✅ CC0 | Not real people — no privacy concerns. |

---

## 4. The PII iceberg — what counts as personal data under GDPR

GDPR Article 4(1) defines personal data as "any information relating to an identified or identifiable natural person." This catches more than you'd think:

- **Direct identifiers**: name, email, phone, government ID.
- **Indirect identifiers (still PII)**: pseudonymous customer ID, hashed email, IP address, device fingerprint, cookie ID, GA `user_pseudo_id`.
- **Quasi-identifiers**: zip code + age + gender combination can identify someone in ~85% of US population (Sweeney 2000). Single-purchase records at granular timestamps are often equally identifying.
- **Behavioral data**: location history, browsing history, app usage — protected when linked to an identifier.
- **Inferred data**: predicted income bracket, inferred sexual orientation, predicted pregnancy status. GDPR treats these as PII even though you generated them.

---

## 5. PCI-DSS for retail PMs (cardholder data)

If your feature touches credit-card numbers (PAN), this applies:

- **Never store full PAN unencrypted.** Use tokenization via your payment provider (Stripe / Adyen / Braintree).
- **Never store CVV/CVC** — even temporarily.
- **Reduce scope**: prefer "client-side tokenization" where the card never touches your servers. Cuts your audit scope from PCI Level 1 to SAQ-A.
- **Audit logging**: every read/write to cardholder data must be logged and retained ≥1 year (≥3 months immediately accessible).

The public datasets in this repo only contain `payment_method` strings (e.g., "credit_card", "boleto") — not actual card data. You're safe.

---

## 6. Common landmines for retail PMs

1. **Dark-pattern consent banners** — pre-checked boxes and "agree or leave" are not valid consent under GDPR.
2. **"Anonymized" data that isn't** — joining two pseudonymous datasets often re-identifies individuals. Document your re-identification risk assessment.
3. **Personalization without opt-out** — under GDPR Art. 21, customers can object to profiling. Your feature needs an off switch.
4. **Cross-border data transfers** — sending EU customer data to a US-hosted model needs SCCs (Standard Contractual Clauses) or an adequacy decision.
5. **Children's data** — if you sell toys, candy, or kids' apparel, COPPA (US) and GDPR-K (EU) impose stricter rules.
6. **Behavioral advertising** — the most-contested area under both GDPR and the EU's ePrivacy Directive. Get explicit opt-in.
7. **Loyalty-program data** — counts as profiling. Disclose what's tracked and how it influences pricing or offers.
8. **Returns / chargeback data** — surprisingly PII-rich. Aggregate before sharing dashboards.

---

## 7. Red-flag phrases in a PRD

If you see these in a draft PRD, ask follow-up questions:

| Phrase | Why it's risky |
|---|---|
| "We'll just hash the email" | A hash is still PII; SHA-256 of an email is reversible with a dictionary attack. |
| "It's anonymized" | Define how, what k-anonymity you achieved, who validated. |
| "We have legitimate interest" | Must be documented in a Legitimate Interest Assessment (LIA). |
| "Customers consented in the ToS" | Bundled consent isn't valid under GDPR — must be granular. |
| "We'll only keep it for analytics" | Need a retention period and deletion process. |
| "It's just an internal tool" | Internal tools still need a lawful basis for processing PII. |

---

## 8. Where to escalate

- **Legal** — for novel data sources, cross-border transfers, M&A data handling.
- **Privacy / DPO** — Data Protection Officer is mandatory under GDPR for most retail orgs.
- **Security** — for anything touching cardholder data or production credentials.
- **Trust & Safety** — for review moderation, fake-review detection, fraud signals on customer data.

---

## References (general knowledge from the field)
- GDPR full text: https://gdpr-info.eu/
- CCPA / CPRA: https://oag.ca.gov/privacy/ccpa
- LGPD English summary: https://iapp.org/resources/article/brazilian-data-protection-law-lgpd-english-translation/
- PCI-DSS quick reference: https://www.pcisecuritystandards.org/
- Sweeney, L. (2000), *Simple Demographics Often Identify People Uniquely* — zip+age+gender re-identification result.
