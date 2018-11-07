'''
Created on Nov 7, 2018
@author: rajiv
'''

from beyond_basics.bb_10_context_manager.simple_example import logging_context_manager
from beyond_basics.bb_10_context_manager.nested import nest_test
from beyond_basics.bb_10_context_manager.propagate import propagater
from beyond_basics.bb_10_context_manager.db.connection import Connection
from beyond_basics.bb_10_context_manager.db.transaction import Transaction
from beyond_basics.bb_10_context_manager.xact import start_transaction, Connection as Conn
#############################################################################################
with logging_context_manager() as x:
    print(x)
#############################################################################################
with logging_context_manager() as x:  # It suppress the error 
    pass
    # raise ValueError('Something went wrong!')
#############################################################################################
# Mutiple Context Manager
with nest_test('outer') as n1, nest_test('inner nested in ' + n1):
    pass
#############################################################################################
# Mutiple Context Manager
with propagater('outer', True) as x, propagater('inner', False) as y:
    raise TypeError('Cannot convert lead into gold')
#############################################################################################
# Without Context Manager
conn = Connection()
xact = Transaction(conn)
xact.commit();
#############################################################################################
# With Context Manager
conn1 = Conn();
try:
    with start_transaction(conn1) as tx:
        x = 1 + 1
        raise ValueError()
        y = x + 2
        print('transaction 0=', x, y)
except ValueError:
    print('Oops! Transaction 0 failed!')

try:
    with start_transaction(conn1) as tx:
        x = 1 + 1
        y = x + 2
        print('transaction 1=', x, y)
except ValueError:
    print('Oops! Transaction 0 failed!')
#############################################################################################
