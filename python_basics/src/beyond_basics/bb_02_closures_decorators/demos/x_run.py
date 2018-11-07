'''
Created on Nov 5, 2018

@author: rajiv
'''

from beyond_basics.bb_02_closures_decorators.demos.sort_by_last_letter import sort_by_last_letter
from beyond_basics.bb_02_closures_decorators.demos.raise_to import raise_to
from beyond_basics.bb_02_closures_decorators.demos.make_timer import make_timer
from beyond_basics.bb_02_closures_decorators.demos.escape_unicode import northern_city
from beyond_basics.bb_02_closures_decorators.demos.call_count import hello
from beyond_basics.bb_02_closures_decorators.demos.tracer import rotate_list
from beyond_basics.bb_02_closures_decorators.demos.island_maker import IslandMaker, norwegian_island_maker, tracer
from beyond_basics.bb_02_closures_decorators.demos.create_list import create_list
##########################################################################################
print(sort_by_last_letter(['Rajiv', 'Tithi', 'Mahika', 'A']))
print(sort_by_last_letter(['Rajiv', 'Tithi', 'Mahika', 'A']))
##########################################################################################
square = raise_to(2)
cube = raise_to(3)
print(square.__closure__)
print(cube.__closure__)
print(square(3))
print(cube(3))
##########################################################################################
t = make_timer();
print(t())
print(t())
print(t())
##########################################################################################
print(northern_city())
##########################################################################################
hello('name')
hello('name')
hello('name')
print(hello.count)
##########################################################################################
print(rotate_list([1, 2, 3, 4, 5]))
##########################################################################################
print(norwegian_island_maker('Ra'))
tracer.enabled = False
print(norwegian_island_maker('Ra'))
im = IslandMaker(' Island')
print(im.make_island('Python'))
tracer.enabled = True
print(im.make_island('Python'))
##########################################################################################
print(create_list(2, 5))