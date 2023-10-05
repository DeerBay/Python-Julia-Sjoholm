class GeometryShapes:
    '''Has two subclasses, Circel, and Rectangel'''
    def __init__(self, x: (int|float), y:(int|float)):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The position for this geometrical shape is (x, y): ({self.x}, {self.y})."

    def __repr__(self):
        return f'"Shape"({self.x =}, {self.y=})'
    
