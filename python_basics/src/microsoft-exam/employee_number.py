'''
Created on Nov 4, 2018

@author: rajiv
'''

e_num = "sentinel"
parts = ""

while e_num !="":
    valid = False;
    
    e_num = input("Enter number");
    parts = e_num.split("-");
    
    if len(parts) == 3:
        if len(parts[0]) == 3 and  len(parts[1]) == 2 and len(parts[2]) == 4:
            if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                valid = True;
                
    print(valid);
    