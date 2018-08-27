'''
Created on Aug 6, 2018
@author: rajiv
'''

a = 1234 #Same Object 1234
print(id(a)) #id prints the hashcode

b = 1234 #Same Object 1234
print(id(b))

c = 4321 #Different Object 4321
print(id(c))

print(b is a)
print(c is a)
b = a
c = a
print(id(a) == id(b))
print(a is b)
print(a is c)

r = [1, 2, 3]
s = r
s[1] = 23
print(r)
print(s is r)
