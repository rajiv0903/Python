'''
Created on Aug 7, 2018
@author: rajiv
'''
#Un-ordered collection of unique elements {}

p = {1,2, 3, 4}
print(type(p))

#Empty Dictionary
empty_dict = {}
print(type(empty_dict))

#Empty Set
empty_set = set()
print(type(empty_set))

#Remove Duplicates 
r = [1, 2, 3, 4, 12, 1, 2, 3]
s = set(r)
print(s)

#Iterable but Aritary
for i in s:
    print(i);
    
#Add
s.add(8);
s.add(8); #Same Number
print(s);

s.remove(1);
s.discard(1); #No side effects

from pprint import pprint as pp
pp(s);

#Shallow Copy 
k = s.copy();


#Set - Union, Intersection , Difference
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair= {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn= {'Harry', 'Amelia'}
taste_phc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood= {'Harry'}
ab_blood = {'Joshua', 'Lola'}


print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes));
print('People with Blond Hair or Blue Eyes:', 
      blue_eyes.union(blond_hair));
print('People with Blond Hair but do not have Blue Eyes:',
      blond_hair.difference(blue_eyes));
print('People with Blond Hair or Blue Eyes- But not both:',
      blond_hair.symmetric_difference(blue_eyes));
print('Whether all people smell HCN also have blond hair:',
      smell_hcn.issubset(blond_hair));
print('Whether all people taste ptc can smell hcn:',
      taste_phc.issuperset(smell_hcn));
print('A or B - Never Both:', a_blood.isdisjoint(b_blood));
