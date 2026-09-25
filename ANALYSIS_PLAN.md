# Analysis Plan

## Unit of analysis

The adapter defines independent evaluation units (episodes, streams, subjects, machines, or trials). Splitting must occur at the highest level necessary to prevent temporal/entity leakage.

## Primary scoring

Default harness metric: binary log loss for probabilistic outcomes.

For a registered continuous target, replace the adapter before freezing with a proper prespecified loss. Do not select among metrics based on observed EFMW performance.

## Boundary analysis

For each condition and horizon:

1. compute loss per independent unit;
2. compute paired `Delta = baseline_loss - efmw_loss`;
3. report mean and median Delta;
4. bootstrap independent units for a 95% interval;
5. retain the entire horizon curve.

The primary boundary analysis fits two models to the paired Delta curve:

- `M0`: smooth/no designated change point;
- `M1`: segmented model with the change point fixed at 108 minutes.

Report the prespecified comparative fit statistic. Do **not** search all possible change points in the confirmatory test. An unconstrained change-point search may be reported only as exploratory.

## Local contrast

Report the frozen local contrast:

`C108 = Delta(105) - 2*Delta(108) + Delta(111)`

as a descriptive measure of local curvature. It is not, by itself, proof of a boundary.

Also report slopes on the prespecified neighborhoods 90–105 and 111–150 minutes.

## Multiple comparisons

All horizon-by-condition secondary hypothesis tests use Holm correction within the confirmatory family. Raw and adjusted values must both be retained.

## Missingness

No silent imputation. The adapter must expose missing targets and reasons. Exclusion counts are reported by horizon and condition.

## Effect reporting

Always report effect sizes and uncertainty, not only p-values.

## Exploratory work

Anything not frozen here is labeled `EXPLORATORY`, saved separately, and cannot alter the confirmatory outcome.
