'''
Created on Aug 21, 2018
@author: rajiv
'''

store = []


def sort_by_last_letter(strings):

    def last_letter(s):
        return s[-1];

    store.append(last_letter);
    print(last_letter)
    return sorted(strings, key=last_letter, reverse=False);


print(sort_by_last_letter(['hello', 'from', 'a', 'local', 'function']));
                           
# Local Function- Are not member of enclosing function
# LEGB Rule:
# Local, Enclosing, Global, Built In

g = 'global';


def outer(p='param'):
    l = 'local';

    def inner():
        print(g, p, l);

    inner();  


outer();


# Returning Function Object
def enclosing():

    def local_func():
        print('local func');

    return local_func;


lf = enclosing();
lf();


# Closures
def ouuter_c():
    x = 2

    def inner_c(y):
        return x + y;  # x is enclosing scope

    return inner_c;


lf_c = ouuter_c();
print(type(lf_c))
print(lf_c.__closure__);
print(lf_c(3))

'''Function Factory'''


def raise_to(exp):

    def raise_to_exp(x):
        return pow(x, exp);

    return raise_to_exp;


square = raise_to(2);
print(square(5));
print(square(9));

cube = raise_to(3);
print(cube(3));



'''global and nonlocal'''
message = 'global'
def enclosing_msg():
    message = 'enclosing'
    def local_msg():
        #global message
        nonlocal message #To modify enclosing message
        message = 'local'
        
    print('enclosing message', message)
    local_msg()
    print('enclosing message', message)

print('global message', message)
enclosing_msg()
print('global message', message)