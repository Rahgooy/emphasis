import numpy as np
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import vocabs as v
    
def read(path, word2Id = None):
        
    def get_one_hot_matrix(mtx, word2Id, lenght = 9):
        matrix = build_matrix(len(mtx.shape[0] * lenght), len(word2Id))
        for i in range(len(mtx)):
            temp = [Id for Id in mtx[i] if Id != -1]
            matrix[i*lenght:(i+1)*lenght, temp] = 1
        return matrix

    def build_matrix(number_of_sentences, number_of_words):
        word_matrix = np.zeros((number_of_sentences, number_of_words))
        return word_matrix          

    def represent_x_as_matrix(word_lsts, word2Id):
        x, temp = [], []
        for i in range(len(word_lsts)):
            temp = [word2Id[stemmer().stem(word.lower())]
                    if stemmer().stem(word.lower()) in word2Id else -1 
                    for word in word_lsts[i]]
            x.append(temp)
        return x

    def represent_y_as_matrix(bios_lsts, words_lsts, word2Id):
        y = []
        for i in range(len(words_lsts)):
            for m in range(9):
                temp = []
                for j in range(len(words_lsts[i])):
                    wordId = word2Id[stemmer().stem(words_lsts[i][j].lower())] 
                    if bios_lsts[i][j][m * 2] == "I" or bios_lsts[i][j][m * 2] == "B":
                        temp.append(wordId)
                y.append(temp)
        return y   

    words_id, word_lsts, bio_lsts, freq_lsts, prob_lsts, pos_lsts = rw.read_data(path)
    Id2word, word2Id = v.build_vocab(word_lsts)
    dataId2word = v.get_dataId2word(word_lsts, words_id)
    x = represent_x_as_matrix(word_lsts, word2Id)
    y = represent_y_as_matrix(bio_lsts, word_lsts, word2Id)
    x_one_hot = get_one_hot_matrix(x, word2Id)
    y_one_hot = get_one_hot_matrix(y, word2Id, 1)
    return x, y, word2Id, Id2word, dataId2word



