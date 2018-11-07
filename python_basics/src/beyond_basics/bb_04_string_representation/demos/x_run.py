'''
Created on Nov 5, 2018

@author: rajiv
'''

from beyond_basics.bb_04_string_representation.demos.point import Point2D
from beyond_basics.bb_04_string_representation.demos.table import Table
import reprlib

###############################################################################
p = Point2D(123, 456)
print(str(p))
print('The circle is centered at {}'.format(p))
print('The circle is centered at {}'.format(repr(p)))

points = [Point2D(x, y) for x in range(1000) for y in range(1000)]
print(len(points))
print(reprlib.repr(points))

t = Table(
    ['First Name', 'Last Name'],
    ['Rajiv', 'Mahika', 'Tithi'],
    ['Chauhduri', 'Chaudhuri', 'Bose']
    )
print(str(t))