'''
Created on Nov 5, 2018

@author: rajiv
'''

from beyond_basics.bb_06_iterable_iteration.demos.tracer import Trace
from beyond_basics.bb_06_iterable_iteration.demos.map_reduce import combine_counts, counts
from _functools import reduce
from beyond_basics.bb_06_iterable_iteration.demos.example_iterator import ExampleIterator, ExampleIterable
from beyond_basics.bb_06_iterable_iteration.demos.alt_iterable import AlternateIterable
#########################################################################################
result = map(Trace() (ord), 'The quick brown fox jumps over the lazy dog')

print(next(result))
print(next(result))
#########################################################################################
total_counts = reduce(combine_counts, counts)
print(total_counts)

#########################################################################################
i = ExampleIterator([1, 2])
print(next(i))
print(next(i))

for i in ExampleIterable():
    print(i)
#########################################################################################
print([i  for i in AlternateIterable()])