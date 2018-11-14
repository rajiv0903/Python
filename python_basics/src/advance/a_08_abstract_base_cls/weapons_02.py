from abc import ABCMeta


# Here Sword will be virtual base class
# ABCMeta required to implement 
class Sword(metaclass=ABCMeta):

    def thrust(self):
        print('Thrusting..')

    # This is same as your own custom meta class and overriding the issubclass and issubinstance
    @classmethod
    def __subclasshook__(cls, sub): 
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and hasattr(sub, 'sharpen') and callable(sub.sharpen))


class BroadSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")


class SamuraiSword:

    def swipe(self):
        print("Slice!")

    def sharpen(self):
        print("Shink!")


class Rifle:

    def fire(self):
        print("Bang!")
