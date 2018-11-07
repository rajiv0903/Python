'''
Created on Nov 5, 2018
@author: rajiv
'''

from beyond_basics.bb_07_polymorphism.demos.base import Base, Sub
from beyond_basics.bb_07_polymorphism.demos.sorted_list import  IntList, SortedList, SortedIntList
from beyond_basics.bb_07_polymorphism.demos.diamond import D
############################################################################################
b = Base();
b.f();

s = Sub();
s.f();
############################################################################################

sl = SortedList([4, 3, 78, 11])
print(sl)
sl.add(-3)
print(sl)

il = IntList([1, 2, 3, 4])
print(il)

sil = SortedIntList([4, 3, 78, 9]); 
print(sil) #Getting Sorted List Behavior
sil.add(1); #Getting Int List Behavior - MRO
print(sil)
#sil.add('-1')

print(SortedIntList.__bases__)
print(IntList.__bases__)

'''
Method Resolution Order
C3 algorithm - 
Subclass come before base class
Base class order from class definition is preserved
First two maintained no matter where you start in inheritance graph
'''
print(SortedIntList.__mro__)
print(SortedIntList.mro())
############################################################################################
print(D.mro())
d = D()
print(d.func());