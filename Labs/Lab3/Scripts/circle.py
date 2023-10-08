from geometry_shapes import GeometryShapes

class Circle(GeometryShapes):
    '''Class representation of circle'''
    def __init__(self, x: int | float, y: int | float, radius):
        '''Initialize a circle with given x and y coordinates and radius.'''
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        '''Return a string representation of the rectangle'''
        return f"Circle: Postion (x, y): ({self.x, self.y}), Radius: {self.radius}."
    
    def __repr__(self):
        '''Return a string representation for developers'''
        return f"Circle({self.x}, {self.y}, {self.radius})"
    
    def calculate_area(self):
        '''Calcultate the area of the circle. Returns float.'''
        import numpy as np
        return np.pi * self.radius * self.radius

    def circumference(self):
        '''Calcultate the circumference of the circle. Returns float.'''
        import numpy as np
        return np.pi * self.radius**2

    def is_unit_circle(self):
        '''Checks if the circle is a unit circle with center at (0, 0) and radius of 1.'''
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else: 
            return False

    def is_point_inside(self, point_x: (int, float), point_y: (int, float)):
        '''Checks if point (point_x, point_y) is inside circle. Returns bool (True/False).'''
        distance_to_point = (self.x - point_x)**2 + (self.y - point_y)**2
        if distance_to_point <= self.radius**2:
            print(f"The point({point_x},{point_y}) is inside the circle.")
        else:
            print(f"The point({point_x},{point_y}) is not inside the circle.")

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
