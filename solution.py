
import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 956745134 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return (loc - len(x)/2 + gamma.ppf(x = alpha/2, a = len(x) , loc=0, scale=1))/(len(x)*43*86), \
           (loc - len(x)/2 + gamma.ppf(x =1- alpha/2, a = len(x) , loc=0, scale=1))/(len(x)*43*86)
