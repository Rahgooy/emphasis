import Read_data_and_Write_results as rw
from collections import defaultdict
from nltk.stem import PorterStemmer as stemmer
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-tr', '--train', help="path to semi_train.txt dataset")
    parser.add_argument('-ts', '--test', help="path to test.txt dataset")
    parser.add_argument('-o', help="path to submition output input/res",default="input")
    args = parser.parse_args()
    if args.train is None or args.test is None:
        parser.print_usage()
        exit()
    return args

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def build_model(bio_freqs_word, occurrences):
    model = {}
    for word ,bio_freq in bio_freqs_word.items():
            model[word] = (bio_freq / ( occurrences[word] * 9))
    return model

def predict(word_lsts, model):
    predictions = []
    for i in range(len(word_lsts)):
        word_prediction = []
        for j in range(len(word_lsts[i])):
            word_stem = stemmer().stem(word_lsts[i][j].lower())
            if word_stem in model.keys():
                word_prediction.append(model[word_stem])
            else:
                word_prediction.append(0)
        predictions.append(word_prediction)
    return predictions


if __name__ == "__main__":
    args = get_args()
    path_to_train = os.path.normpath(args.train) #path to semi_train.txt
    path_to_output = os.path.normpath(args.o)  #path to  input/res submition dir
    path_to_test = os.path.normpath(args.test) #path to test.txt
    
    mkdir(path_to_output)
    path_to_output = os.path.join(path_to_output , "res")
    mkdir(path_to_output)

    _, word_lsts, _, bio_freqs, _, _  = rw.read_data(path_to_train)

    print("training the model ... ")
    bio_freqs_word = defaultdict(int)
    occurrences_word = defaultdict(int)
    for i in range(len(bio_freqs)):
        for j in range(len(bio_freqs[i])):
            bio = bio_freqs[i][j].split("|")
            word_stem = stemmer().stem(word_lsts[i][j].lower())
            bio_freqs_word[word_stem] += (int(bio[0]) + int(bio[1]))
            occurrences_word[word_stem] += 1
    
    
    model = build_model(bio_freqs_word, occurrences_word)

    print("testing the model ... ")
    word_id_lsts, word_lsts, _, _, _, _  = rw.read_data(path_to_test)
    predictions = predict(word_lsts, model)
    rw.write_results(word_id_lsts, word_lsts, predictions, os.path.join(path_to_output, "submission.txt"))