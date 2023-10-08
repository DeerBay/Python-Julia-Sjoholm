from geometry_shapes import GeometryShapes

class Circle(GeometryShapes):
    def __init__(self, x: int | float, y: int | float, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        '''Return a string representation of the rectangle'''
        return f"Circle: Postion (x, y): ({self.x, self.y}), Radius: {self.radius}."
    
    def __repr__(self):
        '''Return a string representation for developers'''
        return f"Circle({self.x}, {self.y}, {self.radius})"
    
    def calculate_area(self):
        pass

    def circumference():
        pass

    def is_unit_circle():
        pass

    def is_point_inside():
        pass

    @property
    def radius(self):
        '''Getter of radius'''
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        '''Setter of height. Only positive numeric values is valid input.'''
        if not isinstance(radius, (int, float)):
            raise TypeError(f"Value of height can only be numeric. You wrote '{height}'.")
        elif radius <= 0:
            raise ValueError(f"Height must be positive. You wrote {height}.")
        self._radius = radius
