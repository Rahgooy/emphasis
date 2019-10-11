import Read_data_and_Write_results as rw
from word_frequency_model import WordFrequencyModel as wfm
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


if __name__ == "__main__":
    args = get_args()
    path_to_train = os.path.normpath(args.train) #path to semi_train.txt
    path_to_output = os.path.normpath(args.o)  #path to  input/res submition dir
    path_to_test = os.path.normpath(args.test) #path to test.txt
    
    mkdir(path_to_output)
    path_to_output = os.path.join(path_to_output , "res")
    mkdir(path_to_output)

    _, word_lsts, _, bio_lsts, _, _  = rw.read_data(path_to_train)

    print("training the model ... ")    
    wfm_model = wfm()
    wfm_model.fit(word_lsts, bio_lsts)
    wfm_model.save("WordFrequencyModel.pkl")

    print("testing the model ... ")
    word_id_lsts, word_lsts, _, _, _, _  = rw.read_data(path_to_test)
    wfm_m = wfm(word_lsts, bio_lsts)
    wfm_m.load("WordFrequencyModel.pkl")
    predictions = wfm_m.predict(word_lsts)
    rw.write_results(word_id_lsts, word_lsts, predictions, os.path.join(path_to_output, "submission.txt"))