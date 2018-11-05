'''
Created on Aug 7, 2018
@author: rajiv
'''


#Local- Inside the current function
#Enclosing- Any and all enclosing functions
#Global- Top-level of the module
#Built-in- Provided by the builtins module

count = 0

def show_count():
    print("c=", count)
    
def set_count(c):    
    # It is required for global scoping so that no new local scope count not generated
    global count 
    count =c
    
    
set_count(5);
show_count();

print(show_count()) #By default any method return None
