'''
Created on Aug 12, 2018
@author: rajiv
'''


import sys

#Default Encoding
print(sys.getdefaultencoding())

#Writing text to file
f = open('wasteland.txt', mode='wt',  encoding='utf-8');
f.write('what are the roots that clutch, ');
f.write('what branches grow\n');
f.write('Out of this stony rubbish? ');
f.close();


g= open('wasteland.txt', mode='rt',  encoding='utf-8');
print(g.read(32)); #In text mode it is number of character 
print(g.read()); #Read rest
print(g.read()); #Read rest
print(g.seek(0)); #Seek to begining
print(g.readline()); #Read line
print(g.readline()); #Read line
print(g.readline()); #Read line
print(g.seek(0)); #Seek to begining
print(g.readlines()); #Read all lines
g.close();




