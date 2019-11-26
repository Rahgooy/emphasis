from evaluate import match_m
from numpy import array
from sklearn.model_selection import KFold

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

