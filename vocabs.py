import numpy as np
import os
import Read_data_and_Write_results as rw
from nltk.stem import PorterStemmer as stemmer
import json
import codecs


def build_vocab(word_lsts):
    words = [word for sent in word_lsts for word in sent]
    words = set([stemmer().stem(word.lower()) for word in words])
    Id2word = dict(enumerate(sorted(words)))
    word2Id = dict(map(reversed, Id2word.items()))
    return Id2word, word2Id


def get_dataId2word(word_lsts, words_id):
    ids = [id for sent in words_id for id in sent]
    words = [word for sent in word_lsts for word in sent]
    words = [stemmer().stem(word.lower()) for word in words]
    return dict(zip(ids, words))


def report_new_words(vocab_path, text_path, output_path):
    t_dataId2word, te_dataId2word = {}, {}
    
    t_dataId2word = get_dataId2word_from_path(vocab_path)
    te_dataId2word = get_dataId2word_from_path(text_path)
    
    Ids_of_new_words = [Id for Id, word in te_dataId2word.items() if word not in t_dataId2word.values()]
    with codecs.open(output_path, "w", encoding= 'utf-8') as f:
        f.write('\n'.join(Ids_of_new_words))
    #save_json(new_words, output_path)
    
    def get_dataId2word_from_path(path):
        dataId2word = {}
        with codecs.open(path, "r", encoding="utf-8") as f:
            for line in f:
                (key, val) = line.split("\t")
                dataId2word[key] = val
        return dataId2word
        


def save_json(obj, path):
    with codecs.open(path, "w", encoding="utf-8") as J:
        json.dump(obj, J, indent=4)

