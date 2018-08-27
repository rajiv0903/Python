'''
Created on Aug 20, 2018

@author: rajiv
'''

scientists =['Marie Curie', 'Albert Einstein', 'Niels Bhor']

'''lambda'''
print(
    sorted(scientists, key=lambda name: name.split()[-1], reverse=False)
    );