"""
    Creating a model & predicting  
"""
from nltk.stem import PorterStemmer as stemmer
from collections import defaultdict
import numpy as np
import pickle 

class WordFrequencyModel:
    def __init__(self):
        pass
    def get_model(self):
        return self.__model
    
    def fit(self, X, y):
        print("training WordFrequencyModel....")
        self.__model = np.zeros((X.shape[1], 1))
        for i in range(X.shape[1]):
            self.__model[i] = y[:, i].sum() / X[:, i].sum()

    def predict(self, X):
        print("predicting....")
        predictions = np.array(X)
        for i in range(X.shape[0]):
            predictions[i][X[i] == 1] = self.__model[X[i] == 1].sum(1)
        return predictions

    def save(self, path):
        pickle.dump(self.model,open(path,"wb"))

    def load(self, path):
        self.model = pickle.load(open(path, "rb"))
