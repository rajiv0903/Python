'''
Created on Aug 8, 2018
@author: rajiv
'''
from math import factorial

'''
    General Formula:
    [expr(item) for item in iterable]
    
'''

words = ("Why sometimes I have believed as many as six" 
         +" impossible things before breakfast").split()

print ([len(word) for word in words])

lengths = []
for word in words:
    lengths.append(len(word))
    
print(lengths)

#Find the length of Factorial value from 1 to 8
f = [len(str(factorial(x))) for x in range(8)]
print (f)

