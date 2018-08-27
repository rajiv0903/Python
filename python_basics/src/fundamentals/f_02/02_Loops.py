'''
Created on Aug 6, 2018
@author: rajiv
'''

# While loops
c = 5 
while c != 0: # Explicit
    print(c)
    c -= 1 # c= c-1

c1 = 5
while c1 : #c1 = 0 means false (Implicit)
    print(c1)
    c1 -= 1 # c1= c1-1
    
while False:
    print("Logging!")
    
while True:
    response = input() #Built in function to take use input 
    if int(response) % 7 == 0:
        print("Got it!!")
        break
    
