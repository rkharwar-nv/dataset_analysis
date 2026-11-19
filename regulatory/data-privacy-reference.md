# Data Privacy and Licensing Reference for Retail Data

A summary of the privacy regulations and license terms that apply to retail and e-commerce datasets, including the datasets indexed in this repo. This is general information, not legal advice.

---

## 1. Major regulations

| Law | Scope | Applies when |
|---|---|---|
| **GDPR** (EU General Data Protection Regulation) | Any data on EU residents | Data covers EU residents, regardless of where the processor is located. Penalties up to 4% of global revenue. |
| **CCPA / CPRA** (California) | Personal information of CA residents | Business has >$25M annual revenue, OR processes 100K+ CA residents/devices, OR derives ≥50% of revenue from selling data. |
| **LGPD** (Brazil) | Brazilian residents | Data covers Brazilian residents (e.g. Olist). Closely mirrors GDPR. |
| **PIPEDA** (Canada) | Canadian residents | Data covers Canadian residents in a commercial context. |
| **PCI-DSS** | Cardholder data (PAN, CVV) | Credit-card numbers are stored, processed or transmitted. |
| **HIPAA** | Protected health information | Health products linked to diagnoses (rare in retail). |
| **COPPA** | Children under 13 | Data is knowingly collected from children. |

---

## 2. Checks before using a dataset

1. **License** — is commercial use allowed? Is redistribution allowed? Is attribution required?
2. **Personal data** — which columns could re-identify a person: name, email, phone, IP, device ID, postal code (especially combined with age and gender), purchase history at granular timestamps.
3. **Lawful basis** *(GDPR Art. 6)* — consent, contract, legal obligation, vital interests, public task or legitimate interest.
4. **Purpose limitation** — personal data should be processed for a specific, stated purpose. "Predict next-order reorder probability" is specific; "customer-experience optimization" is not.
5. **Data-subject rights** — access, rectification, deletion, portability, opt-out of sale, opt-out of profiling. Pipelines need to support targeted deletion.
6. **Sub-processors** — third parties that receive the data (ML hosting, analytics, recommendation APIs) need a Data Processing Agreement.

---

## 3. Per-dataset notes

| # | Dataset | Identifiers | Commercial use | Notes |
|---|---|---|---|---|
| 1 | UCI Online Retail | CustomerID (pseudonymous) | ✅ Yes (CC BY 4.0) | Re-identification possible via invoice patterns; treated as pseudonymous personal data under GDPR. |
| 2 | Olist Brazilian | customer_unique_id + zip prefix | ❌ Non-commercial only | LGPD applies. Zip + other attributes can be re-identifying. |
| 3 | Instacart | user_id (pseudonymous) | ❌ Non-commercial; no redistribution | License forbids use in commercial products. |
| 4 | Amazon Reviews | user_id (pseudonymous) | ❌ Research only | Joining with other Amazon data raises re-identification risk. |
| 5 | Walmart M5 | None (SKU + store only) | ❌ Competition use | Raw data redistribution not permitted. |
| 6 | H&M | customer_id + postal hash + age | ❌ Research only | Age + postal-code hash is borderline-identifying. |
| 7 | Dunnhumby | household_key + demographics | ❌ Academic / non-commercial | Requires registration. |
| 8 | GA4 Sample | user_pseudo_id (obfuscated) | ✅ Google APIs ToS | A real GA4 export of a live site is subject to GDPR/CCPA. |
| 9 | US Census MRTS | None (aggregates) | ✅ Public domain | No personal data. |
| 10 | Kaggle UK e-com (CC0) | CustomerID | ✅ CC0 | CC0 is a license status, not a regulatory exemption; GDPR still applies to re-identified data. |
| 11 | Retail Transactions (synthetic) | Synthetic | ✅ CC0 | Not real people. |

For the Hugging Face and Stanford datasets listed in the main [README](../README.md), the license column there is taken from each dataset card. Several (Amazon Reviews 2023, The Join, RelBench) inherit upstream terms per database.

---

## 4. What counts as personal data under GDPR

GDPR Article 4(1) defines personal data as "any information relating to an identified or identifiable natural person." This includes:

- **Direct identifiers**: name, email, phone, government ID.
- **Indirect identifiers**: pseudonymous customer ID, hashed email, IP address, device fingerprint, cookie ID, GA `user_pseudo_id`.
- **Quasi-identifiers**: zip code + age + gender identifies ~87% of the US population (Sweeney 2000). Single-purchase records at granular timestamps are often equally identifying.
- **Behavioral data**: location history, browsing history, app usage, when linked to an identifier.
- **Inferred data**: predicted income bracket, inferred sexual orientation, predicted pregnancy status. Treated as personal data even though it is derived.

---

## 5. PCI-DSS (cardholder data)

- Full PAN must not be stored unencrypted; tokenization via a payment provider is the usual approach.
- CVV/CVC must never be stored, even temporarily.
- Client-side tokenization (card data never touches the merchant's servers) reduces audit scope from PCI Level 1 to SAQ-A.
- Access to cardholder data must be logged, with logs retained ≥1 year (≥3 months immediately accessible).

None of the public datasets in this repo contain card data; they contain only `payment_method` strings such as `credit_card` or `boleto`.

---

## 6. Common pitfalls

1. **Pseudonymous ≠ anonymous** — joining two pseudonymous datasets often re-identifies individuals.
2. **Hashing is not anonymization** — a SHA-256 of an email can be reversed with a dictionary attack.
3. **Bundled consent** — consent buried in terms of service is not valid under GDPR; it must be granular.
4. **Profiling without opt-out** — GDPR Art. 21 gives data subjects the right to object to profiling, including personalization.
5. **Cross-border transfers** — moving EU personal data to a US-hosted service requires Standard Contractual Clauses or an adequacy decision.
6. **Children's data** — toys, candy and kids' apparel data may fall under COPPA (US) and GDPR Art. 8 (EU).
7. **Behavioral advertising** — the most contested area under GDPR and the ePrivacy Directive; generally requires explicit opt-in.
8. **Loyalty-program data** — counts as profiling when it influences pricing or offers.
9. **Returns and chargeback data** — often contains addresses and free-text notes; aggregate before sharing.

---

## References
- GDPR full text: https://gdpr-info.eu/
- CCPA / CPRA: https://oag.ca.gov/privacy/ccpa
- LGPD English translation: https://iapp.org/resources/article/brazilian-data-protection-law-lgpd-english-translation/
- PCI-DSS: https://www.pcisecuritystandards.org/
- Sweeney, L. (2000), *Simple Demographics Often Identify People Uniquely*.
