'''
Created on Aug 8, 2018
@author: rajiv
'''

from pprint import pprint as pp
from beyond_basics.bb_01_function.airtravel import make_flight, make_flights


# f = Flight('SN9888')
#  
# print(type(Flight))
# print(type(f))
# print(f.number())
#print(Flight.number(f))


# a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6);
# f = Flight('SN9888', a)
# 
# print(a.model())
# print(a.registration())
# print(a.seating_plan())
# print(f.aircraft_model())
# pp (f._seating)
# 
# f.allocate_seat("21F", "Rajiv")
# f.allocate_seat("22F", "Rajiv")
# f.allocate_seat("1F", "Rajiv")
# pp (f._seating)

f = make_flight();
pp(f._aircraft.seating_plan());
pp(f._seating);
print(list(range(1, 3)));

e, g = make_flights();
print(e.num_available_seats())
print(g.num_available_seats())
print(e._aircraft.num_seats())
