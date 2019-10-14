from cross_validation import CrossValidation
from word_frequency_model import WordFrequencyModel as wfm
import Read_data_and_Write_results as rw
from collections import defaultdict

def set_numbers_to_0( word_lsts, pos_lsts ):
    for i in range(len(pos_lsts)):
        for j in range(len(pos_lsts[i])):
            if pos_lsts[i][j] == "CD":
                word_lsts[i][j] = "0"
    return word_lsts

def perform_cv(dataset_path, _stemming = True, set_numbers_0 = False):
    _, word_lsts, _, bio_lsts, e_freq_lsts, pos_lsts = rw.read_data(dataset_path)
    if set_numbers_0:
        word_lsts = set_numbers_to_0(word_lsts, pos_lsts)
    train = { "word_lsts":word_lsts, "bio_lsts":bio_lsts, "e_freq_lsts":e_freq_lsts } 
    cv = CrossValidation()
    rs , _ = cv.cross_val_score(wfm(stemming=_stemming), train)

    overalls = defaultdict(int)
    for _, fold_rs in rs.items():
        for m, score in fold_rs.items():
            overalls[m] += score
    
    averages = { key:(val/5) for key, val in overalls.items() }
    print("----------------------------------------")
    print(dataset_path)
    print(averages)
    print("----------------------------------------")


# perform_cv("datasets/train-train-split.txt", set_numbers_0 = True)
# perform_cv("datasets/q-train-train-split.txt", set_numbers_0 = True)
# perform_cv("datasets/s-train-train-split.txt", set_numbers_0 = True)