'''
Created on Aug 7, 2018
@author: rajiv
'''
#Length
print(len('rajiv'));

#Concatenation
s  = "New"
s += "Found"
print(s);

#Join
colors = ';'.join(['#45ff33', '#1298a3'])
print(colors)

#Split to List
colors = colors.split(';')
print(colors)

#Partition return tuple
print("unforgetable".partition("forget"));
departure, seperator, arrival = "London:USA".partition(":")
print(departure); print(seperator); print(arrival);

#Format
f = "The age of {0} is {1}".format("Rajiv", 33);
print(f)

f = "Current position {latitude} {longitude}".format(latitude="60N", longitude="5E");
print(f)

import math
print("Math constants: pi {m.pi}, e={m.e:.3f}".format(m=math))
