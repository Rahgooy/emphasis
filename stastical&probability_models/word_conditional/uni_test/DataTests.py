import unittest
import numpy as np
from data_helpers import read, get_one_hot_matrix


class TestDataMethods(unittest.TestCase):
    def setUp(self):
        self.x_train, self.y_train, self.word2Id, self.Id2word, self.dataId2word = read('datasets/test_case_train.txt')
        self.one_hot_x = get_one_hot_matrix(self.x_train, len(self.word2Id))
    def test_read(self):
        self.assertEqual(self.word2Id, {'!': 0, 'date': 1, 'day': 2, 'friendship': 3, 'happi': 4, 'real': 5, 'save': 6,
                                        'the': 7, 'un': 8})
                                 

        self.assertEqual(self.Id2word, {0:'!', 1: 'date', 2: 'day', 3: 'friendship', 4: 'happi', 5: 'real', 6: 'save',
                                        7: 'the', 8: 'un'})

        self.assertEqual(self.dataId2word, {'S_0_0' : 'save', 'S_0_1' : 'the', 'S_0_2' : 'date', 
                                            'S_3_0' : 'un', 'S_3_1' : 'real', 
                                            'S_6_0' : 'happi', 'S_6_1' : 'friendship',
                                            'S_6_2' : 'day', 'S_6_3' : '!'})
                                        
        self.assertEqual(self.x_train[0], [6, 7, 1])
        self.assertEqual(self.x_train[10], [8, 5])
        self.assertEqual(self.x_train[18], [4, 3, 2, 0])

        self.assertEqual(self.y_train[0], [1])
        self.assertEqual(self.y_train[1], [6, 7, 1], "it is not working!")
        self.assertEqual(self.y_train[9], [5])
        self.assertEqual(self.y_train[19], [3, 2])

        self.assertEqual(self.one_hot_x.shape, (len(self.x_train), len(self.word2Id)))
        
        self.assertTrue(np.all(self.one_hot_x[0:9, 0:9] == np.array([[0, 1, 0, 0, 0, 0, 1, 1, 0]] * 9)))



if __name__ == '__main__':
    unittest.main()
