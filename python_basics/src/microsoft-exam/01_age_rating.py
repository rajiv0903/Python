'''
Created on Nov 4, 2018
@author: rajiv
'''

def get_rating(age):
    rating = "";
    
    if age == None:
        rating = 'C'
    elif age < 13:
        rating = 'C'
    elif age <18:
        rating = 'T'
    else:
        rating = 'A'
        
    return rating;

while True:
    print("====================");
    age = input("Enter Age:\n");
    print(get_rating(int(age)));
    
    
    
    