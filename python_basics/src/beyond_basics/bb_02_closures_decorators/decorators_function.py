'''
Created on Aug 21, 2018
@author: rajiv
'''
import functools

'''Decorators-
Replace, Enhance and modify exiting functions
Does not change the original function
calling code does not need to change
'''


def escape_unicode(f):

    def wrap(*args, **kwargs):
        x = f(*args, **kwargs);
        return ascii(x);

    return wrap;


@escape_unicode
def norther_city():
    return "Thomas"


print(norther_city())

'''Class Decorator'''


class CallCount:

    def __init__(self, f):  # It takes a function
        self.f = f;
        self.count = 0;
    
    def __call__(self, *args, **kwargs):
        self.count += 1;  # Increment each time is being called
        return self.f(*args, **kwargs);


@CallCount    
def hello(name):
    print("Hello {}".format(name));


print(hello('Rajiv'))
print(hello('Rajiv'))
print(hello('Rajiv'))
print(hello.count)

'''Instance Decorator'''


class Trace:

    def __init__(self):
        self.enabled = True;
        
    def __call__(self, f):

        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f));
            return f(*args, **kwargs);

        return wrap;

    
tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


l = [1, 2, 3]
l = rotate_list(l);
l = rotate_list(l);
l = rotate_list(l);

'''Multiple Decorators'''


@tracer
@escape_unicode
def norwegian_maker(name):
    return name + "'";


print(norwegian_maker('Rajiv'));
print(norwegian_maker('Rajiv'));

'''With Decorator we lose the information- If we decorate then we will lose the actual 
name and doc information to prevent we need to use noop_wrapper'''


def noop(f):

    @functools.wraps(f)
    def noop_wrapper(*args, **kwargs):
        return f(*args, **kwargs);
    
    # It is ugly - as we cannot maintain all attributes
    # noop_wrapper.__name__ = f.__name__;
    # noop_wrapper.__doc__ = f.__doc__;
    return noop_wrapper;

        
def hello_world():
    "Print a well known message"
    print('Hello', ' World!')

    
print(hello_world.__name__)
print(hello_world.__doc__)

'''Useful - Validating function arguments'''


def non_negative(index):

    def validator(f):

        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must be non-negative'.format(index));
            return f(*args);

        return wrap;

    return validator;


@non_negative(1)
def create_list(value, size):
    return [value] * size


print(create_list('a', 3))
print(create_list('a', -1))
