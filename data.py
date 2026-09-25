"""Data contract for EFMW-108."""
from dataclasses import dataclass
import numpy as np

@dataclass
class Dataset:
    X_train: np.ndarray
    y_train: np.ndarray
    X_test: np.ndarray
    y_test: np.ndarray
    test_unit_ids: np.ndarray

def load_confirmatory_dataset(horizon_minutes: int, condition: str) -> Dataset:
    raise NotImplementedError(
        "Register the real dataset adapter before confirmatory execution. "
        "It must enforce temporal causality and identical information access."
    )
