'''
Created on Nov 8, 2018
@author: rajiv
'''
import sys
from pprint import pprint
from advance.a_03_custom_attr.vector.vector_01 import Vector as V1
from advance.a_03_custom_attr.vector.vector_02 import Vector as V2
from advance.a_03_custom_attr.vector.vector_03 import Vector as V3
from advance.a_03_custom_attr.vector.vector_04 import Vector as V4
from advance.a_03_custom_attr.vector.vector_05 import Vector as V5
from advance.a_03_custom_attr.vector.vector_06 import Vector as V6
from advance.a_03_custom_attr.vector.vector_09 import ColoredVector
from advance.a_03_custom_attr.vector.logging_proxy import LoggingProxy
from advance.a_03_custom_attr.resistor.resistor import Resistor
############################################################################################
v1 = V1(5, 3);
# Direct Access of __dict__
print(v1)
pprint(dir(v1))
print(v1.__dict__)
print(v1.__dict__['x'])
v1.__dict__['x'] = 17
print(v1)
# del v1.__dict__['x']
print('x' in v1.__dict__)
v1.__dict__['z'] = 3

# We should use
print(getattr(v1, 'x'))
print(hasattr(v1, 'x'))
print(setattr(v1, 'x', 9))
print(delattr(v1, 'x'))
############################################################################################
v2 = V2(p=5, q=9)
print(v2)
pprint(dir(v2))  # Attributes are now public 
############################################################################################
# Making it private i.e. _<name>
v3 = V3(p=9, q=3)
print(v3)
pprint(dir(v3))
############################################################################################
# Invoked over written __getattr__
v4 = V4(p=3, q=9);
print(v4.p)
############################################################################################
# Still we can set an attribute
v5 = V5(p=1, q=2)
print(v5.p)
v5.x = 5
############################################################################################
v6 = V6(p=2, q=3)
print(v6)
# v6.p= 11 we cannot set attribute
############################################################################################
cv = ColoredVector(red=23, green=45, blue=234, p=1, q=4);
print(cv.red)
print(cv)
pprint(dir(cv))

############################################################################################
cv2 = ColoredVector(red=23, green=45, blue=234, p=1, q=4);
cw = LoggingProxy(cv2)
print(cw.p)
cw.red = 231
print(cw.red)
############################################################################################
r = Resistor(10, 5, 0.25)
print(sys.getsizeof(r))
############################################################################################
