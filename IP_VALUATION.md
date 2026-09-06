# СИНЕРГИЯ — IP / Know-how Valuation Dossier

> **Статус документа:** внутренняя индикативная оценка для грантового, инвестиционного и регуляторного due diligence.  
> **Дата:** 6 сентября 2026.  
> **Портфель:** 45 репозиториев Federation V3.  
> **Это не независимый appraisal, не аудированная fair value и не цена продажи.**

## 1. Что оценивается

Под IP/know-how здесь понимаются не только строки кода, но и совокупность нематериальных активов:

- исходный код и архитектура;
- алгоритмы и математические модели;
- схемы данных и typed contracts;
- federation authority/evidence model;
- Secure Event Fabric и failure/recovery semantics;
- модели MIDAS, feature engineering, validation lineage и execution know-how;
- NEXUS/AUTOPILOT reasoning/control architecture;
- Financial OS / MetaPay accounting-settlement know-how;
- PQ blockchain/metachain integration know-how;
- SynergyNet transport/runtime architecture;
- XPU/TURBO compute-system designs;
- datasets, benchmark procedures и experimental protocols;
- научные гипотезы, модели и воспроизводимые протоколы;
- product UX/flows, business process models и GovTech traceability schemas;
- документация, tests, CI, failure-injection scenarios и accumulated engineering decisions.

## 2. Методология

Оценка следует общей логике WIPO для ранней IP: cost/replacement approach, market/comparable approach, income approach и real-options analysis. Для pre-production технологий наибольший вес здесь имеет **replacement/reproduction cost**, потому что будущий доход ещё не доказан. Market/income используются только как sanity-check и как post-sandbox scenario, а не как основание для сегодняшней цены.

### 2.1 Replacement / Reproduction Cost

Индикативная стоимость воспроизведения технологии третьей стороной с нуля, включая:

- R&D engineering time;
- архитектурные итерации и отрицательные результаты;
- тесты и tooling;
- data/model preparation;
- security/reliability work;
- documentation and integration effort;
- повторение уже накопленного доменного know-how.

Это **не сумма исторических расходов пользователя**. Это ориентир стоимости повторного создания сопоставимого результата.

### 2.2 Current Risk-Adjusted IP & Know-how Value

Replacement-cost band корректируется на:

- зрелость и evidence;
- уникальность/дифференциацию;
- transferability;
- external dependency risk;
- licensing/open-source composition;
- регуляторный риск;
- commercial proof;
- степень дублирования с другими repo;
- необходимость дальнейших инвестиций.

У ранних R&D активов эта величина может быть **ниже стоимости воспроизведения**, потому что покупатель принимает технический и коммерческий риск.

### 2.3 Post-Sandbox Option Value

Это **не сегодняшняя стоимость**. Это scenario band при выполнении доказательных gates, например:

- literal multi-repo E2E;
- security review;
- legal/sandbox perimeter;
- pilot KPI;
- live-settled evidence;
- repeatable customer demand;
- ownership/IP-chain audit;
- production key custody / HSM-KMS;
- independent reproduction для science tracks.

Эта колонка показывает экономическую ценность опциональности, если существенная часть технологического риска снимается.

## 3. Важное различие: стоимость IP ≠ стоимость компании

Enterprise value компании может быть существенно выше или ниже стоимости IP-портфеля. В EV также входят:

- команда;
- бренд;
- contracts/customers;
- distribution;
- licenses;
- cash;
- revenue;
- regulatory approvals;
- partnerships;
- execution capability.

Эти факторы в приведённые ниже цифры **не включены**, если они не воплощены непосредственно в оцениваемом know-how.

## 4. Портфельная оценка

### Gross repo-level sum

Если механически сложить 45 индивидуальных диапазонов:

- **Replacement / reproduction cost:** примерно **$15.7–43.3 млн**;
- **Current risk-adjusted IP & know-how:** примерно **$11.9–34.0 млн**;
- **Post-sandbox option value:** примерно **$43.5–123.4 млн**.

### Portfolio-adjusted range

Простое сложение завышает сумму из-за общих компонентов, общего автора, общего know-how и lineage. Поэтому для портфельной оценки применяется **25% overlap/correlation discount**.

После такого haircut:

- **Replacement / reproduction portfolio:** примерно **$11.8–32.5 млн**;
- **Current indicative IP & know-how portfolio:** примерно **$8.9–25.5 млн**;
- **Post-sandbox option portfolio:** примерно **$32.6–92.5 млн**.

Для внешней презентации разумно округлять до:

> **Текущая индикативная стоимость технологического IP/know-how портфеля СИНЕРГИИ: $9–26 млн.**

> **Индикативная стоимость воспроизведения портфеля независимой командой: $12–32 млн.**

> **Сценарная post-sandbox option value при прохождении evidence gates: $33–93 млн.**

Это не предложение купить/продать проект по указанным значениям.

## 5. Оценка по технологическим кластерам — gross, до overlap discount

| Кластер | Replacement cost | Current IP/know-how | Post-sandbox option |
|---|---:|---:|---:|
| Core financial / trust / network | $5.2–14.0M | $4.35–11.4M | $17.0–44.0M |
| AI / engineering | $2.55–6.8M | $1.95–5.3M | $6.8–18.3M |
| Trading / market intelligence | $2.56–6.8M | $1.97–5.57M | $6.03–16.3M |
| Product / economy / GovTech | $2.0–5.8M | $1.5–4.45M | $6.4–19.7M |
| Compute / data | $1.65–5.05M | $1.2–4.0M | $4.4–13.7M |
| Monetary / financial R&D | $0.95–2.5M | $0.53–1.75M | $1.4–4.7M |
| Scientific R&D | $0.6–1.9M | $0.28–1.2M | $1.3–6.0M |
| Presentation / legacy client | $0.17–0.46M | $0.10–0.30M | $0.18–0.65M |

## 6. Полная оценка 45 репозиториев

Все суммы ниже — **USD millions**.

| # | Репозиторий | Ключевой IP / know-how | Replacement | Current IP | Post-sandbox option |
|---:|---|---|---:|---:|---:|
| 1 | `shtenco.github.io` | public provenance / portfolio presentation | 0.03–0.08 | 0.02–0.06 | 0.03–0.10 |
| 2 | `quantum-trading_metatrader5` | trading experiment lineage | 0.08–0.20 | 0.05–0.15 | 0.10–0.30 |
| 3 | `computer_vision_trading_metatrader_5` | CV market representations | 0.10–0.25 | 0.07–0.20 | 0.15–0.40 |
| 4 | `swap_arbitrage_metatrader_5` | carry/swap portfolio research | 0.08–0.20 | 0.05–0.15 | 0.10–0.30 |
| 5 | `cross_forex_arbitrage_trading_metatrader_5` | cross-rate graph arbitrage lineage | 0.10–0.25 | 0.07–0.20 | 0.15–0.40 |
| 6 | `global_liquidity_dataminer` | macro/global-liquidity feature mining | 0.10–0.30 | 0.08–0.25 | 0.20–0.60 |
| 7 | `3D_bars_market_structure` | volume-time-price representation | 0.12–0.35 | 0.10–0.30 | 0.25–0.70 |
| 8 | `multi_threaded_trading_robot_with_machine_learning_python` | parallel ML trading architecture | 0.15–0.40 | 0.10–0.30 | 0.20–0.60 |
| 9 | `midas_ai_trading_system` | large institutional MIDAS lineage, validation and multi-agent know-how | 0.60–1.50 | 0.45–1.20 | 1.20–3.00 |
| 10 | `midas_lite` | compact MIDAS lineage | 0.08–0.20 | 0.04–0.12 | 0.08–0.20 |
| 11 | `turbo_linux` | host/kernel/runtime/virtualization architecture | 0.50–1.50 | 0.35–1.20 | 1.00–3.00 |
| 12 | `agi_olga` | OLGA/Cybernetic/Logic/SmallWorld/NEXUS reasoning lineage | 0.80–2.00 | 0.60–1.50 | 1.50–4.00 |
| 13 | `ai_coder` | evidence-backed repository change orchestration | 0.15–0.40 | 0.10–0.30 | 0.30–0.80 |
| 14 | `ai_trade_terminal` | institutional trading-terminal lineage | 0.15–0.35 | 0.08–0.25 | 0.20–0.60 |
| 15 | `shtencoauantai.github.io` | quant/AI public presentation and provenance | 0.05–0.15 | 0.03–0.10 | 0.05–0.20 |
| 16 | `cashero` | cyclic-liquidity/tokenomics experimental know-how | 0.10–0.30 | 0.05–0.20 | 0.10–0.40 |
| 17 | `ai_language` | semantic requirements, repo understanding, traceability | 0.40–1.00 | 0.30–0.80 | 1.00–2.50 |
| 18 | `sinergy-super-app` | native federation client/super-app lineage | 0.20–0.60 | 0.10–0.40 | 0.40–1.20 |
| 19 | `binary_quantum_theory` | mathematical/spectral candidate-physics framework and research corpus | 0.40–1.20 | 0.20–0.80 | 0.80–3.00 |
| 20 | `ai_financial_system` | AMM/QE/QT/MEV/AI-central-bank experimental corpus | 0.50–1.20 | 0.30–0.90 | 0.80–2.50 |
| 21 | `algotrading_graph_system` | capacitated multi-venue graph architecture | 0.10–0.30 | 0.08–0.25 | 0.40–1.20 |
| 22 | `ai_compress` | compression/dedup/content-addressed archive know-how | 0.20–0.60 | 0.15–0.45 | 0.50–1.50 |
| 23 | `synergy_pay_system` | MetaPay lifecycle, settlement, reconciliation, transactional outbox | 0.70–1.80 | 0.60–1.50 | 2.00–5.00 |
| 24 | `synergy_ai_blockchain` | typed PQ commitments, checkpointing, ML-DSA integration | 0.70–1.80 | 0.55–1.40 | 2.00–5.00 |
| 25 | `synergychain` | Business/Growth OS, CRM/SMM/Sales/AI-CFO/control-plane design | 0.50–1.30 | 0.40–1.00 | 1.50–4.00 |
| 26 | `synergychain.github.io` | public portal/presentation layer | 0.08–0.20 | 0.05–0.12 | 0.10–0.30 |
| 27 | `cold_nuclear` | LENR/transmutation hypotheses, materials and falsification protocols | 0.20–0.70 | 0.08–0.40 | 0.50–3.00 |
| 28 | `usds` | stable-money/reserve/mint-restore R&D | 0.15–0.40 | 0.08–0.25 | 0.20–0.80 |
| 29 | `synergy_financial_os` | double-entry economic truth, HardNAV, solvency, capacity, reversal accounting | 0.90–2.30 | 0.80–2.00 | 3.00–8.00 |
| 30 | `synergy_eurasian` | productive-economy/project/region/industry system-dynamics know-how | 0.40–1.20 | 0.30–1.00 | 1.50–5.00 |
| 31 | `synergy_matrix_sota` | household capital/savings/maturity model | 0.20–0.60 | 0.15–0.45 | 0.50–1.50 |
| 32 | `agi_nexus` | bounded reasoning, provenance, UNKNOWN, typed graph semantics | 0.90–2.50 | 0.70–2.00 | 3.00–8.00 |
| 33 | `midas_ai` | canonical institutional alpha/quality/risk/portfolio/execution intelligence | 0.90–2.50 | 0.80–2.20 | 3.00–8.00 |
| 34 | `synergy_system` | Federation constitution, authority/evidence graph, Contracts and Secure Event Fabric | 0.80–2.20 | 0.70–1.80 | 3.00–7.00 |
| 35 | `nexus_science_agent` | hypothesis→falsification→experiment→TRL→IP pipeline | 0.30–0.90 | 0.25–0.70 | 1.00–3.00 |
| 36 | `synergynet` | secure evidence transport, durable store-forward, replay/retry semantics | 0.60–1.60 | 0.50–1.30 | 2.00–5.00 |
| 37 | `synergy_meta_os` | runtime/node/service capability orchestration and persistent routing | 0.50–1.40 | 0.40–1.10 | 1.50–4.00 |
| 38 | `blochain_budget` | public-budget/procurement traceability, Merkle audit, anomaly/ROI model | 0.40–1.20 | 0.30–0.90 | 1.50–5.00 |
| 39 | `agi_autopilot` | bounded policy/capability/approval/action orchestration | 0.50–1.50 | 0.40–1.20 | 2.00–6.00 |
| 40 | `sinergy_app` | legacy placeholder / naming lineage | 0.01–0.03 | 0.00–0.02 | 0.00–0.05 |
| 41 | `synergy_app` | Personal Capital product: budget/reserve/debt/investing/goals | 0.30–0.90 | 0.25–0.70 | 1.00–3.00 |
| 42 | `qr_compress` | compact/offline identity/payment/evidence payload R&D | 0.15–0.45 | 0.10–0.35 | 0.40–1.20 |
| 43 | `synergy_metachain` | PQ cross-chain/light-client/finality/bridge-proof architecture | 0.50–1.40 | 0.40–1.10 | 1.50–4.00 |
| 44 | `motherboard_xpu_xml` | compiled-graph/global-wavefront XPU architecture | 0.80–2.50 | 0.60–2.00 | 2.50–8.00 |
| 45 | `print_money_synergychain` | HardNAV/external-profit/liquidity falsification framework | 0.20–0.60 | 0.10–0.40 | 0.30–1.00 |

## 7. Наиболее ценные know-how assets

### 7.1 Federation authority/evidence architecture

Уникальная ценность не в YAML-файле как таковом, а в накопленной модели:

- one-authority-per-fact;
- producer/consumer contracts;
- provenance/causation;
- evidence ladder;
- negative authority tests;
- release promotion rules;
- separation of reasoning, settlement, accounting and trust.

### 7.2 Financial OS economic-truth firewall

Ключевое know-how:

- external settlement before external profit;
- HardNAV vs internal mark;
- distributable capacity;
- append-only reversal accounting;
- replay/restatement;
- settlement-backed PnL;
- double-entry close and commitments.

### 7.3 MetaPay settlement architecture

Ценность создаёт не payment UI, а разложение payment lifecycle на:

`Intent → FundingReservation → Execution → SettlementEvidence → Reconciliation → Receipt → Reversal`.

### 7.4 MIDAS research lineage

Особая стоимость находится в accumulated research process:

- multi-model architecture;
- feature families;
- OOS/walk-forward discipline;
- cost/capacity sensitivity;
- portfolio/risk modelling;
- global-liquidity graph;
- lineage of failed and successful experiments.

### 7.5 NEXUS + AUTOPILOT separation

Коммерчески ценная идея — не просто AI agent, а bounded AI governance:

- explicit UNKNOWN;
- provenance;
- reasoning ≠ authorization;
- policy/capability gates;
- human/multisig escalation;
- denial of direct financial authority.

### 7.6 Secure Event Fabric

Ключевое know-how:

- immutable signed contract envelope;
- transactional outbox/inbox;
- persistent replay ledger;
- conflicting-replay detection;
- delivery lease recovery;
- DLQ/quarantine;
- compensation instead of history rewrite;
- SynergyNet opaque transport;
- PQ signature provider boundary.

### 7.7 PQ trust / metachain integration

Value drivers:

- typed commitment model;
- ML-DSA event signing R&D;
- separation of blockchain commitment from accounting authority;
- light-client/finality/bridge-proof contracts;
- key-rotation/revocation roadmap.

### 7.8 XPU / TURBO

High-option engineering IP:

- compiled graph execution;
- global wavefront placement;
- chiplet/cluster/tile/lane/cycle mapping;
- radix-switch scheduling;
- host/runtime/virtualization substrate.

Текущая value сильно дисконтируется отсутствием silicon proof и production host proof, но successful hardware/emulation evidence может резко увеличить option value.

### 7.9 Blockchain Budget / GovTech

Know-how включает:

- budget→procurement→payment→delivery causal trace;
- Merkle evidence;
- anomaly modelling;
- mock-vs-real outcome separation;
- state ROI methodology.

### 7.10 Science falsification pipeline

Ценность `nexus_science_agent` — не конкретная смелая гипотеза, а process IP:

`Hypothesis → Falsification → Experiment → Reproduction → TRL → IP → Commercialization`.

Это снижает риск научного overclaim и даёт переносимый technology-transfer workflow.

## 8. Что может увеличить оценку в 2–5 раз по отдельным активам

- literal multi-repo E2E evidence;
- independent security review;
- production HSM/KMS and key lifecycle;
- licensed sandbox partner;
- repeatable paying customer;
- audited revenue attribution;
- independently reproducible MIDAS live-settled edge;
- GovTech pilot with measured audit-cost reduction;
- user cohort showing measurable Personal Capital outcomes;
- production SynergyNet benchmark;
- XPU FPGA/emulation/silicon evidence;
- granted or strategically filed patents with clean chain of title;
- licensable datasets/model artifacts with documented rights.

## 9. Что может уменьшить оценку

- unclear copyright/IP ownership;
- contractor contributions without assignment;
- incompatible OSS licenses;
- leaked secrets/private keys;
- unreproducible results;
- non-canonical branches containing the only working implementation;
- missing tests/CI;
- scientific claims without independent reproduction;
- trading results without external settlement evidence;
- dependence on a single person without documentation/transfer plan;
- regulatory model that cannot be licensed or sandboxed;
- lack of buyer/customer validation.

## 10. IP due-diligence work required before external appraisal

1. Create a formal `IP_REGISTER` for all 45 repositories.
2. Bind author/contributor/contractor ownership evidence.
3. Run OSS/SBOM/license audit.
4. Classify each asset as copyright / trade secret / patent candidate / trademark / dataset / model / documentation / process know-how.
5. Identify patentable claims and perform prior-art search.
6. Create secret-remediation and key-rotation evidence.
7. Freeze exact valuation commit/hash per repo.
8. Build repository-level reproduction-cost worksheet.
9. Add commercial comparables where real transaction data exists.
10. Add income valuation only after separable cash flows exist.
11. Commission independent valuation before using the values in audited accounts, collateral, M&A or formal financing documents.

## 11. Recommended external narrative

For grants/investors, use the conservative statement:

> **Federation V3 contains 45 repositories and an internally estimated current technology/IP/know-how portfolio value of approximately $9–26 million, based primarily on risk-adjusted replacement-cost analysis. A separate post-sandbox option scenario is approximately $33–93 million, contingent on technical, regulatory, security and commercial evidence gates. These ranges are internal management estimates, not an independent valuation or transaction price.**

This wording preserves upside without representing unverified future value as current fact.
