'''
Created on Nov 7, 2018
@author: rajiv
'''

###############################################################################################
i = 0;
while i > 4:
    print(i);
else: #Condition False
    print('While: Condition False')

i = 8
while i > 4:
    print(i);
    i -= 1;
else: #Condition True - Normal Flow Ended
    print('While: Condition True - Normal Flow Ended')
    
i = 8
while i > 4:
    print(i);
    i -= 1;
    if i == 7:
        break;
else: #Condition True - break
    print('While: Never reach as nobreak') #Never reach as no break
###############################################################################################
for i in [1, 2, 3]:
    print(i)
else:
    print('For: Condition True - Normal Flow Ended')
    
for i in [1, 2, 3]:
    print(i)
    if i == 2:
        break;
else:
    print('For: Condition True - Break Flow Ended')
    
for i in []:
    print(i)
else:
    print('For: Condition  Falsy Flow Ended')
###############################################################################################
try:
    1/2;
except (ValueError, ZeroDivisionError):
    print('Error');
else:
    print('No Error!')
    
try:
    1/0;
except (ValueError, ZeroDivisionError):
    print('Error');
else:
    print('No Error!')
###############################################################################################

###############################################################################################

###############################################################################################

###############################################################################################

###############################################################################################
