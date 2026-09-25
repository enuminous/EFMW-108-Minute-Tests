import numpy as np

def binary_log_loss(y, p):
    y = np.asarray(y, dtype=float)
    p = np.clip(np.asarray(p, dtype=float), 1e-12, 1-1e-12)
    return float(-np.mean(y*np.log(p) + (1-y)*np.log(1-p)))

def per_item_binary_log_loss(y, p):
    y = np.asarray(y, dtype=float)
    p = np.clip(np.asarray(p, dtype=float), 1e-12, 1-1e-12)
    return -(y*np.log(p) + (1-y)*np.log(1-p))
