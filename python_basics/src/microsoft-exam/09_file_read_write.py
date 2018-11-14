'''
Created on Nov 11, 2018

@author: rajiv
'''

import sys

try:
    file_in = open('x_in.txt', 'r')
    file_out = open('x_out.txt', 'w+')
except IOError:
    print('cannot open', file_name)
else:
    i = 1
    for line in file_in:
        print(line.strip())
        file_out.write('line'+str(i)+':'+line)
        i = i +1
    file_in.close();
    file_out.close();
    