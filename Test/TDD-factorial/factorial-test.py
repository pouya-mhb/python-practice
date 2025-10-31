import unittest
from factorial import Factorial

factorial = Factorial(5)

class TestFactorial (unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial.calculate_factorial(),120)


if __name__ == "__main__":
    unittest.main()