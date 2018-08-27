'''
Created on Aug 7, 2018
@author: rajiv
'''
from builtins import min

t = ("Norway", 4.953, 3)
print(t)
print(t[0]) #Access by zero based index
print(len(t)) #Number of elements

#Iterate
for item in t:
    print(item)
    
t+ (4.0, 26e9)
print(t)

#Multiple
t = t * 2
print(t)

#Nested Tuple
a= ((1, 2), (3, 4))
print(a[1]) ; print(a[1][0])

#For single element tuple use ,
k = (9,) # We need this , because it can understand it is tuple
print(type(k))

#Empty tuple
e = ()
print(type(e))

#Find Min and Max
def minmax(items):
    return min(items) , max(items)

lower , upper = minmax([24, 5, 6, 7, 9, 10]) #Unpack
print(lower); print(upper)

#Arbitrary nested tuples
(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a); print(b); print(c); print(d)

#tuple constructor
l = tuple([1, 2, 3]);
s = tuple('rajiv');
print(l); print(s);

#In Operator
print ( 5 in (3, 4, 5));
print ( 5 not in (3, 4, 5));
