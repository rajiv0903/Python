'''
Created on Aug 26, 2018
@author: rajiv
'''


def sign (x):
#     if x < 0:
#         return -1;
#     elif x > 0:
#         return 1;
#     return 0;
    return (x > 0) - (x < 0);

'''print(False - False);  # 0
print(False - True);  # -1
print(True - False);  # 1
print(True - True);  # 0'''


def orientation(p, q, r):
    d = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]);
    return sign(d);


a = (0, 0);
b = (4, 0);
c = (4, 3);
d = (8, 6);

print(orientation(a, b, c))
print(orientation(a, c, b))
print(orientation(a, c, d))
    
