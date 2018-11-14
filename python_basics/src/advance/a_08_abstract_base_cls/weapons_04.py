from abc import ABC, abstractmethod


# Here Sword will be virtual base class
# ABCMeta required to implement 
class Sword(ABC): #metaclass is ABCMeta

    # This is same as your own custom meta class and overriding the issubclass and issubinstance
    @classmethod
    def __subclasshook__(cls, sub): 
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                and hasattr(sub, 'thrust') and callable(sub.thrust)
                and hasattr(sub, 'parry') and callable(sub.parry)
                and hasattr(sub, 'sharpen') and callable(sub.sharpen)) \
                or NotImplemented)
        
    @abstractmethod
    def thrust(self):
        print('Thrusting..')
    
    @abstractmethod   
    def swipe(self):
        raise NotImplementedError

    @abstractmethod
    def parry(self):
        raise NotImplementedError

class BroadSword(Sword):

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")
        
    def thrust(self):
        super().thrust(); #calling abstract method
    
    def parry(self):
        print('Parry..')


class SamuraiSword:

    def swipe(self):
        print("Slice!")

    def sharpen(self):
        print("Shink!")

