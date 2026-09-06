# СИНЕРГИЯ — IP / Know-how Valuation Dossier V2

> **Статус документа:** внутренняя индикативная оценка для грантового, инвестиционного и регуляторного due diligence.  
> **Дата:** 6 сентября 2026.  
> **Technical IP portfolio:** 45 Federation V3/V3.1 repositories.  
> **Observed Shtenco repositories:** 46, потому что `synergy_project` является отдельным master dossier и **не включается как 46-й runtime/IP domain в техническую сумму**.  
> **Это не независимый appraisal, не аудированная fair value и не цена продажи.**

## 1. Что оценивается

Под IP/know-how здесь понимаются не только строки кода, но и совокупность нематериальных активов:

- source code и архитектура;
- алгоритмы и математические модели;
- schemas, typed contracts и authority/evidence rules;
- Secure Event Fabric + Data Fabric;
- failure/recovery/idempotency/reversal semantics;
- MIDAS models, features, validation lineage, market-graph and execution know-how;
- NEXUS/OLGA/AUTOPILOT reasoning/control lineage;
- Financial OS / MetaPay accounting-settlement know-how;
- PQ blockchain/metachain integration;
- SynergyNet transport/cache/content-addressing;
- archive/compression/dedup/random-access/temporal-model IP;
- XPU/TURBO compute-system designs;
- datasets, benchmark procedures and experimental protocols;
- science falsification/reproducibility workflows;
- product UX/flows, business processes and GovTech traceability schemas;
- documentation, tests, CI, failure-injection scenarios;
- accumulated negative results and engineering decisions that reduce future reproduction cost.

## 2. Методология

Оценка использует гибридную логику раннего technology/IP portfolio:

1. **Replacement / reproduction cost** — основной baseline для pre-production technology.
2. **Current risk-adjusted IP & know-how value** — replacement adjusted for maturity, transferability, overlap, evidence, licensing, security, regulatory and commercial risks.
3. **Market/comparable sanity check** — только когда существует действительно сопоставимая transaction evidence.
4. **Income approach** — только для отделимого и реалистично прогнозируемого cash flow.
5. **Real-options / post-sandbox scenario** — стоимость опциональности после снятия конкретных technical/regulatory/commercial risks.

Для раннего R&D replacement cost может быть выше current buyer value, потому что покупатель принимает риск того, что технология не дойдёт до production/commercial proof.

## 3. Value ≠ company valuation ≠ transaction price

В оценку технического IP не включаются автоматически:

- стоимость юридического лица;
- cash/debt;
- будущая выручка, которая ещё не заработана;
- клиенты/контракты, которых ещё нет;
- regulatory licenses/approvals, которые ещё не получены;
- бренд goodwill без отдельной оценки;
- patents как granted rights, если они ещё не выданы;
- simulated/backtest trading PnL;
- unverified scientific claims;
- `synergy_project` dossier как отдельный runtime technology asset.

## 4. Обновлённая портфельная оценка после полного 46-repo audit

### 4.1 Gross repo-level sum — 45 technical repositories

После детального пересмотра `ai_compress` и `qr_compress`:

- **Replacement / reproduction cost:** **$16.55–45.95M**;
- **Current risk-adjusted IP & know-how:** **$12.45–35.90M**;
- **Post-sandbox option scenario:** **$45.60–129.70M**.

### 4.2 Portfolio overlap adjustment

Repo-level сумма частично дважды считает общий architecture/author know-how и lineage. Для conservative management view сохраняется **25% overlap/correlation haircut**.

После haircut:

- **Replacement / reproduction portfolio:** **$12.41–34.46M**;
- **Current indicative IP & know-how portfolio:** **$9.34–26.93M**;
- **Post-sandbox option portfolio:** **$34.20–97.28M**.

Для внешней презентации разумно округлять:

> **Current technology/IP/know-how portfolio: ~$9–27M.**

> **Independent-team replacement/reproduction range: ~$12–34M.**

> **Post-sandbox option scenario: ~$34–97M.**

Эти диапазоны — internal management estimates, а не предложение купить/продать компанию по указанным значениям.

## 5. Почему Data Fabric переоценён вверх

Предыдущая оценка считала archive repos почти как вспомогательные utilities. Full repository audit показал, что это неверно.

### `ai_compress`

Фактический technology inventory включает:

- EGD-256;
- SABF-X;
- HACE-X;
- TSC-X;
- AMCE-100X;
- UMC-256 + MDL routing;
- Graph-AI Compression V5.2;
- GRAAL-IGC;
- Gabriel Horn `SGH1` — multiscale lifting, significance shells, deduplication, random access, surface-aware MDL;
- Arithmetic coding;
- rANS;
- Huffman;
- Graph Delta;
- Tier-1 benchmark infrastructure;
- exact byte equality + SHA-256 round-trip;
- encode/decode throughput;
- peak RSS;
- random-access cost and access amplification;
- immutable source-snapshot/provenance mechanisms.

Updated internal band:

- **Replacement:** `$0.80–2.50M`;
- **Current IP:** `$0.50–1.80M`;
- **Post-sandbox option:** `$2.00–6.00M`.

### `qr_compress`

Фактический technology inventory включает:

- QTC1 / QTC2;
- QTD1 temporal dictionary;
- timestamp/slot addressing;
- exact / patch / standalone modes;
- residual patch engine;
- COPY/LITERAL operations;
- compact varints;
- MDL codec routing;
- raw/zlib/bz2/LZMA/Zstd/Brotli/rANS + optional Gabriel Horn selection;
- shared model SHA-256;
- final content SHA-256;
- QR frame CRC32;
- QF1 multi-frame out-of-order transport;
- corruption/wrong-model/exact-roundtrip tests;
- benchmark/proof corpus;
- roadmap for QTD2 chunk bank, fountain/Reed–Solomon, Merkle chunk index and random access.

Updated internal band:

- **Replacement:** `$0.40–1.20M`;
- **Current IP:** `$0.30–0.90M`;
- **Post-sandbox option:** `$1.00–3.00M`.

The higher valuation is driven by accumulated algorithmic/benchmark/protocol know-how, not by a claim that either codec is commercially dominant today.

## 6. Updated technology clusters — gross before overlap discount

| Cluster | Replacement | Current IP/know-how | Post-sandbox option |
|---|---:|---:|---:|
| Core financial / trust / network | $5.2–14.0M | $4.35–11.4M | $17.0–44.0M |
| AI / engineering | $2.55–6.8M | $1.95–5.3M | $6.8–18.3M |
| Trading / market intelligence | $2.56–6.8M | $1.97–5.57M | $6.03–16.3M |
| Product / economy / GovTech | $2.0–5.8M | $1.5–4.45M | $6.4–19.7M |
| **Compute / Data Fabric / compression** | **$2.50–7.70M** | **$1.75–5.90M** | **$6.50–20.00M** |
| Monetary / financial R&D | $0.95–2.5M | $0.53–1.75M | $1.4–4.7M |
| Scientific R&D | $0.6–1.9M | $0.28–1.2M | $1.3–6.0M |
| Presentation / legacy client | $0.17–0.46M | $0.10–0.30M | $0.18–0.65M |

Cluster sums are analytical groupings; cross-cluster technology still overlaps, hence the separate portfolio haircut.

## 7. Full valuation of all 45 technical repositories

All values below are **USD millions**.

| # | Repository | Key IP / know-how | Replacement | Current IP | Post-sandbox |
|---:|---|---|---:|---:|---:|
| 1 | `shtenco.github.io` | public provenance / portfolio presentation | 0.03–0.08 | 0.02–0.06 | 0.03–0.10 |
| 2 | `quantum-trading_metatrader5` | quantum-trading experiment lineage | 0.08–0.20 | 0.05–0.15 | 0.10–0.30 |
| 3 | `computer_vision_trading_metatrader_5` | CV/attention market representations | 0.10–0.25 | 0.07–0.20 | 0.15–0.40 |
| 4 | `swap_arbitrage_metatrader_5` | carry/swap portfolio research | 0.08–0.20 | 0.05–0.15 | 0.10–0.30 |
| 5 | `cross_forex_arbitrage_trading_metatrader_5` | cross-rate graph-arbitrage lineage | 0.10–0.25 | 0.07–0.20 | 0.15–0.40 |
| 6 | `global_liquidity_dataminer` | central-bank/global-liquidity feature mining | 0.10–0.30 | 0.08–0.25 | 0.20–0.60 |
| 7 | `3D_bars_market_structure` | volume-time-price 3D representation | 0.12–0.35 | 0.10–0.30 | 0.25–0.70 |
| 8 | `multi_threaded_trading_robot_with_machine_learning_python` | parallel ML trading/runtime patterns | 0.15–0.40 | 0.10–0.30 | 0.20–0.60 |
| 9 | `midas_ai_trading_system` | institutional MIDAS lineage + unified archive know-how | 0.60–1.50 | 0.45–1.20 | 1.20–3.00 |
| 10 | `midas_lite` | compact MIDAS lineage | 0.08–0.20 | 0.04–0.12 | 0.08–0.20 |
| 11 | `turbo_linux` | host/kernel/runtime/virtualization architecture | 0.50–1.50 | 0.35–1.20 | 1.00–3.00 |
| 12 | `agi_olga` | SmallWorld/DSL/OLGA/NEXUS-600K lineage | 0.80–2.00 | 0.60–1.50 | 1.50–4.00 |
| 13 | `ai_coder` | evidence-backed change orchestration target | 0.15–0.40 | 0.10–0.30 | 0.30–0.80 |
| 14 | `ai_trade_terminal` | Cassandra/DataHub/supervisor/operator terminal lineage | 0.15–0.35 | 0.08–0.25 | 0.20–0.60 |
| 15 | `shtencoauantai.github.io` | quant/AI public presentation/provenance | 0.05–0.15 | 0.03–0.10 | 0.05–0.20 |
| 16 | `cashero` | cyclic-liquidity/tokenomics experimental know-how | 0.10–0.30 | 0.05–0.20 | 0.10–0.40 |
| 17 | `ai_language` | repo-aware coding + semantic requirements/traceability | 0.40–1.00 | 0.30–0.80 | 1.00–2.50 |
| 18 | `sinergy-super-app` | native/mobile federation client lineage | 0.20–0.60 | 0.10–0.40 | 0.40–1.20 |
| 19 | `binary_quantum_theory` | mathematical/computational candidate-physics research corpus | 0.40–1.20 | 0.20–0.80 | 0.80–3.00 |
| 20 | `ai_financial_system` | AMM/QE/QT/MEV/orderflow/bridge/solvency R&D | 0.50–1.20 | 0.30–0.90 | 0.80–2.50 |
| 21 | `algotrading_graph_system` | capacity/settlement-aware multi-venue graph | 0.10–0.30 | 0.08–0.25 | 0.40–1.20 |
| 22 | **`ai_compress`** | **multi-codec archive, dedup, random access, Gabriel Horn, Data Fabric** | **0.80–2.50** | **0.50–1.80** | **2.00–6.00** |
| 23 | `synergy_pay_system` | MetaPay routing/compliance/settlement/reconciliation/outbox | 0.70–1.80 | 0.60–1.50 | 2.00–5.00 |
| 24 | `synergy_ai_blockchain` | typed PQ commitments/checkpointing/ML-DSA integration | 0.70–1.80 | 0.55–1.40 | 2.00–5.00 |
| 25 | `synergychain` | Business/Growth OS + multi-agent/business process know-how | 0.50–1.30 | 0.40–1.00 | 1.50–4.00 |
| 26 | `synergychain.github.io` | verified static/public portal distribution | 0.08–0.20 | 0.05–0.12 | 0.10–0.30 |
| 27 | `cold_nuclear` | LENR/transmutation computational/falsification protocols | 0.20–0.70 | 0.08–0.40 | 0.50–3.00 |
| 28 | `usds` | stable-money/reserve/mint-restore falsification R&D | 0.15–0.40 | 0.08–0.25 | 0.20–0.80 |
| 29 | `synergy_financial_os` | double-entry economic truth, HardNAV, solvency/capacity/reversal | 0.90–2.30 | 0.80–2.00 | 3.00–8.00 |
| 30 | `synergy_eurasian` | productive-economy/project/region/industry system dynamics | 0.40–1.20 | 0.30–1.00 | 1.50–5.00 |
| 31 | `synergy_matrix_sota` | household capital/savings/maturity model | 0.20–0.60 | 0.15–0.45 | 0.50–1.50 |
| 32 | `agi_nexus` | bounded reasoning/provenance/UNKNOWN/graph semantics | 0.90–2.50 | 0.70–2.00 | 3.00–8.00 |
| 33 | `midas_ai` | canonical institutional alpha/quality/risk/portfolio/execution intelligence | 0.90–2.50 | 0.80–2.20 | 3.00–8.00 |
| 34 | `synergy_system` | Federation constitution, Contracts, Secure Event + Data Fabric | 0.80–2.20 | 0.70–1.80 | 3.00–7.00 |
| 35 | `nexus_science_agent` | search/evidence/falsification/reproduction/TRL/IP pipeline | 0.30–0.90 | 0.25–0.70 | 1.00–3.00 |
| 36 | `synergynet` | chunk/hash/dedup/cache/P2P/store-forward secure transport | 0.60–1.60 | 0.50–1.30 | 2.00–5.00 |
| 37 | `synergy_meta_os` | node/service/capability/artifact/cache/storage orchestration | 0.50–1.40 | 0.40–1.10 | 1.50–4.00 |
| 38 | `blochain_budget` | public-budget traceability, KBK, Merkle/provenance/archive-node know-how | 0.40–1.20 | 0.30–0.90 | 1.50–5.00 |
| 39 | `agi_autopilot` | bounded policy/capability/approval/action orchestration | 0.50–1.50 | 0.40–1.20 | 2.00–6.00 |
| 40 | `sinergy_app` | legacy placeholder/name lineage | 0.01–0.03 | 0.00–0.02 | 0.00–0.05 |
| 41 | `synergy_app` | Personal Capital store-release product infrastructure | 0.30–0.90 | 0.25–0.70 | 1.00–3.00 |
| 42 | **`qr_compress`** | **QTC1/QTC2/QTD1/QF1 temporal/offline Data Fabric** | **0.40–1.20** | **0.30–0.90** | **1.00–3.00** |
| 43 | `synergy_metachain` | PQ cross-chain/light-client/finality/bridge-proof architecture | 0.50–1.40 | 0.40–1.10 | 1.50–4.00 |
| 44 | `motherboard_xpu_xml` | compiled-graph XPU + content-addressed Persistent State design | 0.80–2.50 | 0.60–2.00 | 2.50–8.00 |
| 45 | `print_money_synergychain` | HardNAV/external-profit/liquidity falsification framework | 0.20–0.60 | 0.10–0.40 | 0.30–1.00 |

## 8. `synergy_project` — intentionally outside the 45-tech valuation

`Shtenco/synergy_project` is the 46th observed repository but acts as:

- regulatory-sandbox dossier;
- grant/investor narrative;
- repository registry;
- valuation/due-diligence package;
- technology audit.

It may have documentation/brand/business-development value, but including it in the technical 45-repository sum would blur the distinction between **IP being valued** and **the dossier describing that IP**. Therefore it is not added to the figures above.

## 9. Highest-value know-how clusters

### 9.1 Federation authority/evidence architecture

Value is in the accumulated process model:

- one-authority-per-fact;
- producer/consumer contracts;
- provenance/causation;
- evidence ladder;
- negative authority tests;
- release promotion rules;
- separation of reasoning, settlement, accounting, transport, archive and trust.

### 9.2 Financial OS economic-truth firewall

- external settlement before external profit;
- HardNAV vs internal marks;
- distributable capacity;
- append-only reversal;
- replay/restatement;
- settlement-backed PnL;
- double-entry close/commitments.

### 9.3 MetaPay settlement architecture

`Intent → Compliance/Funding → Execution → SettlementEvidence → Reconciliation → Receipt → Reversal`.

### 9.4 MIDAS research lineage

- multi-model architecture;
- feature families;
- OOS/walk-forward discipline;
- cost/capacity sensitivity;
- portfolio/risk modelling;
- global-liquidity/graph research;
- failed and successful experiment lineage;
- Unified Data Archive concept now integrated into Data Fabric.

### 9.5 NEXUS + AUTOPILOT separation

- explicit UNKNOWN;
- provenance;
- reasoning ≠ authorization;
- policy/capability gates;
- human/multisig escalation;
- no direct financial authority.

### 9.6 Secure Event Fabric

- immutable signed envelope;
- transactional outbox/inbox;
- persistent replay ledger;
- conflict detection;
- delivery lease recovery;
- DLQ/quarantine;
- compensating flows;
- PQ signer boundary.

### 9.7 Data Fabric — newly recognized core know-how

- dual semantic/archive hash model;
- corpus-aware codec registry;
- lossless exact-roundtrip evidence;
- content addressing + dedup;
- random access;
- shared temporal dictionary/residual transport;
- model/dictionary binding;
- SynergyNet codec negotiation;
- storage tiers;
- blockchain digest binding without bulk on-chain storage;
- future XPU Persistent State integration;
- offline QR transport without authority escalation.

### 9.8 PQ trust / MetaChain

- typed commitments;
- ML-DSA R&D;
- accounting/trust separation;
- light-client/finality/bridge-proof boundaries;
- key rotation/revocation roadmap.

### 9.9 XPU / TURBO

High-option engineering IP, but current value remains discounted by lack of silicon/production-host proof.

### 9.10 Budget / GovTech

- official-source provenance;
- versioned KBK registry;
- strict entity linking;
- Merkle inclusion/anchor path;
- public-only traceability;
- archive/data-node requirement;
- mock-vs-real outcome separation.

### 9.11 Science falsification/reproducibility

`Hypothesis → Falsification → Computation/Experiment → Reproduction → TRL → IP → Commercialization`, backed by content-addressed reproducibility packages.

## 10. What can unlock materially higher value

- literal cross-repo E2E and Data Fabric E2E;
- independent security/codec parser review;
- HSM/KMS/key lifecycle;
- SBOM/license/chain-of-title audit;
- real regulatory sandbox partner;
- repeatable paying customer;
- live-settled MIDAS evidence;
- GovTech pilot with measured outcome;
- Personal Capital cohort KPI;
- production SynergyNet benchmark;
- Data Fabric benchmarks across real Financial/Market/Science/Budget corpora;
- independent codec reproducibility and fuzz/resource tests;
- XPU FPGA/emulation/silicon evidence;
- patents/trade-secret register with clean title;
- external independent IP valuation.

## 11. What can reduce value

- unclear ownership/copyright assignment;
- incompatible OSS licensing;
- leaked keys/secrets;
- only-working implementations living on unmerged branches;
- unreproducible performance claims;
- codec benchmark selection bias;
- decompression/parser security defects;
- weak documentation/transferability;
- scientific overclaims;
- trading results without settlement evidence;
- regulatory architecture that cannot enter sandbox/licensed partnership;
- single-person key-person risk.

## 12. Required formal IP Register

Before independent appraisal, create a machine-readable `IP_REGISTER_V1` for all 45 technical repositories with:

- exact repository + canonical commit;
- author/inventor/contributor;
- copyright ownership evidence;
- contractor assignment evidence where applicable;
- license/SBOM;
- trade-secret classification;
- patent candidate/prior-art state;
- dataset/model rights;
- unique know-how description;
- maturity/TRL;
- reproducibility/test evidence;
- security findings;
- current valuation band;
- overlap group;
- next value-unlock milestone;
- date/assumptions of valuation.

## 13. Recommended external narrative

> **SYNERGY currently comprises 45 technical Federation repositories plus a separate master dossier repository. After a repository-by-repository technology audit, management estimates the current risk-adjusted technology/IP/know-how portfolio at approximately $9–27 million, primarily using replacement-cost and maturity-risk logic. Indicative replacement cost is approximately $12–34 million. A separate post-sandbox real-options scenario is approximately $34–97 million, contingent on technical, regulatory, security, IP-title and commercial evidence gates. These ranges are internal management estimates, not an independent valuation or transaction price.**
