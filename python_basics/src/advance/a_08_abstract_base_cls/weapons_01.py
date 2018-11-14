class SordMeta(type):

    def __subclasscheck__(self, sub):
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and hasattr(sub, 'sharpen') and callable(sub.sharpen))
        
    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance));


# Here Sword will be virtual base class
class Sword(metaclass=SordMeta):

    def thrust(self):
        print('Thrusting..')


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
