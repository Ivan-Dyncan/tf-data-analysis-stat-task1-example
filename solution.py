import pandas as pd
import numpy as np


chat_id = 683312730 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 48
    x = 2*x/t**2
    return np.median(x) # Ваш ответ
