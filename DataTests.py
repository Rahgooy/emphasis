import unittest

from data_helpers import read, get_one_hot_matrix


class TestDataMethods(unittest.TestCase):
    def setUp(self):
        self.x_train, self.y_train, self.word2Id, self.Id2word, self.dataId2word = read('datasets/test_case_train.txt')

    def test_read(self):
        print(self.word2Id)
        self.assertEqual(self.word2Id, {'!': 0, 'date': 1, 'day': 2, 'friendship': 3, 'happi': 4, 'real': 5, 'save': 6,
                                        'the': 7, 'un': 8})
        self.assertEqual(self.x_train[0], [6, 7, 1])
        self.assertEqual(self.x_train[10], [8, 5])
        self.assertEqual(self.x_train[18], [4, 3, 2, 0])


if __name__ == '__main__':
    unittest.main()
