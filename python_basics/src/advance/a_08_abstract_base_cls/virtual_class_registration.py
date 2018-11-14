'''
Created on Nov 9, 2018
@author: rajiv
'''
from abc import ABCMeta

class Text(metaclass=ABCMeta):
    pass;

Text.register(str);

@Text.register
class Prose:
    pass;
    
