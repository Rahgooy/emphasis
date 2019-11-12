import numpy as np
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import vocabs as v

class Read:

    def __init__(self):
        self.__Id2word = {}
        self.__word2Id = {}
        self.__dataId2word = {}
    
    def read(self, path):
        words_id, word_lsts, bio_lsts, freq_lsts, prob_lsts, pos_lsts = rw.read_data(path)
        self.__Id2word , self.__word2Id = v.build_vocab(word_lsts)
        self.__dataId2word = v.get_dataId2word(word_lsts, words_id)
        x = self.__represent_x_as_matrix(word_lsts)
        y = self.__represent_y_as_matrix(bio_lsts, word_lsts)
        return x, y, self.__word2Id, self.__Id2word, self.__dataId2word


    def __represent_x_as_matrix(self, words_lsts):
        matrix = self.__build_matrix(len(words_lsts * 9), len(self.__word2Id))
        for i in range(len(words_lsts)):
            for j in range(len(words_lsts[i])):
                wordId = self.__word2Id[stemmer().stem(words_lsts[i][j].lower())]
                matrix[i*9:(i+1)*9, wordId] = 1
        return matrix


    def __represent_y_as_matrix(self, bios_lsts, words_lsts):
        matrix = self.__build_matrix(len(words_lsts * 9), len(self.__word2Id))
        for i in range(len(words_lsts)):
            for j in range(len(words_lsts[i])):
                wordId = self.__word2Id[stemmer().stem(words_lsts[i][j].lower())]
                for m in range(9):
                    if bios_lsts[i][j][m * 2] == "I" or bios_lsts[i][j][m * 2] == "B":
                        matrix[(i * 9) + m][wordId] = 1
        return matrix


    def __build_matrix(self, number_of_sentences, number_of_words):
        word_matrix = np.zeros((number_of_sentences, number_of_words))
        return word_matrix