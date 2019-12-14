"""
Creating conditional model & predicting  
"""

import numpy as np
from nltk.stem import PorterStemmer as stemmer
import pickle 

class WordConditionalModel:
    
    def __init__(self):
        pass
    def get_model(self):
        return self.__model

    def __calculate_condetional_probs(self,X, y, w_i, w_j):
        wi_wj = X[:, w_i] * X[:, w_j]
        wi_wj_count = wi_wj.sum()
        bold_wi = (wi_wj * y[:, w_i]).sum()
        self.__model[w_i][w_j] = (bold_wi / wi_wj_count) if wi_wj_count else 0

    def fit(self, X, y):
        
        self.__model = np.zeros((X.shape[1], X.shape[1]))
        print("training WordConditionalModel....")
        for i in range(X.shape[1]):
            for j in range(X.shape[1]):
                self.__calculate_condetional_probs(X, y, i, j)

    def predict(self, X):
        predictions = np.array(X)
        for i in range(X.shape[0]):
            predictions[i][X[i] == 1] = (self.__model[X[i] == 1][:, X[i] == 1].sum(1))/ (X[i] == 1).sum()
        return predictions

    def save(self, path):
        model = {"__words":self.__words, "__model":self.__model}
        pickle.dump(model,open(path,"wb"))

    def load(self, path):
        model = pickle.load(open(path, "rb"))
        self.__words, self.__model = model["__words"], model["__model"]