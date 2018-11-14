'''
Created on Nov 4, 2018
@author: rajiv
'''

def safe_root(a, b):
    if a >= 0:
        ans = a**(1/b);
    else:
        if a % 2 == 0:
            ans = "Result is an imaginary number"
        else:
            ans = -(-a)**(1/b)
            
    return ans;

print(safe_root(0, 3));
print(safe_root(2, 3));
print(safe_root(-4, 3));
print(safe_root(-3, 3));