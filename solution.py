import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 721467480 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    sumOfPow=0
    alpha = 1 - p
    for ele in x:
        sumOfPow=sumOfPow+ele**2
    return np.sqrt(sumOfPow / chi2(2 * len(x)).ppf(q=1 - alpha / 2) / 24), \
           np.sqrt(sumOfPow / chi2(2 * len(x)).ppf(q=alpha / 2) / 24)
