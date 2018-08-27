'''
Created on Aug 12, 2018

@author: rajiv
'''

import sys


def main(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8');
        for line in f:
            sys.stdout.write(line)
    finally:
        f.close();


# With Block - Context Manager - Close the Resource
def main_context_manager(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        for line in f:
            sys.stdout.write(line)

    
if __name__ == '__main__':
    main(sys.argv[1]);
    print("\n\nWith Context Manager\n--------------------")  
    main_context_manager(sys.argv[1]);

