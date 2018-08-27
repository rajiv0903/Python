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
print(next(g))# Throw StopIteration 