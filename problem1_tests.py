import unittest
from problem1_code import determine_primes

class TestDeterminePrimes(unittest.TestCase):
    def test_22_number(self):
        result = determine_primes(22)
        self.assertEqual(result, ([2, 3, 5, 7, 11, 13, 17, 19], 2), "Incorrect prime list for up to 22.")

    def test_with_integer_input(self):
        result = determine_primes(30)
        self.assertEqual(result, ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 10), "Should return all primes up to 30 with correct traverse count.")

    def test_11_number(self):
        result = determine_primes(11)
        self.assertEqual(result, ([2, 3, 5, 7, 11], 2), "Incorrect prime list for up to 11.")

    #accept only a single integer value as input; any other input type should throw an exception
    def test_with_non_integer_input(self):
        with self.assertRaises(Exception):
            determine_primes('a')

    def test_with_negative_input(self):
        result = determine_primes(-10)
        self.assertEqual(result, ([], 0), "expecting empty list for negative input.")

    def test_with_zero_input(self):
        result = determine_primes(0)
        self.assertEqual(result, ([], 0), "expecting empty list for zero input.")

    def test_with_one_input(self):
        result = determine_primes(1)
        self.assertEqual(result, ([], 0), "expecting empty list for input of one.")

if __name__ == '__main__':
    unittest.main()
