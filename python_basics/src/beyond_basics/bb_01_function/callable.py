'''
Created on Aug 20, 2018

@author: rajiv
'''

'''Use built in callable'''

def is_even(x):
    return x %2 == 0;

'''regular function is callable'''
print(callable(is_even));

'''lambda is callable'''
is_odd = lambda x: x % 2==1;
print(callable(is_odd));

'''class and method are callable'''
print(callable(list))
print(callable(list.append))

'''Instance Object can be made callable using __call__ method'''
class CallMe:
    #pass
    def __call__(self):
        print('Called!')
        
call_me = CallMe();
print(callable(call_me))

'''String instances are not callable'''
print ( callable('This is string'))