import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 721467480 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    s_2=0
    alpha = 1 - p
    for ele in x:
        s_2=s_2+np.power(ele-x.mean(),2)
    s=np.sqrt(s_2 / (len(x) - 1))
    return x.mean() + s * norm.ppf(alpha) / np.sqrt(len(x)), \
           x.mean() - s * norm.ppf(alpha) / np.sqrt(len(x))
