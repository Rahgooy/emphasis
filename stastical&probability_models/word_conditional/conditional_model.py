import Read_data_and_Write_results as rw
from word_conditional_model import WordConditionalModel as wdm
import argparse
import os

import data_helpers as dh

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


if __name__ == "__main__":
    args = get_args()
    path_to_train = os.path.normpath(args.train) #path to semi_train.txt
    path_to_output = os.path.normpath(args.o)  #path to  input/res submition dir
    path_to_test = os.path.normpath(args.test) #path to test.txt
    
    mkdir(path_to_output)
    path_to_output = os.path.join(path_to_output , "res")
    mkdir(path_to_output)

    #_, word_lsts, bio_lsts, _, _, _  = rw.read_data(path_to_train)
    t_x, t_y, t_word2Id, t_Id2word, t_dataId2word = dh.read(path_to_train)
    one_hot_t_x = dh.get_one_hot_matrix(t_x, t_word2Id)
    one_hot_t_y = dh.get_one_hot_matrix(t_y, t_word2Id)
    wdm_model = wdm()
    wdm_model.fit(one_hot_t_x, one_hot_t_y)
    wdm_model.save("WordConditionalModel.pkl")

    # print("training the model ... ")    
    # wdm_model = wdm()
    # wdm_model.fit(word_lsts, bio_lsts)
    # wdm_model.save("WordConditionalModel.pkl")

    # print("testing the model ... ")
    # word_id_lsts, word_lsts, _, _, _, _  = rw.read_data(path_to_test)
    #rw.write_results(word_id_lsts, word_lsts, predictions, os.path.join(path_to_output, "submission.txt"))
    
    te_x, te_dataId2word = dh.read(path_to_test)
    one_hot_te_x = dh.get_one_hot_matrix(te_x, t_word2Id)
    wdm_m = wdm()
    wdm_m.load("WordConditionalModel.pkl")
    predictions = wdm_m.predict(one_hot_te_x)
