from geometry_shapes import GeometryShapes

class Rectangel(GeometryShapes):
    '''Class representing a rectangel'''
    def __init__(self, x: int | float, y: int | float, height: int|float, width: int|float):
        '''Initialize a rectangel with given x and y coordinates, height and width'''
        super().__init__(x, y)
        self.height = height
        self.width = width

    def __str__(self):
        '''Return a string representation of the rectangel'''
        return f"Rectangel: Postion (x, y): ({self.x, self.y}), Height: {self.height}, Width: {self.width}"
    
    def __repr__(self):
        '''Return a string representation for developers'''
        return f"Rectangel({self.x},{self.y},{self.height},{self.width})"

    def calculate_area(self):
        '''Calcultate the area of the rectangel'''
        return self.height * self.width
    
    def circumference(self):
        '''Calculate the circumference of the rectangel'''
        return self.height*2 + self.width*2
    
    def is_square(self):
        if self.height == self.width:
            return f"This rectangel is a square."
        else:
            return f"This rectangel is not a square."

    @property
    def height(self):
        '''Getter of height'''
        return self._height
    
    @height.setter
    def height(self, height):
        '''Setter of height, with error handling'''
        if not isinstance(height, (int|float)):
            raise TypeError(f"Value of height can only be numeric. You wrote {height}.")
        elif height <= 0:
            raise ValueError(f"Height must be positive. You wrote {height}.")
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width: (int|float)):
        if not isinstance(width, (int|float)):
            raise TypeError(f"Value of Width can only be numeric. You wrote {width}.")
        elif width <= 0:
            raise ValueError(f"Width must be positive. You wrote {width}.")
        self._width = width