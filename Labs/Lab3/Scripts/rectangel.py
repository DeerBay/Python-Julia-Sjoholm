from geometry_shapes import GeometryShapes

class Rectangel(GeometryShapes):
    def __init__(self, x: int | float, y: int | float, height: int|float, width: int|float):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width
    
    def circumference(self):
        return self.height*2 + self.width*2

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height: (int|float)):
        if not isinstance(height, (int|float)):
            raise TypeError(f"value of height can only be numeric.")
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width: (int|float)):
        if not isinstance(width, (int|float)):
            raise TypeError(f"value of Width can only be numeric.")
        self._width = width