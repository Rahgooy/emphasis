"""
    Creating a model & predicting  
"""
from nltk.stem import PorterStemmer as stemmer
from collections import defaultdict
import pickle 

class WordFrequencyModel:
    def __init__(self, word_lsts, bio_lsts, lowercase = True, stemming = True):
        self.model = {}
        self.bio_freq_dict = defaultdict(int)
        self.occurrences_dict = defaultdict(int)
        self.word_lsts = word_lsts
        self.bio_lsts = bio_lsts
        self.lowercase = lowercase
        self.stemming = stemming
    

    def fit(self):
        """
        Build a model based on bio_freq of words
        """
        self.bio_freq_dict = defaultdict(int)
        self.occurrences_dict = defaultdict(int)

        for i in range(len(self.bio_lsts)):
            for j in range(len(self.bio_lsts[i])):
                bio = self.bio_lsts[i][j].split("|")
                word_stem = self.word_lsts[i][j].lower() if self.lowercase else self.word_lsts[i][j]
                word_stem = stemmer().stem(word_stem) if self.stemming else word_stem
                self.bio_freq_dict[word_stem] += (int(bio[0]) + int(bio[1]))
                self.occurrences_dict[word_stem] += 1

        for word ,bio_freq in self.bio_freq_dict.items():
            self.model[word] = (bio_freq / ( self.occurrences_dict[word] * 9))


    def predict(self, word_lsts):
        """
        Predicting on the test set
        param: word_lsts: raw lists of the test set
        return: predictions: list of predictions
        """
        predictions = []
        for i in range(len(word_lsts)):
            word_prediction = []
            for j in range(len(word_lsts[i])):
                word_stem = word_lsts[i][j].lower() if self.lowercase else word_lsts[i][j]
                word_stem = stemmer().stem(word_stem) if self.stemming else word_stem
                word_prediction.append(self.model[word_stem] if word_stem in self.model.keys() else 0)
            predictions.append(word_prediction)
        return predictions


    def save(self, path):
        pickle.dump(self.model,open(path,"wb"))

    def load(self, path):
        self.model = pickle.load(open(path, "rb"))
