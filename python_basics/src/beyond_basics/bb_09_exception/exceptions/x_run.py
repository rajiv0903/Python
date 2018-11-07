'''
Created on Nov 6, 2018

@author: rajiv
'''

from beyond_basics.bb_09_exception.exceptions.handler import main
from beyond_basics.bb_09_exception.exceptions.lookups import lookups
from beyond_basics.bb_09_exception.exceptions.wrapper import wrap, wealth_of_nations
###############################################################################################
print(IndexError.mro())
###############################################################################################
#main();
lookups();
###############################################################################################
print(wrap(wealth_of_nations, 25));