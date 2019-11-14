import numpy as np
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import vocabs as v


def read(path, word2Id=None):
    def represent_x_as_matrix(word_lsts, word2Id):
        x = []
        for i in range(len(word_lsts)):
            row = [stemmer().stem(word.lower()) for word in word_lsts[i]]
            row = [word2Id[word] if word in word2Id else -1 for word in row]
            x += [row] * 9
        return x

    def represent_y_as_matrix(bios_lsts, words_lsts, word2Id):
        y = []
        for i in range(len(words_lsts)):
            for m in range(9):
                row = []
                for j in range(len(words_lsts[i])):
                    wordId = word2Id[stemmer().stem(words_lsts[i][j].lower())]
                    if bios_lsts[i][j][m * 2] == "I" or bios_lsts[i][j][m * 2] == "B":
                        row.append(wordId)
                y.append(row)
        return y

    words_id, word_lsts, bio_lsts, freq_lsts, prob_lsts, pos_lsts = rw.read_data(path)
    Id2word, word2Id = v.build_vocab(word_lsts)
    dataId2word = v.get_dataId2word(word_lsts, words_id)
    x = represent_x_as_matrix(word_lsts, word2Id)
    y = represent_y_as_matrix(bio_lsts, word_lsts, word2Id)
    return x, y, word2Id, Id2word, dataId2word


def get_one_hot_matrix(mtx, n):
    matrix = np.zeros([mtx.shape[0], n])
    for i in range(len(mtx)):
        temp = [Id for Id in mtx[i] if Id != -1]
        matrix[i, temp] = 1
    return matrix
