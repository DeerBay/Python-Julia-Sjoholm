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
        return f'"GeometryShapes"({self.x =}, {self.y=})'
    
    @property
    def x(self):
        '''Getter of x'''
        return self._x   
   
    @x.setter
    def x(self, position: (int|float)):
        '''Setter of x, with error handling'''
        if not isinstance(position, (int|float)):
            raise TypeError(f"Position of x can only be numeric.")
        self._x = position

    @property
    def y(self):
        '''Getter of y'''
        return self._y
    
    @y.setter
    def y(self, position: (int|float)):
        '''Setter of y, with error handling'''
        if not isinstance(position, (int|float)):
            raise TypeError(f"Position of y can only be numeric.")
        self._y = position
    
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