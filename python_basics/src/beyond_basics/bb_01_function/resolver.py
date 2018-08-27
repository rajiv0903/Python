'''
Created on Aug 20, 2018
@author: rajiv
'''
import socket
from timeit import timeit

'''Function are callable'''

class Resolver:

    def __init__(self):
        self._cache ={}
    #Useful to initiate with value
    def __call__(self, host):
        #Conditional Statement
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host);
        return self._cache[host];
    
    
    def clear(self):
        self._cache.clear();
        
    def has_host(self, host):
        return host in self._cache;
        
resolve = Resolver();
print(resolve('sixty-north.com'));
print(resolve.__call__('sixty-north.com'));
print(resolve._cache)

'''Time It'''
print(
    timeit(setup= "from __main__ import resolve", stmt="resolve('sixty-north.com')",  number=1)
    );