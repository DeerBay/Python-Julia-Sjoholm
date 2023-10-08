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
        '''Calcultate the area of the circle. Returns float.'''
        import numpy as np
        return np.pi * self.radius * self.radius

    def circumference(self):
        '''Calcultate the circumference of the circle. Returns float.'''
        import numpy as np
        return 2 * np.pi * self.radius

    def is_unit_circle(self):
        '''calculates the squared distance from the center of the circle to the origin. Then, the method checks if this squared distance is equal to 1. If it is, the circle is a unit circle; otherwise, it is not.'''
        distance_to_origin = (self.x - 0) ** 2 + (self.y - 0) ** 2
        if distance_to_origin == 1:
            print("This is a unit circle.")
        else:
            print("This is not a unit circle.")

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
