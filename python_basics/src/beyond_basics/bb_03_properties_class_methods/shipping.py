'''
Created on Aug 21, 2018

@author: rajiv
'''


class ShippingContainer:
    
    next_serial = 1337  # This is class attribute - Shared across all instances
    
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial;
        ShippingContainer.next_serial += 1;
        return result;
    
    @classmethod
    def get_next_serial_cls(cls):
        result = cls.next_serial;
        cls.next_serial += 1;
        return result;
    
    # class method to create instance
    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs);
    
    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, list(items), *args, **kwargs);
    
    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code;  # These are instance attributes
        self.lenght_ft = length_ft;
        self.contents = contents; 
        self.serial = ShippingContainer.get_next_serial_cls();
        
    @staticmethod
    def _polymorphic_test():
        print('Base Class')

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.lenght_ft

    @property
    def volume_ft3(self):
        return self._calc_volume()
      
        
class RefrigeratedShippingContainer(ShippingContainer):

    # We can set this property outside
    MAX_CELCIUS = 4.0
    
    FRIDGE_VALUME_FT3 = 100
    
    @staticmethod
    def _polymorphic_test():
        print('Child Class')
        
    @staticmethod
    def _c_to_f(celcius):
        return celcius * 9 / 5 + 32;
    
    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9 ;
        
    def __init__(self, owner_code, length_ft, contents, celcius):
        # Call Super Method: Explicit is better than implicit
        super().__init__(owner_code, length_ft, contents);
        # Calling the set property and getting the value check free
        self.celcius = celcius;
        
    @property
    def celcius(self):
        return self._celcius;
    
    # Define Celcius setter 

    def _set_celcius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELCIUS:
            raise ValueError('Temperature too hot!')
        self._celcius = value

    @celcius.setter
    def celcius(self, value):
        self._set_celcius(value)
        
    @property
    def fahrenheight(self):
        return RefrigeratedShippingContainer._c_to_f(self.celcius);
    
    @fahrenheight.setter
    def fahrenheight(self, value):
        self._celcius = RefrigeratedShippingContainer._f_to_c(value);
        
    # Overriding volume_ft3 formula
    # @property
    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VALUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    
    MIN_CELCIUS = -20.0
    
    @RefrigeratedShippingContainer.celcius.setter
    def celcius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELCIUS:
            raise ValueError('Temperature too cold!');
        # Unfortunately it is not possible
        # super()._celcius = value;  # let the max temperature to be validated by super class
        RefrigeratedShippingContainer.celcius.fset(self, value)


s = ShippingContainer('MCA', 3, [1, 2, 3])
s._polymorphic_test();
print(s.volume_ft3);
print(s.serial);

r = RefrigeratedShippingContainer.create_with_items('MCA', 5, [1, 2, 3], 4)
r.MAX_CELCIUS = 12  # Violation
print(r.celcius)
r.celcius = 2;  # We cannot set the property celcius.setter decorator
print(r.volume_ft3);

h = HeatedRefrigeratedShippingContainer.create_with_items('MCA', 5, [1, 2, 3], -20)
print(h.celcius)

