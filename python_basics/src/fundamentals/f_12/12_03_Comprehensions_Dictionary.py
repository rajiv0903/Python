'''
Created on Aug 8, 2018
@author: rajiv
'''
'''
    General Formula:
    [key_expr:value_expr for item in iterable]
    
'''
from pprint import pprint as pp

country_to_capital = {'UK':'London',
                      'Brazil': 'Brazilia'}


capital_to_country = {capital: country for country, capital in country_to_capital.items()}

pp(capital_to_country)

#List
words = ['hotel', 'flight']
#Dictionary 
print ( {x[0]:x for x in words} )