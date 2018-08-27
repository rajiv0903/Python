'''
Created on Aug 12, 2018
@author: rajiv
'''

import unittest


def digits(x):
    '''
    >>> digits(4586378)
    [4, 5, 8, 6, 3, 7, 8]
    '''
    
    #import pdb;
    #pdb.set_trace();
    
    digs = []
    
    while x != 0:
        div, mod = divmod(x, 10);
        digs.append(mod);
        x = div;
    return digs;


def is_palindrome(x):
    
    digs = digits(x);
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False;
    return True;
        
class Tests(unittest.TestCase):
    
    def test_negative(self):
        self.assertFalse(is_palindrome(1234));
        
    def test_positive(self):
        self.assertTrue(is_palindrome(1234321));
        
    def test_single_digit(self):
        for i in range(10):
            self.assertTrue(is_palindrome(i));  
            

if __name__ =='__main__':
    unittest.main();

            

    