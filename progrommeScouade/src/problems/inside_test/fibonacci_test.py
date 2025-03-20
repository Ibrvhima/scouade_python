import unittest
from src.problems.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_values(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(10), 55)

    def test_large_value(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(35), 9227465)

if __name__ == '__main__':
    unittest.main()
