'''
Created on Aug 26, 2018
@author: rajiv
'''
import reprlib


class Point2D:
    
    def __init__(self, x, y):
        self._x = x;
        self._y = y;
        
    def __str__(self):
        return '({}, {})'.format(self._x, self._y);
    
    # Should return the type of the object along with properties
    def __repr__(self):
        return "Point2D(x= {}, y={})".format(self._x, self._y);
    
    def __format__(self, f):
        # return 'Formated point: {} {} {}]'.format(self._x, self._y, f);
        if f == 'r':
            return '{}, {}'.format(self._y, self._x);
        else:
            return '{}, {}'.format(self._x, self._y);
    

p = Point2D(2, 3);
print(str(p));
print(p);  # Default str
print(repr(p));

# repr
l = [Point2D(i, i * 2) for i in range(3)];
print(str(l))
print(repr(l))

# Format
print('{:r}'.format(Point2D(4, 5)))

# reprlib- drop in replacement of built in repr
points = [Point2D(x, y) for x in range(1000) for y in range(1000)];
print(reprlib.repr(points))

# ascii | ord - Charcater to Uinocde Codepoint | chr - Opposite of ord
print(ord('3'));
print(chr(190));
