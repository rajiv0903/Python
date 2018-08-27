'''
Created on Aug 26, 2018
@author: rajiv
'''
from _queue import Empty

# Multi-Input comprehension
print('################# Multi-Input comprehension #########################');
l = [(x, y) for x in range(3) for y in range(2)]
print(l);

values = [x / (x - y) 
          for x in range(100) 
          if x > 50 
          for y in range(50) 
          if x - y != 0] ;
print(values);

print('#################### Nested comprehension #########################');
vals = [ [y * 3 for y in range(x)] for x in range(10) ];
print(vals);

print('#################### Map Function- Lazy #########################');
map(ord, 'The quick brown fox');
for o in map(ord, 'The quick brown fox'):
    print(o) ;
    
sizes = ['small', 'medium', 'large'];
colors = ['lavender', 'teal', 'burnt orange'];
animals = ['koala', 'platypus', 'salamander'];


def combine (size, color, animal):
    return '{} {} {}'.format(size, color, animal);


print(list(map(combine, sizes, colors, animals)));

print('#################### Filter Function- Lazy #########################');
positives = filter(lambda x: x > 0, [1, -1, 2, 3, -5, 6])
print(list(positives))

print('#################### Reduce #########################');
from functools import reduce
import operator

print(reduce(operator.add, [1, 2, 3, 4, 5], 0))


def count_words(docs):
    doc = ''.join(c.lower() if c.isalpha() else ' ' for c in docs);
    
    frequencies = {};
    for word in doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1;
        
    return frequencies;


def combine_counts(d1, d2):
    d = d1.copy();
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count;
    return d;


documents = [
    'it was the best time, It was the worst time',
    'I do not like green eggs'
    'I do like apple eggs'
    ]

counts = map(count_words, documents);
total_counts = reduce(combine_counts, counts);

print (total_counts);

print('#################### Iterable #########################');


class ExampleIterator:

    def __init__(self, data=None):
        self._index = 0;
        self._data = data if data is not None else [2, 3, 4]; 

    def __iter__(self):
        return self;

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration();
        rslt = self._data[self._index];
        self._index += 1;
        return rslt;


class ExampleIterable:

    def __init__(self):
        self._data = [1, 2, 3];

    def __iter__(self):
        return ExampleIterator(self._data);

    
class AlternateIterable:

    def __init__(self):
        self._data = [1, 2, 3];

    def __getitem__(self, idx):  # Overriding get item
        return self._data[idx];


i = ExampleIterator();
print(next(i), next(i), next(i));
for i in ExampleIterable():
    print(i)
l = [i for i in AlternateIterable()]
print(l)
