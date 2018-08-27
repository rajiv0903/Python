'''
Created on Aug 6, 2018
@author: rajiv
'''
#List are mutable
a = [1, 2, 3]
print(a)

b = ["apple", "banana", "pears"]
print(b)

b[1] = 2 #Heterogeneous 
print(b)

c = []
c.append(1)
print(c)
c.append("apple")
print(c)

#List Constructor 
d = list("characters")
print(d)

#Dictionary - Mutable mappings of keys to values
dictObj = {'rajiv': '201-647-9356', 'tithi': '7868062788'}
print(dictObj['rajiv'])
dictObj['rajiv'] ='changed'
print(dictObj['rajiv'])