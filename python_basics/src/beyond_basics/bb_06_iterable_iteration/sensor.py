'''
Created on Aug 26, 2018
@author: rajiv
'''
import random
import datetime
import itertools
import time

class Sensor:
    def __iter__(self):
        return self;
    
    def __next__(self):
        return random.random();

sensor = Sensor();
timestamps = iter(datetime.datetime.now, None); # Never Stop Iteration


for stamp, value in itertools.islice(zip(timestamps, sensor), 10):
    print(stamp, value);
    time.sleep(1)

