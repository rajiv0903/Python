'''
Created on Aug 8, 2018
@author: rajiv
'''

import math as m

#Find the length of Factorial value from 1 to 8
f = {len(str(m.factorial(x))) for x in range(8)}
print (f)