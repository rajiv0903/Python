'''
Created on Aug 8, 2018
@author: rajiv
'''

from pprint import pprint as pp
from beyond_basics.bb_01_function.airtravel import make_flight, make_flights
from beyond_basics.bb_01_function.resolver import Resolver
from timeit import timeit

f = make_flight();
pp(f._aircraft.seating_plan());
pp(f._seating);
print(list(range(1, 3)));

e, g = make_flights();
print(e.num_available_seats())
print(g.num_available_seats())
print(e._aircraft.num_seats())

# Callable      
resolve = Resolver();
#Because we implemented callable hence we can pass argument in the reference
print(resolve('sixty-north.com'));
print(resolve.__call__('sixty-north.com'));
print(resolve._cache)

'''Time It'''
print(timeit(setup="from __main__ import resolve", 
             stmt="resolve('sixty-north.com')", 
             number=1)
    );
print(timeit(setup="from __main__ import resolve", 
             stmt="resolve('sixty-north.com')", 
             number=1)
    );
