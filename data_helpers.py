import numpy as np
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import vocabs as v
    
def reader(path):
        
    def represent_x_as_matrix(words_lsts, word2Id):
        matrix = build_matrix(len(words_lsts * 9), len(word2Id))
        for i in range(len(words_lsts)):
            for j in range(len(words_lsts[i])):
                wordId = word2Id[stemmer().stem(words_lsts[i][j].lower())]
                matrix[i*9:(i+1)*9, wordId] = 1
        return matrix


    def represent_y_as_matrix(bios_lsts, words_lsts, word2Id):
        matrix = build_matrix(len(words_lsts * 9), len(word2Id))
        for i in range(len(words_lsts)):
            for j in range(len(words_lsts[i])):
                wordId = word2Id[stemmer().stem(words_lsts[i][j].lower())]
                for m in range(9):
                    if bios_lsts[i][j][m * 2] == "I" or bios_lsts[i][j][m * 2] == "B":
                        matrix[(i * 9) + m][wordId] = 1
        return matrix


    def build_matrix(number_of_sentences, number_of_words):
        word_matrix = np.zeros((number_of_sentences, number_of_words))
        return word_matrix
    
    words_id, word_lsts, bio_lsts, freq_lsts, prob_lsts, pos_lsts = rw.read_data(path)
    Id2word, word2Id = v.build_vocab(word_lsts)
    dataId2word = v.get_dataId2word(word_lsts, words_id)
    x = represent_x_as_matrix(word_lsts, word2Id)
    y = represent_y_as_matrix(bio_lsts, word_lsts, word2Id)
    return x, y, word2Id, Id2word, dataId2word
