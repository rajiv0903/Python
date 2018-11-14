

def my_class_decorator(cls):
    for name, attr in vars(cls).items():  # @UnusedVariable
        print(name)
    return cls

@my_class_decorator        
class Temperature:

    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, value):
        self._kelvin = value

    
