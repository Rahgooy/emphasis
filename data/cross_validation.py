from evaluate import match_m
from numpy import array
from sklearn.model_selection import KFold
from word_frequency_model import WordFrequencyModel as wfm
import Read_data_and_Write_results as rw
from collections import defaultdict



class CrossValidation:

	def cross_val_score(self, model , train, cv = 5 ):
		word_lsts, bio_lsts, e_freq_lsts = train["word_lsts"], train["bio_lsts"], train["e_freq_lsts"]
		train_index = array([index for index in range(len(word_lsts))])
		kfold = KFold( cv, True, 1)
		result_log , cv_score , kf = {}, 0, 0

		for train_indexes, test_indexes in kfold.split(train_index):
			kf += 1
			print("Cross-validation on Fold-",kf)    
			#prepare train
			train_words = [word_lsts[index] for index in train_index[train_indexes]]
			train_bios = [bio_lsts[index] for index in train_index[train_indexes]]
			#prepare test
			test_words = [word_lsts[index] for index in train_index[test_indexes]]
			test_e_freqs = [e_freq_lsts[index] for index in train_index[test_indexes]]

			model.fit(train_words, train_bios)
			predictions = model.predict(test_words)

			result = match_m(predictions, test_e_freqs)
			score = sum(result.values())/4

			cv_score += score
			result["Overall"] = score
			result_log["Fold-"+str(kf)] = result
			print("Result for Fold-"+str(kf), ": ", result)
			print("---------------------------------")

		cv_score = cv_score/cv

		return result_log, cv_score



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
