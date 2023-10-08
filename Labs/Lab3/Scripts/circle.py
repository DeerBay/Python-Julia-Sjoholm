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