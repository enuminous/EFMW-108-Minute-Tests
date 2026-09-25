# Failure / Falsification Criteria

EFMW-108 does **not** support the candidate 108-minute boundary if one or more of the following materially accounts for the result:

1. The apparent effect requires future/oracle information.
2. The effect disappears under strict held-out temporal evaluation.
3. A prespecified conventional baseline matches or exceeds the EFMW candidate without greater information access.
4. The effect is explained by a documented implementation bug, timestamp alignment error, target leakage, or preprocessing artifact.
5. The candidate transition does not reproduce on the independent confirmatory dataset/run.
6. The location of an unconstrained transition is unstable across reasonable independent replications.
7. The claimed EFMW-specific advantage survives only through post-hoc parameter, metric, horizon, seed, or exclusion selection.
8. Removing the purported EFMW-specific recursive mechanism does not materially change the result where the mechanism is claimed to be causal.

A null result is a valid experimental result and must remain in the record.
