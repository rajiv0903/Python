'''
Created on Aug 26, 2018
@author: rajiv
'''

print('#################### Single Inheritance #########################');
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
    
sl = SortedList([4, 3, 78, 11]);
print(sl)
sl.add(-42)
print(sl)

print('#################### Multiple Inheritance #########################');
print(isinstance(3, int))
print(isinstance('Hello', str))
print(isinstance((2,3), tuple))
print(isinstance((2,3), bytes))
print(isinstance(sl, SortedList))
print(isinstance(sl, SimpleList))

#Tuple Type Check
x = []
print(isinstance(x, (float, dict, list)));

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
                     
il = IntList([1, 2, 3, 4]);
print(il)
#il.add('2');

print(issubclass(IntList, SimpleList))
print(issubclass(SortedList, SimpleList))
print(issubclass(SortedList, IntList))