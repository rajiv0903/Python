'''
Created on Nov 11, 2018

@author: rajiv
'''

distance= int(input('Enter distance in feet'))
d_miles = distance/5280

time = int(input('Enter time in seconds'))
time_h = time/3600

velocity = d_miles/time_h

print('the avg velocity', velocity, ' miles/hour')