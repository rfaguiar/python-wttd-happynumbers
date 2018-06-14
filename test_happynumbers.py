import unittest

from happynumbers import happy, sum_of_squares


class HappyNumbersTest(unittest.TestCase):
    def test_true_when_1(self):
        self.assertTrue(happy(1))

    def test_true_when_10(self):
        self.assertTrue(happy(10))

    def test_true_when_100(self):
        self.assertTrue(happy(100))

    def test_false_when_4(self):
        self.assertFalse(happy(4))

    def test_say_10_when_130(self):
        self.assertEquals(sum_of_squares(130), 10)

    def test_true_when_130(self):
        self.assertTrue(happy(130))

    def test_true_when_97(self):
        self.assertTrue(happy(97))
