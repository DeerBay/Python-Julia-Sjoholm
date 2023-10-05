class GeometryShapes:
    '''Has two subclasses, Circel, and Rectangel'''t
    def __init__(self, x: (int|float), y:(int|float)):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The position for this geometrical shape is (x, y): ({self.x}, {self.y})."

    def __repr__(self):
        return f'"Shape"({self.x =}, {self.y=})'
    
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