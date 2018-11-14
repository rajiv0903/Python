from abc import ABC, abstractmethod


class DataDescriptor(ABC):

    @abstractmethod
    def __get__(self, instance, owner):
        print("DataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))

    @abstractmethod
    def __set__(self, instance, value):
        print("DataDescriptor.__set__({!r}, {!r}, {!r})"
              .format(self, instance, value))
    
    @abstractmethod  
    def __delete__(self, instance):
        pass
    
    @property
    def __isabstractmethod__(self): #Required to make this Data Descriptor to be abstract
        return True

    
# Read Only
class NonDataDescriptor(ABC):

    @abstractmethod
    def __get__(self, instance, owner):
        print("NonDataDescriptor.__get__({!r}, {!r}, {!r})"
              .format(self, instance, owner))


class AbstractBaseClass(ABC):
    
    @property
    @abstractmethod
    def abstract_property(self):
        raise NotImplementedError
    
    @property
    def concrete_property(self):
        return 'sand. cement, water'
