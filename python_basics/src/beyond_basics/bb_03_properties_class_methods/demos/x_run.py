'''
Created on Nov 5, 2018

@author: rajiv
'''

from beyond_basics.bb_03_properties_class_methods.demos.shipping import RefrigeratedShippingContainer, HeatedRefrigeratedShippingContainer

r1 = RefrigeratedShippingContainer.create_with_items('ESC', length_ft=40, items=['apple','guava'], celsius=-18.0)
print(r1.contents)

h1 = HeatedRefrigeratedShippingContainer.create_empty('YML', length_ft=40, celsius=-18.0);
print(h1)
#h1.celsius = -21.0