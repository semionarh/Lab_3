import sys
import unittest
from random import randint
import main


class TestMethods(unittest.TestCase):

    def test_det_2(self):
        self.assertEqual(main.get_det([[7, 5], [2, 3]]), 11)

    def test_det_3(self):
        self.assertEqual(main.get_det([[2, 0, -1], [6, 4, 3], [-2, 1, 4]]), 12)

    def test_det_4(self):
        self.assertEqual(main.get_det([[4, 6, -3, 2], [1, 3, 5, -7], [2, 2, -2, 2], [8, -5, 4, 3]]), 84)

    def test_det_0(self):
        self.assertEqual(main.get_det([[2, 4, 6], [1, 3, 5], [7, 8, 9]]), 0)

    def test_reverse_2(self):
        self.assertEqual(main.reverse_matrix([[1, 2], [3, 4]]), [[-2, 1], [1.5, -0.5]])

    def test_reverse_3(self):
        self.assertEqual(main.reverse_matrix([[1, 1, 1], [-1, 0, 0], [0, 0, 1]]), [[0, -1, 0], [1, 1, -1], [0, 0, 1]])

    def test_vector_3(self):
        self.assertEqual(main.vector_mult([[6, 3, 11], [12, 4, 7], [1, 1, 2]], [0, 0, 10]), [110, 70, 20])

    def test_unknown_members_1(self):
        self.assertEqual(main.unknown_members([[1, 2, 5], [6, 7, 2], [3, 1, 4]], [11, 10, 9]), [0.27058823529411713, 0.6588235294117646, 1.8823529411764701])

    def test_unknown_members_2(self):
        self.assertEqual(main.unknown_members([[1, 1, 0], [4, 2, 0], [1, 3, 5]], [12, 20, 13]), [-2.0, 14.0, -5.4])

    def test_unknown_members_3(self):
        self.assertEqual(main.unknown_members([[1, 2, -3], [-1, 5, 4], [-2, 1, 5]], [-10, -15, -20]), [39.58333333333333, -5.416666666666666, 12.916666666666664])


if __name__ == '__main__':
    unittest.main()