import numpy as np
import os
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer

def build_vocab(str_lsts):
    vocab_encoder = {}
    vocab_id = 0
    for e in str_lsts:
        if e not in vocab_encoder:
            vocab_encoder[e] = vocab_id
            vocab_id += 1
    vocab_decoder = {value: key for key, value in vocab_encoder.items()}
    return vocab_encoder, vocab_decoder

def create_vocabs(input_path, output_path):
    _, word_vocab, _, _, _, pos_vocab = rw.read_data(input_path)
    
    pos_vocab = [item for innerlist in pos_vocab for item in innerlist]
    word_vocab = [stemmer().stem(item.lower()) for innerlist in word_vocab for item in innerlist]
    
    pos_encoder, pos_decoder = build_vocab(pos_vocab)
    word_encoder, word_decoder = build_vocab(word_vocab)
    
    
    np.save( os.path.join(output_path,"pos_decoder.npy"), pos_decoder)
    np.save(os.path.join(output_path, "pos_encoder.npy"), pos_encoder)
    
    np.save(os.path.join(output_path, "word_decoder.npy"), word_decoder)
    np.save(os.path.join(output_path, "word_encoder.npy"), word_encoder)
    
