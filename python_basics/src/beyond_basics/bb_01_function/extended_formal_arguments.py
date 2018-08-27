'''
Created on Aug 20, 2018
@author: rajiv
'''

print("one")
print("one", "two", "three")
print("{a}<===>{b}".format(a="Rajiv", b="Tithi"));

'''Determine area or volume
Arguments'''


def hypervolume1(*lengths):
    print(lengths);
    print(type(lengths))
    
    i = iter(lengths);
    v = next(i)
    for length in i:
        v = v * length;
    return v;


print(hypervolume1(3, 4))
print(hypervolume1(3, 4, 5))
print(hypervolume1(1))

'''Argument + Arguments'''


def hypervolume2(length, *lengths):
    i = iter(lengths);
    v = length
    for length in i:
        v = v * length;
    return v;


print(hypervolume2(1))

'''Argument + Keyword Arguments'''


def tag(name, **attributes):
    result = "<" + name;
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += "/>"
    return result;


print(tag('img', src="image.png", alt="My Image"))

'''Define positional argument then keyword arguments'''


def print_args1(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1); print(arg2); print(args);
    print(kwarg1); print(kwarg2); print(kwargs)


print_args1(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwargs3=8, kwargs4=9);


def print_args2(arg1, arg2, *args):
    print(arg1); print(arg2); print(args);

    
t = (11, 12, 13, 14);
print_args2(*t);

'''Keyword Arguments- Argument name has to match'''


def print_keywo_args1(r, g, **kargs):
    print("r=", r); print("g=", g); print(kargs);

    
k = {'r': 20, 'g':12, 'b':13, 'alpha':52};
print_keywo_args1(**k)

'''Daily Temperature'''
sunday = [21, 22, 34, 56]
monday = [21, 22, 34, 56]
tuesday = [24, 22, 34, 56, 57]

for item in zip(sunday, monday, tuesday):
    print(item)
    
daily = [sunday, monday, tuesday]
for item in zip(*daily):
    print(item)

