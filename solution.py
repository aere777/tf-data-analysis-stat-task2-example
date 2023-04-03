import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 721467480 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    s_2=0
    n=len(x)
    for ele in x:
        s_2=s_2+(ele-x.mean)**2
    s=(1/(n-1)*s_2)**(1/2)*24
    t=x.mean/(s*n**(1/2))
    return x.mean() -t *s/np.sqrt(n), \
           x.mean() +t *s/np.sqrt(n)
