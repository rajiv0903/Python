'''
Created on Aug 12, 2018

@author: rajiv
'''

from contextlib import closing

class RefrigeratorRider:
    
    def open(self):
        print('Open fridge door')
    
    def take(self, food):
        print('Finding.....{}'.format(food))
        
        if (food == 'pizza'):
            raise RuntimeError('Health Warning!')
        
        print('Taking...{}'.format(food))
        
    def close(self):
        print('Closed fridge door')
        
def raid(food):
    with closing(RefrigeratorRider()) as r:
        r.open();
        r.take(food);
        #r.close();
        
raid ('Banana');
raid ('pizza'); 