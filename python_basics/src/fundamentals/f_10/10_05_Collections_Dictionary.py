'''
Created on Aug 7, 2018
@author: rajiv
'''

#Unordered Mapping from unique immutable keys to mutable values

urls = {'Google':'https://www.google.com/',
        'Microsoft':'https://www.microsoft.com/',
        'Verizon':'https://www.verizonwireless.com',
        'Comcast':'https://comcast.com/',
        'TMObile':'https://comcast.com/'
        }

print(urls['Google']);
print(urls['TMObile']);

#Constructor- Tuples
name_and_ages = [('Rajiv', 33), ('Tithi', 28), ('Bubai', 34)]
d = dict(name_and_ages);
print(d);
print(d['Bubai']);

#Copy
colors = dict(red=1, blue=2, green=3);
print(colors)
color_copy = colors.copy();
print(color_copy)
color_copy_1 = dict(color_copy)
print(color_copy_1);

#Iteration
for key in colors:
    print("{key}={value}".format(key= key, value=colors[key]));

print(colors.values());
print(colors.keys());

l = list(colors.keys());
print(l)

#Presence Test
print('red' in colors);

#Extending List
m = {'H': [1, 2, 3],
     'J': [1, 2, 3, 4]}

m['H'] += [2,3]
print(m)

#Pretty Printing
from pprint import  pprint as pp
pp(m)




