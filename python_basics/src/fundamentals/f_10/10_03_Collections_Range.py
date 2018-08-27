'''
Created on Aug 7, 2018
@author: rajiv
'''
#Range is used as stop value
for i in range(5):
    print(i)

#Construct a list
l = list(range(5, 10))
print(l)

#Step Argument
l = list(range(10, 20, 2))
print(l)

#Enumerate
t = [1, 2, 3, 4]

for i in enumerate(t):
    print(i)
    
for i, v in enumerate(t):
    print("i={}, v={}".format(i, v))