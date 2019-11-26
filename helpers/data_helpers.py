import numpy as np
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import vocabs as v

def read(path, word2Id = None, pos2Id = None):

    def represent_pos_as_matrix(pos_lsts, pos2Id):
        x = []
        for i in range(len(pos_lsts)):
            row = [pos2Id[pos] if pos in pos2Id else -1 for pos in pos_lsts[i]]
            x += [row] * 9
        return x
    
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
    
    def represent_ypos_as_matrix(bios_lsts, pos_lsts, pos2Id):
        y = []
        for i in range(len(pos_lsts)):
            for m in range(9):
                row = []
                for j in range(len(pos_lsts[i])):
                    posId = pos2Id[pos_lsts[i][j]]
                    if bios_lsts[i][j][m * 2] == "I" or bios_lsts[i][j][m * 2] == "B":
                        row.append(posId)
                y.append(row)
        return y

    if(word2Id == None and pos2Id == None):
        words_id, word_lsts, bio_lsts, freq_lsts, prob_lsts, pos_lsts = rw.read_data(path)
        Id2word, word2Id = v.build_vocab(word_lsts)
        Id2pos, pos2Id = v.build_pos_vocab(pos_lsts)
        dataId2word = v.get_dataId2word(word_lsts, words_id)
        
        x = represent_x_as_matrix(word_lsts, word2Id)
        y = represent_y_as_matrix(bio_lsts, word_lsts, word2Id)
        
        x_pos = represent_pos_as_matrix(pos_lsts, pos2Id)
        y_pos = represent_ypos_as_matrix(bio_lsts, pos_lsts, pos2Id)
        
        return x, y, word2Id, Id2word, dataId2word, x_pos, y_pos, pos2Id, Id2pos
    elif(pos2Id != None):
        words_id, _, _, _, _, pos_lsts = rw.read_data(path)
        dataId2pos = v.get_dataId2word(pos_lsts, words_id)
        x = represent_pos_as_matrix(pos_lsts, pos2Id)
        return x, dataId2pos        
    elif(word2Id != None):
        words_id, word_lsts, _, _, _, _ = rw.read_data(path)
        dataId2word = v.get_dataId2word(word_lsts, words_id)
        x = represent_x_as_matrix(word_lsts, word2Id)
        return x, dataId2word



def get_one_hot_matrix(mtx, n):
    #mtx = np.array(mtx)
    matrix = np.zeros([len(mtx), n])
    for i in range(len(mtx)):
        temp = [Id for Id in mtx[i] if Id != -1]
        matrix[i, temp] = 1
    return matrix


def represent_words_as_features(word_lsts, word2Id):
    x = np.zeros( (len(word_lsts)* len(word2Id), (len(word2Id)* 2) ))
    row = 0
    for i in range(len(word_lsts)):
        row = i * len(word2Id)
        for j in range(len(word_lsts[i])):
            if word_lsts[i][j] in word2Id:
                x[row][word2Id[word_lsts[i][j]]] = 1
                for m in range(len(word_lsts[i])):
                    if word_lsts[i][m] in word2Id:
                        x[row][word2Id[word_lsts[i][m]] + len(word2Id)] = 1
                row += 1
    return x


def calculate_probs_for_words_features(mtx, prob_lsts, word_lsts, Id2word):
    y = np.zeros((mtx.shape[0], 1))
    row = 0
    for i in range(mtx.shape[0]):
        for j in range(int((mtx.shape[1]) / 2)):
            if mtx[i][j] == 1:
                cloumn = word_lsts[row].index(Id2word[j])
                y[i] = prob_lsts[row][cloumn]
        if i != 0 and (i + 1) % len(word2Id) == 0:
            row += 1
    return y

if __name__ == "__main__":
    word_lsts = [['save', 'the', 'date'], ['my', 'phone', 'on', 'table']]
    prob_lsts = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6, 0.7]]
    word2Id = {'save': 0, 'the': 1, 'date': 2, 'my': 3, 'phone': 4, 'table': 5}
    Id2word = {0: 'save', 1: 'the', 2: 'date', 3: 'my', 4: 'phone', 5: 'table'}
    x = represent_words_as_features(word_lsts, word2Id)
    y = calculate_probs_for_words_features(x, prob_lsts, word_lsts, Id2word)
    print(x)
    print(y)