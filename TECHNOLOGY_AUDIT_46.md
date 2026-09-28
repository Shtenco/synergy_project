# СИНЕРГИЯ — Technology Audit 46/46
> [!IMPORTANT]
> **ИСТОРИЧЕСКИЙ СНИМОК.** Этот документ фиксирует более раннее состояние Федерации 45/46 на 6 сентября 2026 года и сохраняется для provenance.
> Текущий канонический реестр содержит **75 репозиториев**:
> [SYNERGY Repository Atlas](https://github.com/Shtenco/synergy_system/blob/main/docs/SYNERGY_REPOSITORY_ATLAS.md) ·
> [Registry JSON](https://github.com/Shtenco/synergy_system/blob/main/registry/SYNERGY_REPOSITORIES.json) ·
> [Federation V2](https://github.com/Shtenco/synergy_system/blob/main/config/repository_federation_v2.yaml).


> **Дата:** 6 сентября 2026  
> **Scope:** default-branch/root/README technology inventory + known active Federation V3 candidate work.  
> **Observed repos:** 46 = 45 technical Federation repositories + `synergy_project` master dossier.  
> **Важно:** это портфельный architectural audit, не exhaustive source/security/legal audit каждой строки кода.

## Главный вывод аудита

Предыдущая карта правильно отделяла authorities, но **слишком грубо описывала ряд R&D/legacy репозиториев и недооценивала слой архивации/сжатия**. После просмотра всех текущих repo root/default branches архиваторы становятся самостоятельным cross-cutting слоем:

# `SYNERGY Data Fabric`

```text
Authoritative Domain Object
        ↓ canonical serialization
canonical_content_sha256
        ↓
ai_compress
  codec registry / compression / dedup / random access
        ↓
archive_sha256 + ArchiveManifest
        ↓
SynergyNet
  chunk / cache / store-forward / replication
        ↓
Meta-OS
  placement / lifecycle / retention / rollback
        ├── Cold Archive
        ├── QTC2/QF1 Offline Path
        ├── Blockchain/MetaChain digest commitments
        └── future XPU Persistent State
```

The archive stores and transports evidence; **it does not own the meaning of the evidence**.

---

# 1. Repository-by-repository audit

## 1 — `shtenco.github.io`
**Observed:** single public `index.html` presentation site.  
**Value:** public provenance/portfolio surface.  
**Migration/integration:** presentation only; may consume signed project-status feeds later.  
**Authority:** NONE.

## 2 — `quantum-trading_metatrader5`
**Observed technology:** Qiskit/IBM-Q + MetaTrader 5 experiment for market prediction.  
**Value:** quantum-feature/optimizer research lineage.  
**Migration:** only reproducible components → `midas_ai/models/quantum` or optimization R&D after matched classical baseline.  
**Do not promote:** old quantum/trading claims without new OOS evidence.

## 3 — `computer_vision_trading_metatrader_5`
**Observed technology:** OHLC/indicators/oscillators encoded as RGB market images; CNN/local/trend/volatility paths; attention maps; BiLSTM; direction + magnitude prediction.  
**Migration:** `midas_ai/features/vision` + operator explainability/attention visualization.  
**Archive integration:** image tensors, checkpoints, attention maps, split manifests → Data Fabric.

## 4 — `swap_arbitrage_metatrader_5`
**Observed technology:** portfolio optimization with swap/carry, covariance, Sharpe objective, MT5 swap data, multi-pair backtests.  
**Migration:** `midas_ai/strategies/carry`; current swap schedule adapters can also inform global market graph costs.  
**Boundary:** historical annual-return/Sharpe claims are lineage, not current canonical evidence.

## 5 — `cross_forex_arbitrage_trading_metatrader_5`
**Observed technology:** synthetic FX cross-rates, multi-path pricing, direct-vs-synthetic discrepancy detection.  
**Migration:** `algotrading_graph_system` route/edge construction + MIDAS arbitrage candidate generation.  
**Boundary:** arithmetic discrepancy ≠ executable arbitrage.

## 6 — `global_liquidity_dataminer`
**Observed technology:** Fed/ECB/BOJ/PBoC balance-sheet mining, composite liquidity index, ML FX forecasting.  
**Migration:** not only MIDAS — also `synergy_eurasian` macro stress/scenario inputs and Federation systemic-risk scenarios.  
**Data Fabric:** source snapshots, normalization lineage and model datasets should be immutable/provenanced.

## 7 — `3D_bars_market_structure`
**Observed technology:** time × price × volume voxel representation, volume profiles, 3D visualization and reversal-cluster research.  
**Migration:** `midas_ai/features/3d_market` + operator visualization.  
**Boundary:** historical 97%/early-reversal wording needs current frozen benchmark before promotion.

## 8 — `multi_threaded_trading_robot_with_machine_learning_python`
**Observed technology:** XGBoost, GMM regime clustering, RFECV, bagging, multi-symbol threads, portfolio risk, queue logging, MT5 execution.  
**Migration:** MIDAS worker/runtime patterns, regime baselines and multi-symbol risk tests.  
**Boundary:** execution code does not become canonical risk authority by inheritance.

## 9 — `midas_ai_trading_system`
**Observed technology:** institutional multi-agent architecture Levels 0–10, independent risk veto, forward-first validation, strategy modules, execution separation. Critically includes **Level 8 Unified Data Archive** for raw data/features/signals/decisions/trades/latent states.  
**Migration:** strongest evidence-backed components → canonical `midas_ai`; Unified Data Archive semantics → shared Data Fabric.  
**Why important:** this repo is a major technology source, not just historical code.

## 10 — `midas_lite`
**Observed:** minimal README/default root.  
**Role:** legacy compact MIDAS lineage.  
**Migration:** only after artifact inventory and reproducible differentiation.

## 11 — `turbo_linux`
**Observed technology:** active clean-room `turbo_core`, capability primitive, bounded IPC, O(1) priority scheduler, freestanding checks/benchmarks; legacy VPS/KVM experiment remains.  
**Migration:** host substrate for Meta-OS/XPU/SynergyNet.  
**Security:** legacy committed `.ppk` history must be treated as compromised/rotated; old remote-key workflow is not a production pattern.

## 12 — `agi_olga`
**Observed technology:** SmallWorld AGI V11.3, deterministic graph workspace, ARC grid algebra, symbolic DSL, MDL program synthesis, episodic world model; NEXUS-600K / InfoGraph lineage.  
**Migration:** benchmark- and digest-gated components → `agi_nexus`.  
**Data Fabric:** checkpoints, frozen splits and benchmark artifacts.

## 13 — `ai_coder`
**Observed default branch:** currently minimal README.  
**Federation target:** evidence-backed change orchestration.  
**Migration:** build canonical implementation only from tested candidate work; do not claim main already contains it.

## 14 — `ai_trade_terminal`
**Observed technology:** Cassandra process supervisor, DataCollector, TradeTester, DataHub, cache, WebSocket stream, watchdog/reconnect, logs, dashboard, AI supervisor/executor UI.  
**Migration:** MIDAS operator terminal; Meta-OS supervision patterns; SynergyNet streaming/cache patterns.  
**Data Fabric:** event/log/history retention.

## 15 — `shtencoauantai.github.io`
**Observed:** public quant/AI presentation site.  
**Role:** provenance/showcase only.  
**Authority:** NONE.

## 16 — `cashero`
**Observed technology:** cyclic liquidity simulation, Polygon multi-RPC live bot, LP reinvestment, tokenomics simulations, contracts/deployment lineage.  
**Migration:** economic/falsification ideas only → `ai_financial_system` / `print_money_synergychain`; any execution/security pieces require clean-room review.  
**Security:** historical key/env handling means no direct promotion to production.

## 17 — `ai_language`
**Observed technology:** published repository-aware coding agent, semantic task/repository/change/impact graphs, stable `REQ-*` traceability, experimental `.ailang` compiler.  
**Migration:** core Federation semantic requirements/compiler and AI-Coder input layer.  
**Data Fabric:** requirements/change/evidence trace packages may be archived as release evidence.

## 18 — `sinergy-super-app`
**Observed root:** native `mobile/` project + CI; no root README in main.  
**Role:** non-authoritative federation client lineage.  
**Migration:** consume Personal Capital, MetaPay receipts, NEXUS and offline Data Fabric; never own ledger/payment truth.

## 19 — `binary_quantum_theory`
**Observed technology:** large candidate mathematical/computational theory with explicit EXACT/FINITE/OPEN/FAIL status vocabulary and preserved held-out failures.  
**Migration:** Science Agent orchestration + Data Fabric reproducibility packages.  
**Boundary:** experimental confirmation explicitly not claimed.

## 20 — `ai_financial_system`
**Observed technology:** Flash Loan Arbitrage, AI Central Bank, AI Market Maker, Value Flow Treasury, QE/Bridge QE, Economic State Oracle, DeFi Contour Registry, Monte Carlo, anti-MEV/orderflow auction, bridge-solvency research.  
**Migration:** split by responsibility:
- execution/orderflow/route adapters → MetaPay/MIDAS R&D;
- economic truth tests → Financial OS falsification inputs;
- trust commitments → blockchain research;
- internal-value experiments → `print_money_synergychain`.
**Authority:** NONE.

## 21 — `algotrading_graph_system`
**Observed technology:** explicit settlement/capacity-aware graph; node=(institution, venue, account/channel, asset, settlement date); edge includes rate, fee, capacity, depth, slippage, latency and evidence.  
**Invariant:** `AlphaGraph != RebalancingGraph`.  
**Migration/integration:** shared market/network normalization for MIDAS alpha and MetaPay routing, with independent objectives.

## 22 — `ai_compress`
**Observed technology:** far larger than prior map described.

Technology inventory includes:
- EGD-256;
- SABF-X;
- HACE-X;
- TSC-X;
- AMCE-100X;
- UMC-256 + MDL routing;
- Graph-AI Compression V5.2;
- GRAAL-IGC;
- Gabriel Horn `SGH1` with multiscale lifting, significance shells, deduplication, random access and surface-aware MDL;
- Arithmetic coding;
- rANS;
- Huffman;
- Graph Delta;
- Tier-1 benchmark infrastructure;
- exact byte equality/SHA-256 validation;
- throughput, memory and random-access measurement.

**Correct new role:** `CANONICAL_DATA_FABRIC_TARGET` / archive codec profile owner.  
**Consumers:** SynergyNet, Meta-OS, MIDAS, NEXUS, Science, Financial OS, MetaPay, Budget, Blockchain/MetaChain, Business OS, Personal Capital and future XPU Persistent State.  
**Authority boundary:** compression/archive profile authority only; semantic authority remains with producer domain.

## 23 — `synergy_pay_system`
**Observed technology:** substantial MetaPay integration core: fiat/crypto/CBDC boundaries, omnichain catalog, CEX/DEX/bridge routes, compliance/readiness, provider registry, signed REST, public reference rates, CCXT boundary, double-entry internal payment ledger, settlement state machine, reconciliation, signed manifests, AML boundaries, FastAPI/CLI.  
**Data Fabric:** archive settlement/reconciliation/readiness evidence; QR/QTC can transport references, never settle by itself.

## 24 — `synergy_ai_blockchain`
**Observed main:** README-only; richer PQ/commitment candidate PR lineage exists.  
**Correct integration:** blockchain stores/anchors compact content/manifest digests; bulk evidence belongs to Data Fabric.  
**Authority:** trust commitment only, never accounting.

## 25 — `synergychain`
**Observed technology:** Growth OS V7, portal, OLGA AGI chat, multi-agent modes, recursive compressed conversation memory, business autopilot, SMM/CRM/Sales/CFO, encrypted API vault, backend/static build. Full reproducible source distributed as `.tar.gz`.  
**Data Fabric migration:** replace ad-hoc large source/memory bundles over time with content-addressed archive manifests and approved codec profiles.

## 26 — `synergychain.github.io`
**Observed technology:** static GitHub Pages distribution with service-worker expansion of verified bundle.  
**Integration:** presentation consumer of signed/content-addressed release artifacts.

## 27 — `cold_nuclear`
**Observed technology:** reproducible computational programme, molten vs solid hypotheses, Pd–RE selection, isotope/decay networks, causal graph consistency, Pareto selection, explicit measured/derived/stress/hypothesis/legacy statuses.  
**Data Fabric:** full reproducibility package—code, seeds, raw/generated datasets, run logs, evaluated-data references.  
**Boundary:** not proof of LENR/transmutation.

## 28 — `usds`
**Observed technology:** Base fork economic model, mint→sell→restore cycle, explicit decomposition of external productive value from internal mint mechanics; deployment hardening.  
**Important positive finding:** README itself correctly states mint/sale do not create dollar profit and synthetic `3x` value added is a hypothesis.  
**Migration:** monetary/falsification R&D only.

## 29 — `synergy_financial_os`
**Observed main:** README-only; rich candidate protocol/contract lineage exists.  
**Target:** accounting truth/HardNAV/solvency/liquidity/revenue/distribution capacity.  
**Data Fabric:** AccountingClose/FinancialSnapshot/Merkle/replay/restatement packages. Canonical hash must be independent of archive codec.

## 30 — `synergy_eurasian`
**Observed main:** README-only; candidate domain expansion exists.  
**Target:** productive projects, industry, regions, infrastructure, agriculture and system dynamics.  
**Data Fabric:** project evidence/datasets/reports; does not own archive codec selection.

## 31 — `synergy_matrix_sota`
**Observed main:** README-only; candidate household-capital model work exists.  
**Target:** household savings/maturity/capital model.  
**Integration:** feeds `synergy_app` + Financial OS; simulation datasets/evidence may use Data Fabric.

## 32 — `agi_nexus`
**Observed technology:** canonical bounded reasoning target with explicit migration from OLGA, frozen artifact identity, graph/small-world reasoning, logic/cybernetics, benchmarks, inference artifacts and authority restrictions.  
**Data Fabric:** model/checkpoint/split/benchmark/provenance archive.

## 33 — `midas_ai`
**Observed technology:** canonical MIDAS target, clear migration source family, causal alignment, graph/macro/microstructure/3D/vision features, models/strategies/portfolio/risk/validation/execution/reconciliation/evidence.  
**Data Fabric:** canonical consumer for raw data, model artifacts, validation reports and immutable decision/execution evidence.

## 34 — `synergy_system`
**Observed technology:** architecture/governance root, authority constitution, economic truth rules, federation, system-of-systems map; Contracts/Secure Event Fabric candidate stack.  
**New V3.1 role:** owns Data Fabric protocol/schema/authority map, not compression implementation.

## 35 — `nexus_science_agent`
**Observed technology:** search/retrieval/index/evidence graph/falsification/reproduction pipeline; explicitly requires **Content-Addressed Cache** and reproducibility package.  
**Data Fabric:** natural storage/archive backend for source/dataset/computation/reproduction objects.

## 36 — `synergynet`
**Observed technology:** architecture already contains content-defined chunking → content hash → local/network dedup/cache → compression profile → PQ session → multipath/store-forward → reconstruction/integrity.  
**Correct new role:** transport/data plane for Data Fabric objects, not archive semantic owner.  
**Codec selector:** optimize bytes + CPU + latency + memory + cache amplification, not ratio alone.

## 37 — `synergy_meta_os`
**Observed technology:** node runtime orchestration, signed manifest, capabilities, lifecycle, compression/content cache, storage, updates/rollback, health/audit.  
**Correct Data Fabric role:** storage-tier placement, cache lifecycle, retention and service orchestration; no semantic authority.

## 38 — `blochain_budget`
**Observed technology:** public budget/treasury/EIS append-only provenance ledger, versioned KBK registry, strict entity linking, Merkle proofs, trace graph and EVM anchor.  
**Critical archive finding:** README explicitly says large physical backfill should run on a **networked archive/data node**.  
**Data Fabric:** raw official artifacts, normalized corpora, registry snapshots, trace/proof bundles.

## 39 — `agi_autopilot`
**Observed main:** README-only; candidate bounded action/control work exists in PR lineage.  
**Target:** policy/capability/approval/domain-action orchestration.  
**Data Fabric:** audit/action decision packages may be retained; archive cannot grant action authority.

## 40 — `sinergy_app`
**Observed root:** minimal legacy placeholder.  
**Role:** preserve provenance, do not duplicate canonical `synergy_app`.

## 41 — `synergy_app`
**Observed technology:** actual store-release repository with Android/iOS/www, CI/CD for APK/AAB/IPA/store delivery and signing-secret separation.  
**Migration/integration:** canonical Personal Capital product; Data Fabric provides encrypted user-controlled backup/export and offline evidence references.

## 42 — `qr_compress`
**Observed technology:** QTC1 + QTC2 Temporal Dictionary Engine, QTD1 shared temporal model, exact/patch/standalone, residual patching, MDL multi-codec router, model/content hashes, CRC32 frames, QF1 multi-frame out-of-order reconstruction, benchmark/proof corpus.  
**Correct new role:** `OFFLINE_DATA_FABRIC_TARGET`.  
**Consumers:** MetaPay, Personal Capital/super-app, Budget, Science, Meta-OS, SynergyNet, MetaChain proof references.  
**Authority:** NONE. QR/QTC decode or presence never equals authorization/settlement/trust.

## 43 — `synergy_metachain`
**Observed main:** README-only; candidate cross-chain/light-client/finality proof work exists.  
**Data Fabric:** proof/checkpoint packages off-chain; chain/meta layer binds/verifies digests and assumptions.

## 44 — `motherboard_xpu_xml`
**Observed technology:** persistent programmable dataflow XPU; explicitly defines **Persistent State** as content-addressed programs, models, files and snapshots.  
**Critical new integration:** future hardware acceleration/storage tier for Data Fabric.  
**Boundary:** analytical model/ISA/package designs ≠ fabricated silicon performance.

## 45 — `print_money_synergychain`
**Observed main:** README-only; candidate falsification work exists.  
**Role:** explicit HardNAV/external-value monetary falsification R&D.  
**Authority:** NONE.

## 46 — `synergy_project`
**Observed technology:** master regulatory-sandbox/grant/investor dossier, 45-repo registry, IP valuation and due-diligence package.  
**Role:** portfolio/documentation layer created after the 45-repo technical Federation inventory.  
**Authority:** NONE.  
**Counting rule:** never inflate technical federation membership by counting the dossier as a runtime domain.

---

# 2. Cross-repository migration map

## Trading lineage → canonical MIDAS / graph

```text
quantum-trading ────────────────┐
computer-vision ────────────────┤
3D-bars ────────────────────────┤
global-liquidity ───────────────┤
swap/carry ─────────────────────┤
multithreaded-ML ───────────────┤
midas_ai_trading_system ────────┼──→ midas_ai
midas_lite ─────────────────────┤
ai_trade_terminal ──────────────┘

cross-forex-arbitrage ─────────────→ algotrading_graph_system → MIDAS / MetaPay
```

## AI lineage → canonical intelligence

```text
agi_olga / SmallWorld / NEXUS-600K → agi_nexus
agi_nexus → nexus_science_agent
agi_nexus → agi_autopilot
ai_language → ai_coder / federation semantic tooling
```

## Financial R&D → bounded domain owners

```text
ai_financial_system / usds / cashero / print_money
         ├──→ MIDAS research
         ├──→ MetaPay research
         ├──→ Financial OS falsification/accounting tests
         └──→ Blockchain trust research
```

No R&D monetary mechanism can bypass external settlement/HardNAV rules.

## Data / archive migration — newly promoted

```text
midas Unified Data Archive ──────┐
Science content-addressed cache ─┤
Budget archive/data node ────────┤
Financial close packages ────────┤
MetaPay settlement packages ─────┤
NEXUS checkpoints ───────────────┤
Business source bundles ─────────┤
Personal Capital backups ────────┼──→ Data Fabric
                                 │
ai_compress codec/archive core ──┤
qr_compress offline/QTC path ─────┤
SynergyNet transport/cache ──────┤
Meta-OS lifecycle ────────────────┤
Blockchain/MetaChain commitments ┤
XPU Persistent State (future) ────┘
```

---

# 3. Data Fabric authority matrix

| Responsibility | Owner |
|---|---|
| Domain semantic truth | original domain repo |
| Archive/codec profile registry | `ai_compress` |
| Offline temporal/QR encoding R&D | `qr_compress` |
| Network object/chunk transport | `synergynet` |
| Storage/cache/service lifecycle | `synergy_meta_os` |
| Architecture/schema/authority rules | `synergy_system` |
| Economic/accounting truth | `synergy_financial_os` |
| Settlement truth | `synergy_pay_system` |
| On-chain commitment | `synergy_ai_blockchain` |
| Cross-chain verification | `synergy_metachain` |
| Future persistent-state compute | `motherboard_xpu_xml` R&D |

---

# 4. Non-negotiable archive invariants

```text
canonical_content_sha256 = SHA256(canonical original bytes)
archive_sha256           = SHA256(exact encoded archive bytes)
```

Therefore:

- codec migration does not change semantic truth;
- archive corruption is independently detectable;
- blockchain does not need to store bulk data;
- dedup/cache does not redefine ownership;
- QTC shared-model lookup cannot silently change the referenced content;
- all lossless profiles must prove exact round-trip;
- raw secrets are forbidden in unencrypted archive manifests/packages;
- external KMS/HSM/user key references are used for encrypted high-value data.

---

# 5. Priority actions produced by this audit

1. Complete Federation V3.1 Data Fabric schemas/runtime/tests in `synergy_system`.
2. Promote `ai_compress` from generic ENGINEERING_CORE to canonical archive/codec target.
3. Promote `qr_compress` from generic R&D target to explicit offline Data Fabric target with Authority=NONE.
4. Bind MIDAS Unified Data Archive to shared Data Fabric manifests.
5. Bind Science Agent content-addressed cache and reproducibility packages.
6. Bind Budget large official data backfill to archive/data node profile.
7. Bind Financial OS/MetaPay artifacts to dual-hash archive manifests.
8. Let blockchain/metachain commit canonical/manifest hashes, not encoded blobs.
9. Add XPU Persistent State as future storage/compute tier, never as current hardware claim.
10. Maintain the distinction `45 technical federation + 1 dossier = 46 observed repos` in every investor/grant document.
