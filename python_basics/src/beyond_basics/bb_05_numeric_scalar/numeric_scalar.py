'''
Created on Aug 26, 2018
@author: rajiv
'''

# Large number in int 

from math import factorial as fact
import sys
import decimal
from decimal import Decimal
from pprint import pprint as pp
from fractions import Fraction
import cmath
from builtins import round, str
import datetime
from calendar import week

x = fact(1000);
print('######### Int ##################');
print(x);

# 64 bit float - 1 for sign, 11 for exponent and remaining 52 for fraction
# 15 to 17 decimal precision 
print('######### Float ##################');
print (sys.float_info);
print(sys.float_info.max);  # 1.7976931348623157e+308
print(sys.float_info.min);  # 2.2250738585072014e-308
print (pow(2, 53));  # 9007199254740992
print(float(0.8 - 0.7));  # 0.10000000000000009

# Decimal is used in financial institute
print('######### Decimal ##################');
pp(decimal.getcontext());
print(Decimal(7))
print(Decimal(0.8) - Decimal (0.7))
print(Decimal('0.8') - Decimal ('0.7'))
print(Decimal('NaN') - Decimal ('0.7'))

print('######### Fraction ##################');
two_third = Fraction(2, 3);
pp(two_third);
four_fifths = Fraction(4, 5);
pp(four_fifths);
# Fraction (4, 0); #Error
print(Fraction(0.5));
print(Fraction(Decimal('0.1')));
print(Fraction(2, 3) / Fraction (4, 5));

print('######### Complex ##################');
print(3 + 4j)
print(complex(3));
print(complex(-2, 3))
# cmath can return imaginary results 
print(cmath.sqrt(-1));
print(cmath.phase(1 + 1j))

print('######### Built-In ##################');
print(abs(-5), abs(5.0), abs(complex(0, -5)));
print(round(0.2812, 3), round(0.625, 1), round(Decimal('2.675'), 2));

print('######### Number Base Conversion ##################');
print(bin(42), oct(42), hex(42));

print('######### Date Time ##################');
datetime.date(2014, 1, 6);
td = datetime.date.today();
print(td.year, td.month, td.day);
print(td.weekday(), td.isoweekday());
print(td.strftime('%A %d %B %Y'));

pp(datetime.time(hour=23, minute=59, second=59, microsecond=999999));

print('######### Time Delta ##################');
td = datetime.timedelta(weeks =1, minutes= 2, milliseconds= 5500);
print(str(td))




