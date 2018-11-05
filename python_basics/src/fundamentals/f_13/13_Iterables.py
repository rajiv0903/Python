'''
Created on Aug 8, 2018
@author: rajiv
'''

iterable = ['Rajiv', 'Tithi', 'Mahika']

iterator = iter(iterable);

print (next(iterator));
print (next(iterator));
print (next(iterator));
#print (next(iterator));# Throw StopIteration 

def gen123():
    yield 1
    yield 3
    yield 5
    
g = gen123()

print(type(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))# Throw StopIteration 

#itertools module
from itertools import islice, count
from math import sqrt

def is_prime(x):
    if (x <2):
        return False;
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True;

thousand_prime = islice(( x for x in count() if is_prime(x)), 1000)
print(type(thousand_prime))
print(list(thousand_prime))

print (any([False, True, False]))

print( all([False, True]))


 