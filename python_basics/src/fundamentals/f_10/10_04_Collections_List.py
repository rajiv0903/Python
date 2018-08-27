'''
Created on Aug 7, 2018
@author: rajiv
'''
from builtins import len

#Zero Based Index
s= "show how to index into sequences".split();
print(s); print(s[4]);

#Negative Based Index
print(s[-1]);

#Slicing - Starts with 0
print(s[1:4]); print(s[1:-1]);
print(s[3:]);
print(s[:3]);

# Immutability
full_slice = s[:]
print(full_slice is s); 
print(full_slice == s);

#Copy- Shallow - New List Got Created
u = s.copy()
v = list(s);
print(u); print(v);

#List Repetition in Shallow
c = [1, 2]
d = c * 3
print(d)

k = [[-1, +1]] * 5
print(k)
k[1].append(7);
print(k); #All elements added as all of them pointing to same list

#Finding elements
w = "the quick brown fox jumps over the lazy dod".split();
i = w.index("fox");
print(i); print(w.count("the")); 
del w [0]; #Delete by index
print(w);
w.insert(0, "the"); #Insert by Index
print(w);

#Reversing and Sorting In Place
g = [1, 2, 3, 4, 5]
print(g)
g.reverse(); print(g)
g.sort(); print(g);
g.sort(reverse=True); print(g);

#Sorting In Place - Key - Callable Object Ex. Len
h = "the quick brown fox jumps over the lazy dod".split();
h.sort(key=len, reverse=False);
print(h);
print(' '.join(h))

