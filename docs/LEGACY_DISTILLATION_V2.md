# LEGACY DISTILLATION V2 — MASTER DOSSIER ENTRY

On 2026-09-11 the legacy archive corpus was re-audited at code-unit level.

Pipeline: 1206 legacy file instances -> 646 YELLOW instances -> 332 unique YELLOW SHA objects -> 5,653 Python/Solidity units -> 2,651 normalized structural variants -> 221 semantic mechanisms -> 19 canonical authority repositories -> 53 required test profiles -> promotion gates.

Validation: 646/646 source paths present; SHA mismatches 0; Python AST parse 69/69; Solidity structural parse 157/157; unmapped code units 0; package tests 8/8; embedded raw private-key assignment pattern hits 0.

Promotion status is intentionally conservative: 77 REWRITE_REQUIRED, 129 CANDIDATE_AFTER_TEST, 9 SUPPORT_CANDIDATE and 6 utility/plumbing support clusters requiring manual review. No mechanism is marked production-ready and no gate is marked passed.

The master architectural source for V2 is `Shtenco/synergy_system/docs/LEGACY_DISTILLATION_V2.md`; owner-specific manifests live in each canonical authority repository.