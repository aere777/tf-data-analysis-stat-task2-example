import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 721467480 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return x.mean() - np.sqrt(np.var(x)) * norm.ppf(1-alpha/2) / np.sqrt(len(x)), \
           x.mean() - np.sqrt(np.var(x))* norm.ppf(alpha/2) / np.sqrt(len(x))
