from task5_python_module import *
import unittest
class Test_Python_Module(unittest.TestCase):
    '''Testing task5_python_module'''
    def test_is_prime_true(self):
        '''The Number is a prime, should return  True'''
        self.assertTrue(True==is_prime(89))
    def test_is_prime_False(self):
        '''The Number isn't a prime, should return  False'''
        self.assertFalse(True==is_prime(4))
    def test_vowels_found(self):
        '''Vowels should be found, return list should not be empty'''
        self.assertTrue([]!=vowels("Salut toi"))
    def test_vowels_not_found(self):
        '''Vowels should not be found, return list should  be empty'''
        self.assertTrue([]==vowels("qwrtplkjhgfdszxcvbn"))
    def test_factors_found(self):
        '''Factors should  be found, return list should not be empty'''
        self.assertTrue([]!=factors(5))
    def test_factors_not_found(self):
        '''Factors should not be found, return list should  be empty'''
        self.assertTrue([]==factors(3))
    def test_len(self):
        '''Should be True'''
        self.assertTrue(9   ==len("salut toi"))
    


if __name__=="__main__":
    unittest.main()