"""Frozen model interface. Replace placeholders BEFORE creating the confirmatory freeze."""
from abc import ABC, abstractmethod
import numpy as np

class ForecastModel(ABC):
    name = "abstract"
    @abstractmethod
    def fit(self, X, y): ...
    @abstractmethod
    def predict_proba(self, X): ...

class NaiveRateBaseline(ForecastModel):
    name = "naive_rate"
    def fit(self, X, y):
        self.p = float(np.clip(np.mean(y), 1e-6, 1-1e-6))
        return self
    def predict_proba(self, X):
        return np.full(len(X), self.p)

class EFMWCandidate(ForecastModel):
    name = "efmw_candidate_UNIMPLEMENTED"
    def fit(self, X, y):
        raise NotImplementedError(
            "Insert and freeze the actual EFMW candidate before confirmatory use."
        )
    def predict_proba(self, X):
        raise NotImplementedError

class EFMWAblation(ForecastModel):
    name = "efmw_ablation_UNIMPLEMENTED"
    def fit(self, X, y):
        raise NotImplementedError(
            "Insert and freeze the recurrence/EFMW-specific ablation."
        )
    def predict_proba(self, X):
        raise NotImplementedError
