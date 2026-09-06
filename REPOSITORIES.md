# СИНЕРГИЯ — полный реестр: 45 технических репозиториев + master dossier

> Открытая карта для грантового, инвестиционного и регуляторного due diligence.  
> Срез: 6 сентября 2026.  
> **Technical Federation V3:** 45 репозиториев.  
> **Master dossier:** `Shtenco/synergy_project`.  
> **Observed Shtenco repositories total:** 46.  
> Архитектурный источник: `Shtenco/synergy_system` / Federation V3 → V3.1 Data Fabric candidate.

## Как читать таблицу

- **CANONICAL / TARGET** — целевой домен или источник конкретной authority.
- **R&D SOURCE / TARGET** — исследовательская ветка, источник технологий или экспериментальный контур.
- **LEGACY** — историческая линия, из которой полезные технологии мигрируют в canonical target только через evidence gates.
- **PRESENTATION / CLIENT / DOSSIER** — интерфейс, публичная витрина или портфельный документ; не источник финансовой/исполнительной истины.
- **Authority = NONE** означает отсутствие самостоятельной бухгалтерской, платёжной, инвестиционной, governance или scientific-truth authority.

## Все 45 технических репозиториев Федерации

| # | Репозиторий | Слой | Класс / статус | Роль и migration target | Authority |
|---:|---|---|---|---|---|
| 1 | [Shtenco/shtenco.github.io](https://github.com/Shtenco/shtenco.github.io) | Presentation | PUBLIC_PROVENANCE | Персональная исследовательская/публичная витрина | NONE |
| 2 | [Shtenco/quantum-trading_metatrader5](https://github.com/Shtenco/quantum-trading_metatrader5) | Trading | LEGACY_RND | Qiskit/MT5 trading experiment → evidence-gated `midas_ai` research source | NONE |
| 3 | [Shtenco/computer_vision_trading_metatrader_5](https://github.com/Shtenco/computer_vision_trading_metatrader_5) | Trading features | R&D_SOURCE | RGB market representation + attention/CNN/LSTM → MIDAS vision feature layer | NONE |
| 4 | [Shtenco/swap_arbitrage_metatrader_5](https://github.com/Shtenco/swap_arbitrage_metatrader_5) | Trading | R&D_SOURCE | Carry/swap portfolio research → MIDAS carry module; historical returns must be revalidated | NONE |
| 5 | [Shtenco/cross_forex_arbitrage_trading_metatrader_5](https://github.com/Shtenco/cross_forex_arbitrage_trading_metatrader_5) | Trading graph | R&D_SOURCE | Synthetic cross-rate graph → `algotrading_graph_system` + MIDAS | NONE |
| 6 | [Shtenco/global_liquidity_dataminer](https://github.com/Shtenco/global_liquidity_dataminer) | Macro / Trading data | R&D_SOURCE | Central-bank/global-liquidity features → MIDAS + Eurasian/system stress scenarios | NONE |
| 7 | [Shtenco/3D_bars_market_structure](https://github.com/Shtenco/3D_bars_market_structure) | Trading data | R&D_SOURCE | Volume-time-price 3D representation → MIDAS feature/visualization layer | NONE |
| 8 | [Shtenco/multi_threaded_trading_robot_with_machine_learning_python](https://github.com/Shtenco/multi_threaded_trading_robot_with_machine_learning_python) | Trading runtime | R&D_SOURCE | XGBoost/GMM/multi-worker/risk/logging patterns → MIDAS runtime/validation | NONE |
| 9 | [Shtenco/midas_ai_trading_system](https://github.com/Shtenco/midas_ai_trading_system) | Trading | R&D_SOURCE | Large institutional MIDAS lineage; Level 8 Unified Data Archive migrates into Data Fabric | NONE |
| 10 | [Shtenco/midas_lite](https://github.com/Shtenco/midas_lite) | Trading | LEGACY_SOURCE | Lightweight MIDAS lineage | NONE |
| 11 | [Shtenco/turbo_linux](https://github.com/Shtenco/turbo_linux) | Host / Compute | ACTIVE_R&D_TARGET | Clean-room host/kernel/runtime/virtualization substrate | `host_kernel` |
| 12 | [Shtenco/agi_olga](https://github.com/Shtenco/agi_olga) | AI | ACTIVE_R&D_SOURCE | SmallWorld/DSL/NEXUS-600K/OLGA lineage → evidence-gated `agi_nexus` | NONE |
| 13 | [Shtenco/ai_coder](https://github.com/Shtenco/ai_coder) | Engineering | ENGINEERING_CONTROL_TARGET | Evidence-backed code-change/review orchestration; current main remains minimal | `engineering_change_evidence` |
| 14 | [Shtenco/ai_trade_terminal](https://github.com/Shtenco/ai_trade_terminal) | Trading app/runtime | LEGACY_SOURCE | Cassandra supervisor/DataHub/WebSocket/watchdog → MIDAS operator console + Meta-OS/SynergyNet patterns | NONE |
| 15 | [Shtenco/shtencoauantai.github.io](https://github.com/Shtenco/shtencoauantai.github.io) | Presentation | PUBLIC_PROVENANCE | Quant/AI public showcase | NONE |
| 16 | [Shtenco/cashero](https://github.com/Shtenco/cashero) | Monetary R&D | LEGACY_TOKENOMIC_RND | Cyclic-liquidity/Polygon robot lineage; no production promotion without security/economic revalidation | NONE |
| 17 | [Shtenco/ai_language](https://github.com/Shtenco/ai_language) | Engineering | ENGINEERING_CORE | Repository-aware coding + semantic requirement/impact/change graphs | `requirements_semantics` |
| 18 | [Shtenco/sinergy-super-app](https://github.com/Shtenco/sinergy-super-app) | Application | APPLICATION_CLIENT | Mobile federation client lineage | NONE |
| 19 | [Shtenco/binary_quantum_theory](https://github.com/Shtenco/binary_quantum_theory) | Science | SCIENTIFIC_R&D | Candidate mathematical/computational gravity framework; no experimental-confirmation authority | NONE |
| 20 | [Shtenco/ai_financial_system](https://github.com/Shtenco/ai_financial_system) | Financial R&D | R&D_SOURCE | AMM/QE/QT/MEV/orderflow/bridge/solver/solvency experiments → MetaPay/MIDAS/trust research | NONE |
| 21 | [Shtenco/algotrading_graph_system](https://github.com/Shtenco/algotrading_graph_system) | Market graph | R&D_TARGET | Settlement/capacity-aware global market graph; `AlphaGraph != RebalancingGraph` | NONE |
| 22 | [Shtenco/ai_compress](https://github.com/Shtenco/ai_compress) | **Data Fabric** | **CANONICAL_DATA_FABRIC_TARGET** | EGD/SABF/HACE/TSC/AMCE/UMC, Graph-AI, GRAAL-IGC, Gabriel Horn SGH1, dedup, random access, corpus benchmarks, archive manifests | `archive_codec_profiles` |
| 23 | [Shtenco/synergy_pay_system](https://github.com/Shtenco/synergy_pay_system) | Payments | CANONICAL_DOMAIN | MetaPay: routing, compliance, funding, execution, settlement, reconciliation; Data Fabric archives evidence | `payment_execution_settlement` |
| 24 | [Shtenco/synergy_ai_blockchain](https://github.com/Shtenco/synergy_ai_blockchain) | Trust | CANONICAL_TARGET | PQ typed commitments/checkpoints/event-signing R&D; commits digests, not bulk archive blobs | `pq_chain_trust` |
| 25 | [Shtenco/synergychain](https://github.com/Shtenco/synergychain) | Business | APPLICATION_CONTROL_PLANE | Growth OS/CRM/SMM/Sales/AI-CFO; source bundles + memory artifacts migrate to Data Fabric | `business_growth_control_plane` |
| 26 | [Shtenco/synergychain.github.io](https://github.com/Shtenco/synergychain.github.io) | Presentation | PRESENTATION | Public static portal/build only | NONE |
| 27 | [Shtenco/cold_nuclear](https://github.com/Shtenco/cold_nuclear) | Science | SCIENTIFIC_R&D | Reproducible LENR/transmutation/materials computation; reproducibility packages → Data Fabric | NONE |
| 28 | [Shtenco/usds](https://github.com/Shtenco/usds) | Monetary R&D | MONETARY_R&D | Stable-money/reserve/mint-restore experiments with explicit external-value firewall | NONE |
| 29 | [Shtenco/synergy_financial_os](https://github.com/Shtenco/synergy_financial_os) | Financial truth | CANONICAL_TARGET | Double-entry, HardNAV, solvency, liquidity, recognition/capacity; closes/snapshots → Data Fabric | `canonical_accounting` |
| 30 | [Shtenco/synergy_eurasian](https://github.com/Shtenco/synergy_eurasian) | Economy | CANONICAL_DOMAIN_TARGET | Productive projects, industry, infrastructure, agriculture, regions | `productive_project_model` |
| 31 | [Shtenco/synergy_matrix_sota](https://github.com/Shtenco/synergy_matrix_sota) | Household | CANONICAL_DOMAIN_TARGET | Household savings/maturity/personal-capital model | `household_capital_model` |
| 32 | [Shtenco/agi_nexus](https://github.com/Shtenco/agi_nexus) | AI | CANONICAL_TARGET | Bounded reasoning/provenance/UNKNOWN/world-model core; checkpoints/evidence → Data Fabric | `reasoning_core` |
| 33 | [Shtenco/midas_ai](https://github.com/Shtenco/midas_ai) | Trading | CANONICAL_TARGET | Institutional alpha/quality/risk/portfolio/execution intelligence; canonical archive consumer | `trading_intelligence` |
| 34 | [Shtenco/synergy_system](https://github.com/Shtenco/synergy_system) | Governance | CANONICAL_ROOT | Constitution, federation/authority/evidence graph, Contracts, Secure Event Fabric, Data Fabric architecture | `architecture_governance` |
| 35 | [Shtenco/nexus_science_agent](https://github.com/Shtenco/nexus_science_agent) | Science AI | CANONICAL_TARGET | Search/evidence/falsification/reproduction pipeline with content-addressed research cache | `science_research_orchestration` |
| 36 | [Shtenco/synergynet](https://github.com/Shtenco/synergynet) | Network / Data plane | CANONICAL_TARGET | Chunk/hash/dedup/compression negotiation, P2P transport, cache/store-forward | `p2p_transport` |
| 37 | [Shtenco/synergy_meta_os](https://github.com/Shtenco/synergy_meta_os) | Orchestration | CANONICAL_TARGET | Node/runtime/capability/artifact/cache/storage lifecycle orchestration | `runtime_orchestration` |
| 38 | [Shtenco/blochain_budget](https://github.com/Shtenco/blochain_budget) | State / GovTech | CANONICAL_DOMAIN_TARGET | Budget/procurement traceability + official raw artifact/proof archive consumer | `state_budget_traceability` |
| 39 | [Shtenco/agi_autopilot](https://github.com/Shtenco/agi_autopilot) | Control | CANONICAL_TARGET | Bounded policy/capability/approval/action orchestration; current main minimal, candidate work in PR lineage | `action_orchestration` |
| 40 | [Shtenco/sinergy_app](https://github.com/Shtenco/sinergy_app) | Application | LEGACY_PLACEHOLDER | Legacy app-name lineage | NONE |
| 41 | [Shtenco/synergy_app](https://github.com/Shtenco/synergy_app) | Household app | CANONICAL_PRODUCT_TARGET | Store-ready personal finance app; encrypted portable backups/offline refs → Data Fabric | `household_capital_product` |
| 42 | [Shtenco/qr_compress](https://github.com/Shtenco/qr_compress) | **Offline Data Fabric** | **OFFLINE_DATA_FABRIC_TARGET** | QTC1/QTC2/QTD1 temporal dictionary + QF1 multi-frame QR, residual patching, model binding, offline evidence refs | NONE |
| 43 | [Shtenco/synergy_metachain](https://github.com/Shtenco/synergy_metachain) | Trust | CANONICAL_TARGET | PQ cross-chain/light-client/finality/bridge-proof verification; proof bundles → Data Fabric | `cross_chain_trust` |
| 44 | [Shtenco/motherboard_xpu_xml](https://github.com/Shtenco/motherboard_xpu_xml) | Compute | ACTIVE_R&D_TARGET | Compiled-graph XPU; future `Persistent State` target for content-addressed programs/models/files/snapshots | `compute_substrate_rnd` |
| 45 | [Shtenco/print_money_synergychain](https://github.com/Shtenco/print_money_synergychain) | Financial R&D | FALSIFICATION_R&D | HardNAV/external-profit/token-liquidity falsification engine | NONE |

## 46-й observed repo: master dossier, не runtime authority

| # | Репозиторий | Слой | Класс | Роль | Authority |
|---:|---|---|---|---|---|
| 46 | [Shtenco/synergy_project](https://github.com/Shtenco/synergy_project) | Portfolio / Governance presentation | MASTER_DOSSIER | Grant/investor/regulatory-sandbox dossier, repo registry, IP valuation, due-diligence package | NONE |

## Data Fabric — исправленная системная роль архиваторов

```text
DOMAIN AUTHORITATIVE BYTES
       │
       ├── SHA256(canonical bytes) = semantic digest
       ▼
ai_compress / Archive Profiles
       │
       ├── SGH1 / GRAAL / Graph-AI / UMC / other validated codec
       ├── content-defined chunks / dedup / random access
       └── SHA256(encoded archive) = archive digest
       ▼
SynergyNet distributed transport/cache
       ▼
Meta-OS lifecycle / placement / retention
       ├── cold archive
       ├── node cache
       ├── QTC2/QF1 offline side-channel
       ├── blockchain/metachain digest commitments
       └── future XPU Persistent State
```

Ключевой invariant:

> **Codec can change; semantic truth must not.**

`canonical_content_sha256` считается по каноническим исходным байтам, а `archive_sha256` — по конкретному сжатому контейнеру. Поэтому перекодирование архива не переписывает Financial OS, settlement, science evidence или blockchain semantic commitment.

## Сводка

- **45 / 45 technical federation repos** перечислены.
- **46 / 46 observed Shtenco repos** учтены вместе с master dossier.
- `ai_compress` повышен до canonical Data Fabric target.
- `qr_compress` повышен до Offline Data Fabric target, но **Authority = NONE**.
- Legacy/R&D repo теперь рассматриваются не как «хвост», а как provenance + migration sources с конкретными target domains.
- Main/default branch reality и candidate PR reality должны учитываться отдельно.
- Любая migration требует exact source commit, provenance, tests, evidence и explicit promotion decision.

## Экономический invariant

> `No external settlement ⇒ no external profit.`

Архивация, compression ratio, internal mark, mint/rebase, flash principal, backtest или model uplift сами по себе не создают external profit.
