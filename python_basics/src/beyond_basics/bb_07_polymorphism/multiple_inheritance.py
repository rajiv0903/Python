'''
Created on Aug 26, 2018
@author: rajiv
'''
from test.test_datetime import all_test_classes
from test._test_multiprocessing import initializer
from test.test_sys_settrace import called

print('#################### Multiple Inheritance #########################');
#Well define Method resolution order
class SimpleList:
    
    def __init__(self, items):
        self._items = list(items);
   
    def add(self, item):
        self._items.append(item)
        
    def __getitem__(self, index):
        return self._items.get(index);
    
    def sort(self):
        self._items.sort();
    
    def __len__(self):
        return len(self._items);
    
    def __repr__(self):
        return "SimpleList{!r}".format(self._items)
    
class SortedList(SimpleList):
    
    def __init__(self, items=()):
        super().__init__(items);
        self.sort();
        
    def add(self, item):
        super().add(item);
        self.sort();
        
    def __repr__(self):
        return "SortedList{!r}".format(self._items)

#Define Int List
class IntList(SimpleList):
    
    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise ValueError("IntList supports only integer values!");
    
    def __init__(self, items=()):
        for item in items:
            self._validate(item);
        super().__init__(items);
   
    def add(self, item):
        self._validate(item);
        super().add(item)
    
    def __repr__(self):
        return "IntList{!r}".format(self._items)
                     
class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList{!r}".format(self._items)
    
sil = SortedIntList([1,2, 11, 3]);
print(sil)
sil.add(-2); #which add to call - MRO
print(sil);

#Rules:
'''
If a class 
    1. has multiple base class
    2. no initializer
 - Only the initializer of first base class will be called
'''

print(SortedIntList.__mro__)
print(SortedIntList.mro())