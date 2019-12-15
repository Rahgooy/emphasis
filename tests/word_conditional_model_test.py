import unittest
import sys
import numpy as np
sys.path.insert(1,'D:\Emphasis_Selection\Github\Taher_Github\emphasis\data')
from reader import read, get_one_hot_matrix
sys.path.insert(2, 'D:\Emphasis_Selection\Github\Taher_Github\emphasis\models')
from word_conditional_model import WordConditionalModel


class TestWordFrequencyMethods(unittest.TestCase):
    def setUp(self):
        self.X, self.y, self.word2Id, self.Id2word, self.dataId2word = read('D:\Emphasis_Selection\Github\Taher_Github\emphasis\input/test_case_models.txt')
        self.x_test = read('D:\Emphasis_Selection\Github\Taher_Github\emphasis\input/test_case_train.txt', word2Id= self.word2Id)
        self.one_hot_X = get_one_hot_matrix(self.X, len(self.word2Id))
        self.one_hot_y = get_one_hot_matrix(self.y, len(self.word2Id))
        model = WordConditionalModel()
        model.fit(np.array(self.one_hot_X), np.array(self.one_hot_y))
        self.model = model.get_model()
        print(self.Id2word)
        self.predictions = model.predict(self.one_hot_X)

    def test_read(self):
        self.assertEqual(self.Id2word, {0:'date', 1:'real', 2:'save', 3:'the', 4:'un'})
        self.assertEqual(self.model[0].tolist(), [7/9, 0, 7/9, 7/9, 0])
        self.assertEqual(self.model[1].tolist(), [0, 8/9, 0, 0, 8/9])
        self.assertEqual(self.model[2].tolist(), [8/9, 0, 8/9, 8/9, 0])
        self.assertEqual(self.model[3].tolist(), [4/9, 0, 4/9, 9/18, 0])
        self.assertEqual(self.model[4].tolist(), [0, 6/9, 0, 0, 6/9])
        self.assertEqual(self.predictions[0].tolist(), [21/27, 0, 24/27, 25/54, 0])
        self.assertEqual(self.predictions[9].tolist(), [0, 16/18, 0, 0, 12/18])
        self.assertEqual(self.predictions[18].tolist(), [0, 0, 0, 9/18, 0])

if __name__ == '__main__':
    unittest.main()