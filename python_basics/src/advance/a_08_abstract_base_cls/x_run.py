'''
Created on Nov 9, 2018
@author: rajiv
'''
from collections.abc import MutableSequence
from collections.abc import Sized, Hashable
from pprint import pprint
from advance.a_08_abstract_base_cls.weapons_01 import \
                Sword as S1, \
                BroadSword as BS1, \
                SamuraiSword as SS1, \
                Rifle as R1
from advance.a_08_abstract_base_cls.weapons_02 import \
                Sword as S2, \
                BroadSword as BS2, \
                SamuraiSword as SS2, \
                Rifle as R2
from advance.a_08_abstract_base_cls.virtual_class_registration import \
                Text, Prose
from advance.a_08_abstract_base_cls.weapons_03 import \
                Sword as S3, \
                BroadSword as BS3, \
                SamuraiSword as SS3, \
                Rifle as R3, \
                LightSaber as LS3
from advance.a_08_abstract_base_cls.weapons_04 import \
                BroadSword as BS4, \
                SamuraiSword as SS4
from advance.a_08_abstract_base_cls.datadescriptors import AbstractBaseClass
###########################################################################################
'''
List is sub class of MutableSequence
But List has only one Base Class i.e. built in object 
So MutableSequence check __subclasscheck__(sub) of ABCMeta- This is virtual base class 
'''
print(issubclass(list, MutableSequence))
pprint(list.mro())  # MutableSequence is not coming in hierarchy

###########################################################################################
print(issubclass(BS1, S1))
print(issubclass(SS1, S1))
print(issubclass(R1, S1))

ss1 = SS1()
print(isinstance(ss1, S1))


###########################################################################################
# We can make class which will be subclass of Sized
class SizedCollection:

    def __init__(self, size):
        self._size = size;

    def __len__(self):  # Sized - We need to override this method 
        return self._size;


print(issubclass(SizedCollection, Sized))
###########################################################################################
# If C is subclass of B and B is subclass of A then - it is not mandatory 
# that C is subclass of A- Below example list is mutable and overlooked the hash
print(issubclass(object, Hashable))
print(issubclass(list, object))
print(issubclass(list, Hashable))
print(object.__hash__)
print(list.__hash__)
###########################################################################################
# We can not invoke the virtual base class method 
bs1 = BS1()
print(bs1.swipe())
# print(bs1.thrust()) #It will throw error
print(BS1.__mro__)  # @UndefinedVariable
###########################################################################################
# We can use standard library ABCs for base class check- __subclasshook__
print(issubclass(BS2, S2))
print(issubclass(SS2, S2))
print(issubclass(R2, S2))

ss2 = SS2()
print(isinstance(ss2, S2))
###########################################################################################
# Virtual class registration using ABC Meta
print(issubclass(str, Text))
print(isinstance('Hello Rajiv!', Text));
print(issubclass(Prose, Text))
print(issubclass(str, Prose))
###########################################################################################
# Virtual Base Class Registration - __subclasshook__ took precedence over register
print(issubclass(BS3, S3))
print(issubclass(SS3, S3))
print(issubclass(R3, S3))
print(issubclass(LS3, S3))  # We need to check Not Implemented as well
###########################################################################################
# Abstract method has to be implemented is super class is declared 
bs4 = BS4();
bs4.thrust();
bs4.parry();

# SamuraiSword we can still instantiated because of NotImplemented at __subclasshook__
ss4 = SS4();
ss4.sharpen();
###########################################################################################
# If we develop method descriptors we need to override the property __isabstractmethod__
# Inspect the property 
print(AbstractBaseClass.abstract_property.__isabstractmethod__);  # @UndefinedVariable
print(AbstractBaseClass.concrete_property.__isabstractmethod__);  # @UndefinedVariable
###########################################################################################

###########################################################################################
