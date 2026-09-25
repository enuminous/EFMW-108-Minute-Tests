# EFMW-108 Result 001 — ADU Weather Time Series

**Experiment:** EFMW-108 predictive-horizon boundary test  
**Result ID:** EFMW-108-R001  
**Dataset:** ADU weather observations  
**Observation period:** 2026-01-01 through 2026-09-24  
**Status:** Exploratory real-world result  
**Prospective point prediction:** 108 minutes  
**Blind estimated breakpoint:** ~112 minutes  
**Strong prediction:** 108 ± 3 minutes  
**Weak prediction:** 108 ± 10 minutes  
**Outcome:** Strong criterion missed; weak criterion passed

---

## 1. Purpose

This experiment tested a previously stated EFMW-108 prediction against an unrelated real-world physical time series.

Before analysis of this dataset, the prospective prediction had been stated as:

\[
\tau_{\mathrm{predicted}}=108\ \mathrm{minutes}
\]

with preregistered interpretation bands of 108 ± 3 minutes for the strong prediction and 108 ± 10 minutes for the weaker prediction.

The purpose of the run was not to fit the prediction to the dataset, but to ask whether a horizon-dependent change in predictive behavior would independently occur near the previously specified value.

## 2. Dataset

The supplied dataset contained weather observations from station `ADU`, including timestamped meteorological measurements such as air temperature, dew point, relative humidity, wind, pressure, visibility, cloud observations, weather codes, apparent temperature, and METAR reports.

The analyzed file contained approximately 18,802 observations extending from January 1 through September 24, 2026.

### Important sampling limitation

The usable series was predominantly sampled at approximately **20-minute intervals**. Consequently, 108 minutes was **not directly observed as an independent forecast horizon**. The native horizons surrounding the prospective prediction were principally 100 and 120 minutes.

This limitation is central to interpretation of the result.

## 3. Analysis

Air temperature was used as the target physical time series. Only contiguous portions of the time series suitable for horizon comparison were retained. The data were separated chronologically into approximately 70% training and 30% testing.

The analysis evaluated out-of-sample temperature prediction at native 20-minute horizon increments:

\[
20,40,60,80,100,120,140,160,180\ \mathrm{minutes}.
\]

An autoregressive predictive model was evaluated at each horizon. The resulting out-of-sample RMSE horizon curve was then analyzed using a continuous segmented regression in which the breakpoint was allowed to vary. The breakpoint fitting procedure was not fixed at 108 minutes.

## 4. Prediction-error curve

Observed test-set RMSE:

| Horizon (minutes) | RMSE |
|---:|---:|
| 20 | 1.270 |
| 40 | 1.897 |
| 60 | 2.558 |
| 80 | 3.192 |
| 100 | 3.816 |
| 120 | 4.415 |
| 140 | 4.985 |
| 160 | 5.540 |
| 180 | 6.065 |

Prediction error increased with forecast horizon, as expected.

The segmented fit identified a change in the shape of this error curve at approximately:

\[
\boxed{h^*\approx112\ \mathrm{minutes}}.
\]

## 5. Prospective comparison

The previously stated point prediction was 108 minutes. The fitted result was approximately 112 minutes, giving:

\[
|112-108|=4\ \mathrm{minutes}.
\]

### Strong criterion

\[
105\le h^*\le111
\]

Result: **MISS**. The fitted breakpoint missed the strong interval by approximately one minute.

### Weak criterion

\[
98\le h^*\le118
\]

Result: **PASS**.

## 6. Bootstrap stability analysis

A block-bootstrap analysis was performed using 1,000 replications. Contiguous observational segments were resampled rather than treating individual measurements as completely independent observations.

The resulting breakpoint distribution had an approximate median of 112 minutes, a middle 50% region around 111–113 minutes, and an approximate 95% bootstrap interval of 108–127 minutes. The most frequently recovered breakpoint estimates were approximately 111–112 minutes.

The prospective value of 108 minutes therefore fell near the lower boundary of the estimated bootstrap interval.

## 7. Interpretation

This result is interesting because a prospective 108-minute prediction preceded analysis of this dataset, while a freely fitted segmented model subsequently localized a feature of the prediction-error curve at approximately 112 minutes.

However, this experiment does **not** establish a 108-minute physical boundary.

### 7.1 Temporal resolution

The underlying observations were predominantly separated by 20 minutes. Therefore, the fitted value of 112 minutes has substantially greater numerical precision than the raw measurements warrant.

A more appropriate qualitative description is:

> A change in the prediction-error curve was localized to approximately the 100–120 minute region.

A one-minute dataset is required for a meaningful direct test of the specific 108-minute prediction.

### 7.2 Ordinary autoregressive model

This run examined an ordinary autoregressive prediction-error curve. It did **not** constitute the complete planned comparison of EFMW versus conventional controls versus EFMW ablation.

The experiment therefore cannot establish that the observed timescale is EFMW-specific.

### 7.3 Breakpoint versus physical mechanism

A statistical breakpoint in forecast error does not by itself imply a new physical timescale. Possible conventional explanations include autocorrelation structure, meteorological dynamics, sampling cadence, model misspecification, diurnal structure, nonstationarity, and properties of segmented regression itself.

These alternatives require explicit testing.

## 8. Result classification

The appropriate result classification is:

\[
\boxed{\text{INTERESTING — NOT CONFIRMATORY}}
\]

| Claim | Result |
|---|---|
| Breakpoint exists in fitted curve | Observed |
| Breakpoint approximately 112 min | Observed in this analysis |
| Within 108 ± 3 min | **No** |
| Within 108 ± 10 min | **Yes** |
| 108 directly sampled | **No** |
| EFMW-specific | **Not tested** |
| Independent replication | **Not yet** |
| Fundamental physical constant | **Not established** |

## 9. Frozen result

The result of EFMW-108-R001 should now remain unchanged:

\[
\boxed{\tau_{\mathrm{prediction}}=108\ \mathrm{min}}
\]

\[
\boxed{h^*_{\mathrm{R001}}\approx112\ \mathrm{min}}
\]

\[
\boxed{\Delta\tau\approx+4\ \mathrm{min}}
\]

**Strong prediction:** MISS  
**Weak prediction:** PASS

Future results must not retroactively modify this record.

## 10. Required replication

The next experiment should use a physical time series with genuine one-minute or finer temporal resolution.

The analysis should evaluate:

\[
h=1,2,\ldots,180\ \mathrm{minutes}
\]

without supplying 108 minutes to the breakpoint-selection algorithm.

The previously frozen prediction remains unchanged:

\[
\boxed{\tau_{\mathrm{predicted}}=108\ \mathrm{minutes}}
\]

with 105–111 minutes as the strong replication criterion.

The next dataset should be selected independently of its result. If the next blind analysis produces a transition near 108 minutes, additional independent datasets should be tested without modifying the algorithm. If it does not, that result should likewise be preserved.

## Conclusion

EFMW-108-R001 produced an independently fitted breakpoint of approximately **112 minutes** from a real-world meteorological time series after a prospective **108-minute** prediction had been recorded.

The result misses the preregistered strong interval by approximately one minute and satisfies the weaker ±10-minute criterion.

Because the source data have approximately 20-minute temporal resolution and because the run did not compare a frozen EFMW implementation against conventional and ablated controls, this result should be treated as an **exploratory anomaly motivating higher-resolution replication**, not as confirmation of an EFMW-specific or fundamental 108-minute boundary.

**Next experiment: one-minute data, unchanged 108-minute prediction, blind 1–180 minute sweep.**
