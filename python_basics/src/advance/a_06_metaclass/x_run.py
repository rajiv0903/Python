'''
Created on Nov 8, 2018
@author: rajiv
'''
from pprint import pprint
from advance.a_06_metaclass.tracing import TracingMeta
from advance.a_06_metaclass.entries import EntriesMeta
from advance.a_06_metaclass.keywordmeta import ConstrainedToKeywords
from advance.a_06_metaclass.metainheritance import D, C
###########################################################################################
print(type(type))


###########################################################################################
class Widget:
    pass


w = Widget()
print(type(w))
print(type(Widget))
pprint(dir(Widget))


###########################################################################################
class WidgetWithMeta(metaclass=TracingMeta):

    def action(self, message):
        print(message)

    the_answer = 42;


wm = WidgetWithMeta();
WidgetWithMeta.metamethod();


# Passing Keyword Arguments
# class Reticulator(metaclass=TracingMeta, tension=496):
class Reticulator(metaclass=TracingMeta):

    def reticulate(self, spline):
        print(spline)

    cubic = True

rt = Reticulator();
Reticulator.metamethod();


###########################################################################################
class AtoZ(metaclass=EntriesMeta, num_entries=26):
    pass

a = AtoZ();
###########################################################################################
#__call__ is being invoked of metaclass where positional argument is not 
#acceptable
#ctk = ConstrainedToKeywords(23, 45, color='White')
ctk = ConstrainedToKeywords(color='White')
###########################################################################################

print(type(D))

print(type(C))
###########################################################################################

###########################################################################################

###########################################################################################

###########################################################################################

###########################################################################################

###########################################################################################

###########################################################################################
