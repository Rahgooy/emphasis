"""
    Creating conditional model & predicting  
"""

import numpy as np
from nltk.stem import PorterStemmer as stemmer
import pickle 

class WordConditionalModel:

    def __init__(self):
        self.__words_matrix = 0
        self.__bios_matrix = 0
        self.__model = 0
        self.__words = []
    
    def __build_matrix(self, number_of_sentences, number_of_words):
        word_matrix = np.zeros((number_of_sentences, number_of_words))
        return word_matrix


    def __represent_sentences_as_matrix(self, words_lsts):
        matrix = self.__build_matrix(len(words_lsts * 9), len(self.__words))
        for i in range(len(words_lsts)):
            for j in range(len(words_lsts[i])):
                mj = self.__words.index( stemmer().stem(words_lsts[i][j].lower()))
                matrix[i*9:(i+1)*9, mj] = 1
        return matrix

    def __represent_bios_as_matrix(self, bios_lsts, words_lsts):
        matrix = self.__build_matrix(len(words_lsts * 9), len(self.__words))
        for i in range(len(words_lsts)):
            for j in range(len(words_lsts[i])):
                d = self.__words.index( stemmer().stem(words_lsts[i][j].lower()))
                for m in range(9):
                    if bios_lsts[i][j][m * 2] == "I" or bios_lsts[i][j][m * 2] == "B":
                        matrix[(i * 9) + m][d] = 1
        return matrix

    def __calculate_condetional_probs(self, w_i, w_j):
        occurrenece_of_wi_and_wj, bold_wi = 0, 0
        occurrenece_of_wi_and_wj = (self.__words_matrix[:, w_i] * self.__words_matrix[:, w_j]).sum()
        y = self.__words_matrix[:, w_i] * self.__words_matrix[:, w_j]
        bold_wi = (y * self.__bios_matrix[:, w_i]).sum()
        self.__model[w_i][w_j] = (bold_wi / occurrenece_of_wi_and_wj) if occurrenece_of_wi_and_wj else 0
        #print("[{}], [{}] = {}".format(self.__words[w_i], self.__words[w_j], self.__model[w_i][w_j]))

    def fit(self, words_lsts, bios_lsts):
        print("training WordConditionalModel....")
        self.__words = []
        words_vocab = [stemmer().stem(word.lower()) for innerlist in words_lsts for word in innerlist]
        for word in words_vocab:
            if word not in self.__words:
                self.__words.append(word)
        
        self.__model = self.__build_matrix(len(self.__words), len(self.__words))
        self.__words_matrix = self.__represent_sentences_as_matrix(words_lsts)
        self.__bios_matrix = self.__represent_bios_as_matrix(bios_lsts, words_lsts)
        print("vocab lenghts: " , len(self.__words))
        for i in range(len(self.__words)):
            if i%100 == 0:
                print(i , end = ' ')
            for j in range(len(self.__words)):
                self.__calculate_condetional_probs(i, j)
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