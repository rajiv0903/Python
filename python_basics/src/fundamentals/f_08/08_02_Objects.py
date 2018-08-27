'''
Created on Aug 6, 2018
@author: rajiv
'''
'''Pass By Object Reference
    The value of the reference is copied
    not the value of the object
'''
m = [1, 2, 3]

def modify(k):
    k.append(4)
    print("k=", k)
    
modify(m)
print(m)

f = [1, 2, 3]

def replace(g):
    g = [1, 2, 3, 4]
    print("g=", g)

replace(f)
print(f)

def banner(message, border='-'): # Dafault value
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    
banner("Rajiv");
banner("Rajiv", "*");
banner(message="Hello, How r u!", border=":");


def add_spam(menu= None): #Always create immutable object
    if menu is None:
        menu = []
    menu.append("spam");
    return menu;

print(add_spam());
