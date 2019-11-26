import sys
sys.path.insert(0, "D:\Emphasis_Selection\Main\Expreiments")
#sys.path.append('../')

import Read_data_and_Write_results as rw
import data_helpers as dh
import numpy as np

def regression():
    words_Id , word_lsts, _, _, prob_lsts, _ = rw.read_data("regression_models/uni_test_set/test_case_train.txt")
    
if __name__ == "__main__":
    regression()
