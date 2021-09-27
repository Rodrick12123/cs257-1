'''
   primecheckertests.py
   Jeff Ondich, 9 May 2012
   Updated for use in a lab exercise, 4 Nov 2013
'''

import primechecker
import unittest

class PrimeCheckerTester(unittest.TestCase):
    def setUp(self):
        #print("testing setUp")
        self.prime_checker = primechecker.PrimeChecker(100)

    def tearDown(self):
        #print("testing tearDown")
        pass

    @unittest.expectedFailure
    def test_zero(self):
        #print("testing test_zero")
        self.assertFalse(self.prime_checker.is_prime(0))

    def test_two(self):
        #print("testing test_two")
        self.assertTrue(self.prime_checker.is_prime(2))

    def test_prime(self):
        #print("testing test_prime")
        self.assertTrue(self.prime_checker.is_prime(97))

    def test_composite(self):
        #print("testing test_composite")
        self.assertFalse(self.prime_checker.is_prime(96))

    def test_primes_below(self):
        #print("testing test_primes_below")
        self.assertEqual(self.prime_checker.get_primes_below(20), [2, 3, 5, 7, 11, 13, 17, 19])

    @unittest.expectedFailure
    def test_negative(self):
        #print("testing test_negative")
        self.assertFalse(self.prime_checker.is_prime(-4))
    
    @unittest.expectedFailure
    def test_double(self):
        self.assertFalse(self.prime_checker.is_prime(2.7))

    @unittest.expectedFailure
    def test_string(self):
        self.assertFalse(self.prime_checker.is_prime("hello"))

    @unittest.expectedFailure
    def test_primes_below_negative(self):
        self.assertEqual(self.prime_checker.get_primes_below(0), [])

    def test_primes_below_edgecase(self):
        self.assertEqual(self.prime_checker.get_primes_below(2), [])

    def test_primes_below_prime(self):
        self.assertEqual(self.prime_checker.get_primes_below(7), [2,3,5])

    def test_operations(self):
        self.assertTrue(self.prime_checker.is_prime(2+5))

if __name__ == '__main__':
    unittest.main()

