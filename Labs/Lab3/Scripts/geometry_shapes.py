class GeometryShapes:
    '''Base class for geometrical shapes'''
    def __init__(self, x: (int|float), y:(int|float)):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The position for this geometrical shape is (x, y): ({self.x}, {self.y})."

    def __repr__(self):
        return f'"Shape"({self.x =}, {self.y=})'
    
    @property
    def x(self):
        return self._x   
   
    @x.setter
    def x(self, position: (int|float)):
        if not isinstance(position, (int|float)):
            raise TypeError(f"Position of x can only be numeric.")
        self._x = position

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, position: (int|float)):
        if not isinstance(position, (int|float)):
            raise TypeError(f"Position of y can only be numeric.")
        self._y = position
    
    '''Operator overloading'''

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