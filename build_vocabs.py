import numpy as np
import os
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import codecs

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
    
def create_wordvocab(word_lsts, words_id, out_path):
    words = [stemmer().stem(item.lower()) for innerlist in word_lsts for item in innerlist]
    ids = [item for innerlist in words_id for item in innerlist]
    word_vocab = []
    with codecs.open(out_path, "w", encoding = "utf-8") as f:
            
        for i in range(len(word_lsts)):
            for j in range(len(word_lsts[i])):
                if word_lsts[i][j] not in word_vocab:
                    word_vocab.append(stemmer().stem(word_lsts[i][j].lower()))
                    f.write(words_id[i][j] + "\t" + word_lsts[i][j] + "\n")
    return word_vocab


def get_id_of_none_wordvocab(model_vocab_path, test_vocab_path, output_path):
    
    id_of_none_wordvocab = []
    
    with codecs.open(model_vocab_path, "r", encoding = "utf-8") as f:
        model = f.read()
    model_words_id = [item.split("\t")[0] for item in model.split("\n") if len(item) != 0]
    model_words = [item.split("\t")[1] for item in model.split("\n") if len(item) != 0]
    
    with codecs.open(test_vocab_path, "r", encoding = "utf-8") as f:
        test = f.read()
    test_words_id = [item.split("\t")[0] for item in test.split("\n") if len(item) != 0]
    test_words = [item.split("\t")[1] for item in test.split("\n") if len(item) != 0]
    
                
    with codecs.open(output_path, "w", encoding = "utf-8") as f:
        for i in range(len(test_words)):
            if test_words[i] not in model_words:
                f.write(test_words_id[i] + "\t" + test_words[i] + "\n")