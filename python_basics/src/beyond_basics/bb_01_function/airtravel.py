'''
Created on Aug 8, 2018
@author: rajiv
'''


class Flight:
    
    '''
    Initialization method - must be __intin - this is not a constructor
    Actual constructor is provided by Python Run time Environment
    '''
    
    """ A flight with particular passenger aircraft- SN9888"""
    
    def __init__(self, number, aircraft):
        
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        
        if not (number[2:].isdigit()  and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))
        
        self._number = number; 
        self._aircraft = aircraft;
        
        '''
        Seating plan
        '''
        rows, seats = aircraft.seating_plan()  # It will return Tuple (range(1, 23), 'ABCDEF')
        # Initialize with None using underscore means not interested 
        self._seating = [None] + [ {letter: None for letter in seats} for _ in rows]
    
    def number(self):
        return self._number;
    
    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft.model();
    
    def _parse_seat(self, seat):
        
        row_numbers, seat_letters = self._aircraft.seating_plan();

        letter = seat[-1];  # Give me from list counting from right
        
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        
        row_text = seat[:-1]  # Give me not including the last one
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        
        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))
        
        return row , letter;
    
    def allocate_seat(self, seat, passenger):
        """Allocate a seat to passenger
        Args:
            seat: A seat designator such as 12C, 21F etc
            passenger: Name of the passenger
        Raises:
            ValueError is seat is not available
        """
        row , letter = self._parse_seat(seat);
        
        if self._seating[row][letter] is not None:
            raise ValueError("Seat already occupied {}".format(seat))
        
        self._seating[row][letter] = passenger;
        
    def relocate_passenger(self, from_seat, to_seat):
        
        from_row, from_letter = self._parse_seat(from_seat);
        
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate to seat {}".format(from_seat))
        
        to_row, to_letter = self._parse_seat(to_seat)
        
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))
        
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
        
    def num_available_seats(self):
        return sum (
            sum(1 for s in row.values() if s is None)
            for row in self._seating
            if row is not None  # Why None Check Because we assign first Dummy row as None
            )

        
class Aircraft:
    
    def model(self):
        return self._model;
    
    def registration(self):
        return self._registration;
    
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration;
        self._model = model;
        self._num_rows = num_rows;
        self._num_seats_per_row = num_seats_per_row;
        
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                  "ABCDEFGHJK"[:self._num_seats_per_row]);


# Polymorphism
class AircraftBase:
    
    def __init__(self, registration):
        self._registration = registration;
        
    def registration(self):
        return self._registration;
    
    def num_seats(self):
        rows, row_seats = self.seating_plan();
        return len(rows) * len(row_seats);

    
class AirbusA319(AircraftBase):  # Extend
    
    def model(self):
        return "Airbus A319"
    
    def seating_plan(self):
        return (range (1, 22), "ABCDEF")

                  
class Boeing777(AircraftBase):
    
    def model(self):
        return "Boeing 777"
    
    def seating_plan(self):
        return (range (1, 56), "ABCDEGHJK")


def make_flight():
    a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6);
    f = Flight('SN9888', a);
    f.allocate_seat("12A", "P 1")
    f.allocate_seat("15F", "P 2")
    f.allocate_seat("15E", "P 3")
    f.allocate_seat("1C", "P 4")
    f.allocate_seat("1D", "P 5")
    return f;

        
def make_flights():
    a = AirbusA319("G-EUPT");
    f = Flight('BA758', a);
    
    b = Boeing777("F-GSPC");
    g = Flight("AF72", b);
    
    return f, g;
