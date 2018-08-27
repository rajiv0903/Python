'''
Created on Aug 8, 2018
@author: rajiv
'''
import sys
from math import log
import os

#Handling Exception
def convert(s):
    '''Convert to an integer- Do not check Type in advance - It will fail with 
    appropriate error
    '''
    try:
        return int(s);
    except (ValueError, TypeError, OSError) as e:
        print("Conversion Error: {}".format(str(e)), file= sys.stderr)
        #return -1
        #raise
        raise ValueError("Not allowed")
    finally:
        print('Alaways Print.......')

#print(convert("s"));
#print(convert([1, 2, 3]));
#print(convert('3'));


def string_log(s):
    v = convert(s); #Calling the convert method
    return log(v);

print(string_log("2"));
