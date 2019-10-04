"""
    This script gets the data and creates two dictionaries(decoding, encoding)
    e.g for using encoder
        word_vocab_encoder = np.load("word_vocab_encoder.npy", allow_pickle = True) 
        word_id = word_vocab_encoder.item().get("save") #output is a word id
    e.g for using decoder
        word_vocab_decoder = np.load("word_vocab_decoder.npy", allow_pickle = True) 
        word = word_vocab_deecoder.item().get(0) #output is a word for word_id = 0
"""


from nltk.stem import PorterStemmer
import numpy as np
import Read_data_and_Write_results as rw


stemmer = PorterStemmer()
_, word_lists, _, _, _, _ = rw.read_data("train.txt")

word_vocab = {}
vocab_id = 0
for i in range(len(word_lists)):
    for j in range(len(word_lists[i])):
        duplicate = False
        word = stemmer.stem(word_lists[i][j].lower())
        for key, value in word_vocab.items():
            if word == value:
                duplicate = True
        if not duplicate :
            word_vocab[vocab_id] = word
            vocab_id += 1

inv_word_vocab = {value: key for key, value in word_vocab.items()}

np.save("word_vocab_decoder.npy", word_vocab)
np.save("word_vocab_encoder.npy", inv_word_vocab)