class GeometryShapes:
    '''Base class for geometrical shapes'''
    def __init__(self, x: (int|float), y:(int|float)):
        '''Initalize a position with given x and y coordinates for a geometrical shape'''
        self.x = x
        self.y = y

    def __str__(self):
        '''Return a position for a gemetrical shape'''
        return f"The position for this geometrical shape is (x, y): ({self.x}, {self.y})."

    def __repr__(self):
        '''Return a string for developers'''
        return f"GeometryShapes({self.x =}, {self.y=})"
    
    def translate(self, x_move_units: (int, float), y_move_units: (int, float)):
        '''Method for moving a geometry shapes coordinates (ex. translate(1, 1)) move x and y one unit.'''
        if not isinstance(x_move_units, (int, float)) or not isinstance(y_move_units, (int, float)):
            raise TypeError("x_move_units and y_move_units must be numeric values (int or float).")
        self.x += x_move_units
        self.y += y_move_units
        print(f"The new coordinates for the center of the object is = ({self.x},{self.y})")
    
    @property
    def x(self):
        '''Getter of x'''
        return self._x   
   
    @x.setter
    def x(self, x):
        '''Setter of x, with error handling'''
        if not isinstance(x, (int, float)):
            print(f"Position of x can only be numeric. You wrote: {x}.")
            raise TypeError("Position of x can only be numeric (GeometryShapes(x, y))")
        self._x = x

    @property
    def y(self):
        '''Getter of y'''
        return self._y
    
    @y.setter
    def y(self, y):
        '''Setter of y, with error handling'''
        if not isinstance(y, (int, float)):
            print(f"Position of y can only be numeric. You wrote: {y}.")
            raise TypeError(f"Position of y can only be numeric (GeometryShapes(x, y)).")
        self._y = y
    
    '''Operator overloading for equal, not equal, greater than, less than, greater or equal and less or equal for calculated areas.'''
    def __eq__(self, other):
        return self.calculate_area() == other.calculate_area()

    def __ne__(self, other):
        return self.calculate_area() != other.calculate_area()
    
    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()
    
    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()
    
    def __ge__(self, other):
        return self.calculate_area() >= other.calculate_area()
    
    def __le__(self, other):
        return self.calculate_area() <= other.calculate_area()