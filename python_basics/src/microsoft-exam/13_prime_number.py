'''
Created on Nov 11, 2018

@author: rajiv
'''

p=2
while p <=10:
    is_prime = True
    p = p +1
    for i in range(2, p):
        if p % 2 == 0:
            is_prime = False
    if is_prime == True:
        print(p)
        continue