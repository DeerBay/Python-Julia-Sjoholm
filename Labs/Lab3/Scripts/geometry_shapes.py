class GeometryShapes:
    '''Has two subclasses, Circel, and Rectangel'''
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
        return self.y
    
    @y.setter
    def x(self, position: (int|float)):
        if not isinstance(position, (int|float)):
            raise TypeError(f"Position of x can only be numeric.")
        self._x = position
    
    '''Operator overloading'''

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area
    
    def __gt__(self, other):
        return self.area > other.area
    
    def __lt__(self, other):
        return self.area < other.area
    
    def __ge__(self, other):
        return self.area >= other.area
    
    def __le__(self, other):
        return self.area <= other.area