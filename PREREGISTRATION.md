# EFMW-108 Preregistration

## Hypothesis status

The candidate boundary `tau0 = 108 minutes` is **not newly inferred from the confirmatory data**. It is treated as a prior observation motivating this prospective replication.

## Primary estimand

For horizon `tau`, define

`Delta(tau) = Loss(best prespecified baseline, tau) - Loss(EFMW, tau)`

using the primary proper scoring loss specified before outcome access. Positive Delta favors EFMW.

If the task is detection rather than probabilistic forecasting, the registered adapter must map outputs to the frozen primary metric before execution. It may not choose the metric after observing results.

## Primary hypothesis

There is a reproducible horizon-dependent change in `Delta(tau)` localized near the candidate boundary of 108 minutes.

## Null

There is no reproducible EFMW-specific boundary near 108 minutes after comparison with prespecified controls, uncertainty estimation, multiplicity handling, and leakage/ablation checks.

## Horizons

`[30, 60, 90, 100, 105, 108, 111, 120, 150, 180]` minutes.

No horizon may be added, removed, or relabeled in the confirmatory analysis.

## Conditions

`CONCEALED`, `REVEALED`, `ADVERSARIAL`.

If a dataset/system cannot support causal disclosure of predictions, only CONCEALED is confirmatory for that dataset; unsupported conditions must be marked `NOT_APPLICABLE`, not simulated post hoc.

## Required comparisons

- EFMW candidate
- persistence/naive baseline
- registered conventional statistical/control baseline
- registered strong task-specific baseline
- EFMW recurrence/recursive component ablation

## Data separation

All transformations at time `t` may use information available at or before `t` only. Targets at `t + tau` and later are inaccessible to fitting, threshold selection, feature construction, and model selection.

## Freeze rule

Before confirmatory outcome access:

- commit source;
- record commit SHA;
- generate `FREEZE_MANIFEST.sha256`;
- record dataset identifiers/version hashes;
- freeze model parameters;
- freeze random seeds;
- freeze exclusions;
- freeze primary metric and multiplicity procedure.

Any later change creates a new protocol version and must not be represented as the original frozen test.

## Replication rule

The 108-minute boundary is not considered robust from this protocol unless it reproduces in an independent run/dataset under the same frozen decision rule. This repository intentionally does not define such a result as a new law of physics.
