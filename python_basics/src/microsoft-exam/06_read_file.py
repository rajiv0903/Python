'''
Created on Nov 11, 2018

@author: rajiv
'''
import os

def read_file(file):
    line = None
    if os.path.isfile(file):
        data = open(file, 'r')
        while line != '':
            line = data.readline()
            print(line)
    
read_file('x_text.txt');