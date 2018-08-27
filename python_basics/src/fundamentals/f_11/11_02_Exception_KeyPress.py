'''
Created on Aug 8, 2018
@author: rajiv
'''

try:
    import msvcrt
    def getkey():
        """ Wait for a key press and return a single character string """ 
        return msvcrt.getch()
    
except ImportError:
    import sys
    from sys import stdin
    import tty
    import termios
    
    def getkey():
        fd = sys.stdin.fileno()
        original_attributes =   termios.tcgetattr(fd)  
        try:
            tty.setraw(sys, stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr( fd, termios.TCSADRAIN, original_attributes)
        return ch

