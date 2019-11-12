import numpy as np
import os
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import json
import codecs

def build_vocab(word_lsts):
    words = np.unique([stemmer().stem(word.lower()) for word in np.array(word_lsts).ravel()])
    Id2word = dict(enumerate(words))
    word2Id = dict(map(reversed, Id2word.items()))
    return Id2word , word2Id

def get_dataId2word(word_lsts, words_id):
    ids = np.array(words_id).ravel()
    words = [stemmer().stem(word.lower()) for word in np.array(word_lsts).ravel()]
    return dict(zip(ids, words))


def report_new_words(vocab_path, text_path, output_path):
    
    with codecs.open(vocab_path, "r", encoding = "utf-8") as f:
        model = f.read()
    vocab = {item.split("\t")[0]:item.split("\t")[1] for item in model.split("\n") if len(item) != 0}
    
    with codecs.open(text_path, "r", encoding = "utf-8") as f:
        test = f.read()
    text = {item.split("\t")[0]:item.split("\t")[1] for item in test.split("\n") if len(item) != 0}
    
    new_words = {key: value for key, value in text.items() if value not in dict(map(reversed, vocab.items()))} 
    save_json(new_words, output_path)

def save_json(obj, path):
    with codecs.open(path, "w", encoding = "utf-8") as J:
        json.dump(obj, J, indent= 4)