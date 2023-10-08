from geometry_shapes import GeometryShapes

class Rectangle(GeometryShapes):
    '''Class representing a rectangle'''
    def __init__(self, x: int | float, y: int | float, height: int|float, width: int|float):
        '''Initialize a rectangle with given x and y coordinates, height and width.'''
        super().__init__(x, y)
        self.height = height
        self.width = width

    def __str__(self):
        '''Return a string representation of the rectangle'''
        return f"Rectangle: Postion (x, y): ({self.x, self.y}), Height: {self.height}, Width: {self.width}"
    
    def __repr__(self):
        '''Return a string representation for developers'''
        return f"Rectangle({self.x},{self.y},{self.height},{self.width})"

    def calculate_area(self):
        '''Calcultate the area of the rectangle. Return float.'''
        return self.height * self.width
    
    def circumference(self):
        '''Calculate the circumference of the rectangle. Returns float.'''
        return self.height*2 + self.width*2
    
    def is_square(self):
        '''Checks if the rectangel is a square.'''
        if self.height == self.width:
            return f"This rectangle is a square."
        else:
            return f"This rectangle is not a square."
        
    def is_point_inside(self, point_x: (int, float), point_y: (int, float)):
        '''Checks if point (point_x, point_y) is inside rectangle. Returns bool (True/False).'''
        left_boundary = self._x - self.width/2
        right_boundary = self._x + self.width/2
        top_boundary =  self._y + self.height/2
        bottom_boundary = self._y - self.height/2

        return left_boundary <= point_x <= right_boundary and  bottom_boundary <= point_y <= top_boundary

    @property
    def height(self):
        '''Getter of height'''
        return self._height
    
    @height.setter
    def height(self, height):
        '''Setter of height. Only positive numeric values is valid input.'''
        if not isinstance(height, (int, float)):
            raise TypeError(f"Value of height can only be numeric. You wrote '{height}'.")
        elif height <= 0:
            raise ValueError(f"Height must be positive. You wrote {height}.")
        self._height = height

    @property
    def width(self):
        '''Getter of width'''
        return self._width
    
    @width.setter
    def width(self, width: (int, float)):
        '''Setter of width. Only positive numeric values is valid input.'''
        if not isinstance(width, (int, float)):
            raise TypeError(f"Value of width can only be numeric. You wrote '{width}'.")
        elif width <= 0:
            raise ValueError(f"Width must be positive. You wrote {width}.")
        self._width = width