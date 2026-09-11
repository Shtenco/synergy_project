# SYNERGY LEGACY DISTILLATION V1 — master summary

Date: 2026-09-11.

The eight audited legacy archives were converted into a controlled migration program rather than bulk-copied into canonical repositories.

## Distillation classes

- `GREEN`: source snapshot is safe enough for R&D reuse after provenance capture.
- `YELLOW_REVIEW`: useful concept or code lineage, but must be rewritten/revalidated before canonical use.
- `RED_QUARANTINE`: embedded secrets, live-signing/deployment risk, contradicted production claims or unsafe economic/accounting behavior.
- `ARCHIVE`: supporting artifacts, images and historical evidence.

Local full-corpus inventory produced during the audit contained 1206 records: 7 GREEN, 646 YELLOW-review, 147 RED-quarantine and 406 archive/support records.

## Canonical migrations completed in V1

- `synergy_system`: federation/provenance rules for legacy promotion.
- `synergy_financial_os`: HardNAV, flash-principal, capital-vs-profit and deposit-liability regression gates.
- `synergy_graph_print_money`: conservation, self-LP, QE and zero-denominator regression gates.
- `synergy_pay_system`: deterministic off-chain Debt Netting V2 + solvency/net-position tests.
- `synergynet`: adaptive VerificationNetwork V2 with cumulative slow-drift detection.
- `ai_financial_system`: AICB scenario-only authority boundary + content-addressed scenario evidence object/tests.
- `synergy_eurasian`: typed AICB scenario schema so simulated paths cannot silently become observed facts.
- `usds`: stablecoin transient-depeg/left-tail stress gate.
- `synergy_meta_os`: sanitized keeper/GasGuard migration rules with no embedded signing authority.

## Permanent economic rules distilled from legacy failures

```text
own-token mark            != external profit
internal AMM mark         != external profit
self-LP movement          != consolidated income
flash principal           != owned NAV
new capital               != revenue
synthetic yield           requires an external source + settlement evidence
QE                        requires a balanced counter-entry
participant deposits      remain liabilities
zero/near-zero denominator must not create astronomical ROI
simulation                != observed economic fact
```

The archive remains immutable provenance. Canonical repositories receive only validated/re-written components and falsification tests.
