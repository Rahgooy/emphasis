"""
    Creating conditional model & predicting  
"""

import numpy as np
from nltk.stem import PorterStemmer as stemmer
import pickle 

class WordConditionalModel:

    def __init__(self):
        pass

    def __calculate_condetional_probs(self,x, y, w_i, w_j):
        wi_wj = x[:, w_i] * x[:, w_j]
        wi_wj_count = wi_wj.sum()
        bold_wi = (wi_wj * y[:, w_i]).sum()
        self.__model[w_i][w_j] = (bold_wi / wi_wj_count) if wi_wj_count else 0

    def fit(self, x, y):
        self.__model = np.zeros((x.shape[1], x.shape[1]))
        print("training WordConditionalModel....")
        for i in range(x.shape[1]):
            for j in range(x.shape[1]):
                self.__calculate_condetional_probs(x, y, i, j)

    def predict(self, x):
        predictions = np.array(x)
        
        for i in range(x.shape[0]):
            predictions[i][x[i] == 1] = self.__model[x[i] == 1].sum(1)
        return predictions

    def save(self, path):
        model = {"__words":self.__words, "__model":self.__model}
        pickle.dump(model,open(path,"wb"))

    def load(self, path):
        model = pickle.load(open(path, "rb"))
        self.__words, self.__model = model["__words"], model["__model"]