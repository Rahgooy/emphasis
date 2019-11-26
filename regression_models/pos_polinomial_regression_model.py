import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class linear_regression_model:
    def fit(self, x, y):
        x_r, y_r = [], []
        for i in range(x.shape[1]):
            x_r.append(x[:, i].sum() / np.sum(x))
            y_r.append((y[:, i].sum())/ x[:, i].sum()) 
        p4 = np.poly1d(np.polyfit(x_r, y_r, 1))
        return x_r, y_r, p4
    
    def predict(self, x):
        x_m = []
        for i in range(x.shape[1]):
            x_m.append(x[:, i].sum() / np.sum(x))
        return x_m