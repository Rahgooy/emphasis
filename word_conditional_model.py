"""
    Creating conditional model & predicting  
"""

import numpy as np
from nltk.stem import PorterStemmer as stemmer
import pickle 

class WordConditionalModel:

    def __init__(self):
           self.__model = 0

    def __calculate_condetional_probs(self,x, y, w_i, w_j):
        occurrenece_of_wi_and_wj, bold_wi = 0, 0
        occurrenece_vector = x[:, w_i] * x[:, w_j]
        occurrenece_of_wi_and_wj = occurrenece_vector.sum()
        bold_wi = (occurrenece_vector * y[:, w_i]).sum()
        self.__model[w_i][w_j] = (bold_wi / occurrenece_of_wi_and_wj) if occurrenece_of_wi_and_wj else 0

    def fit(self, x, y):
        print("training WordConditionalModel....")
        for i in range(x.shape[1]):
            if i%100 == 0:
                print(i , end = ' ')
            for j in range(x.shape[1]):
                self.__calculate_condetional_probs(x, y, i, j)
        print()

    def predict(self, word_lsts):
        predictions = []
        for i in range(len(word_lsts)):
            prediction = []
            for j in range(len(word_lsts[i])):
                word_ij = stemmer().stem(word_lsts[i][j].lower())
                if word_ij in self.__words:
                    w_i = self.__words.index( word_ij )
                    s = 0
                    for m in range(len(word_lsts[i])):
                        word_im = stemmer().stem(word_lsts[i][m].lower())
                        if word_im in self.__words:
                            w_j = self.__words.index( word_im )
                            s += self.__model[w_i][w_j]
                    prediction.append(s / len(word_lsts[i]))
                else:
                    prediction.append(0)
            predictions.append(prediction)
        return predictions
    
    
    def save(self, path):
        model = {"__words":self.__words, "__model":self.__model}
        pickle.dump(model,open(path,"wb"))

    def load(self, path):
        model = pickle.load(open(path, "rb"))
        self.__words, self.__model = model["__words"], model["__model"]