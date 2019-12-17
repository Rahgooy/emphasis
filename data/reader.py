import numpy as np
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import vocabs as v

def read(path, word2Id=None):

    def vocab_features_X(word_lsts, word2Id, num_of_annotators = 1):
        x = []
        for i in range(len(word_lsts)):
            row = [stemmer().stem(word.lower()) for word in word_lsts[i]]
            row = [word2Id[word] if word in word2Id else -1 for word in row]
            x += [row] * num_of_annotators
        return x

    def y_as_one_hot(bios_lsts, words_lsts, word2Id, num_of_annotators = 1):
        y = []
        for i in range(len(words_lsts)):
            for m in range(num_of_annotators):
                row = []
                for j in range(len(words_lsts[i])):
                    if bios_lsts[i][j][m * 2] == "I" or bios_lsts[i][j][m * 2] == "B":
                        row.append(1)
                    else:
                        row.append(0)
                y.append(row)
        return y

    if word2Id == None:
        words_id, word_lsts, bio_lsts, freq_lsts, prob_lsts, pos_lsts = rw.read_data(path)
        Id2word, word2Id = v.build_vocab(word_lsts)
        dataId2word = v.get_dataId2word(word_lsts, words_id)
        annotators = int(freq_lsts[0][0][0]) + int(freq_lsts[0][0][2]) + int(freq_lsts[0][0][4])
        x = vocab_features_X(word_lsts, word2Id, num_of_annotators = annotators)
        y = y_as_one_hot(bio_lsts, word_lsts, word2Id, annotators)
        return x, y, word2Id, Id2word, dataId2word
    else:
        _, word_lsts, _, _, _, _ = rw.read_data(path)
        x = vocab_features_X(word_lsts, word2Id)
        return x

