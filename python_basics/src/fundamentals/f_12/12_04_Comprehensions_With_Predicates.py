'''
Created on Aug 8, 2018
@author: rajiv
'''
from math import sqrt

def is_prime(x):
    if (x <2):
        return False;
    
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
        
    return True

#Filtering Clause
print ( [x for x in range(101) if is_prime(x)] );
        
        