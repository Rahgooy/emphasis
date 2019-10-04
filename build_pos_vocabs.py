"""
    This script gets the data and creates two dictionaries(decoding, encoding) for pos tags
    e.g for using encoder
        pos_vocab_encoder = np.load("pos_vocab_encoder.npy", allow_pickle = True) 
        pos_id = pos_vocab_encoder.item().get("NN") #output is a pos id
    e.g for using decoder
        pos_vocab_decoder = np.load("pos_vocab_decoder.npy", allow_pickle = True) 
        pos = pos_vocab_decoder.item().get(2) #output is a pos for pos_id = 2
"""

import numpy as np
import Read_data_and_Write_results as rw

_, _, _, _, _, pos_lsts = rw.read_data("train.txt")

pos_vocab = {}
vocab_id = 0
for i in range(len(pos_lsts)):
    for j in range(len(pos_lsts[i])):
        duplicate = False
        pos = pos_lsts[i][j]
        for key, value in pos_vocab.items():
            if pos == value:
                duplicate = True
        if not duplicate:
            pos_vocab[vocab_id] = pos
            vocab_id += 1

inv_pos_vocab = {value: key for key, value in pos_vocab.items()}

np.save("pos_vocab_decoder.npy", pos_vocab)
np.save("pos_vocab_encoder.npy", inv_pos_vocab)