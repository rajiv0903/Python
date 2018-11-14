'''
Created on Nov 10, 2018
@author: rajiv
'''

from advance.a_07_class_decorators.class_decorators_01 import Temperature as T1
from advance.a_07_class_decorators.class_decorators_02 import Temperature as T2
from advance.a_07_class_decorators.class_decorators_03 import Temperature as T3
from advance.a_07_class_decorators.class_decorators import Temperature as T
from pprint import pprint
###########################################################################################
# At the time of importing the module decorator take into action and print the metadat
t1 = T1(23);
###########################################################################################
# We cannot initiate the class with negative kelvin temperature 
t2 = T2(2);
#t2 = T2(-1);
pprint(vars(T2))
###########################################################################################
t3 = T3(42)
pprint(vars(T3))
print(t3.celsius)
#t3.celsius = -300
###########################################################################################
t = T(42)
print(t.celsius)
pprint(vars(t))
###########################################################################################

###########################################################################################

###########################################################################################