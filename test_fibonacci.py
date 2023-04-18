import unittest
from fibonacci import serie_fibonacci
class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, serie_fibonacci(0))
    def test_2(self):
        self.assertEqual(1, serie_fibonacci(2))
    def test_3(self):
        self.assertEqual(2, serie_fibonacci(3))
    def test_4(self):
        self.assertEqual(3, serie_fibonacci(4))
    def test_5(self):
        self.assertEqual(5, serie_fibonacci(5))
    def test_6(self):
        self.assertEqual(8, serie_fibonacci(6))

if __name__ == '__main__':
    unittest.main()