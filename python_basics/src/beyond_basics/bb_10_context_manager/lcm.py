'''
Created on Oct 30, 2018
@author: rajiv
'''
class LoggingContextManager:
    def __enter__(self):
        return 'Hello, Rajiv!';
    
    def __exit__(self, exc_type, exc_val, ext_tb):
        return;
        #return false - no exception propagated
    

with LoggingContextManager() as x:
    print(x)