class GeometryShapes:
    '''Base class for geometrical shapes'''
    def __init__(self, x: (int|float), y:(int|float)):
        '''Initalize a position with given x and y coordinates for a geometrical shape'''
        self.x = x
        self.y = y

    def __str__(self):
        '''Return a position for a gemetrical shape'''
        return f"The position for this geometrical shape is (x, y): ({self.x}, {self.y})."

    def __repr__(self):
        '''Return a string for developers'''
        return f"GeometryShapes({self.x =}, {self.y=})"
    
    def translate(self, x_move_units: (int, float), y_move_units: (int, float)):
        '''Method for moving a geometry shapes coordinates (ex. translate(1, 1)) move x and y one unit.'''
        if not isinstance(x_move_units, (int, float)) or not isinstance(y_move_units, (int, float)):
            raise TypeError("x_move_units and y_move_units must be numeric values (int or float).")
        self.x += x_move_units
        self.y += y_move_units
        print(f"The new coordinates for the center of the object is = ({self.x},{self.y})")
    
    @property
    def x(self):
        '''Getter of x'''
        return self._x   
   
    @x.setter
    def x(self, x):
        '''Setter of x, with error handling'''
        if not isinstance(x, (int, float)):
            print(f"Position of x can only be numeric. You wrote: {x}.")
            raise TypeError("Position of x can only be numeric (GeometryShapes(x, y))")
        self._x = x

    @property
    def y(self):
        '''Getter of y'''
        return self._y
    
    @y.setter
    def y(self, y):
        '''Setter of y, with error handling'''
        if not isinstance(y, (int, float)):
            print(f"Position of y can only be numeric. You wrote: {y}.")
            raise TypeError(f"Position of y can only be numeric (GeometryShapes(x, y)).")
        self._y = y
    
    def __eq__(self, other):
        '''Operator overload for equal.'''
        return self.calculate_area() == other.calculate_area()

    def __ne__(self, other):
        '''Operator overload for not equal.'''
        return self.calculate_area() != other.calculate_area()
    
    def __gt__(self, other):
        '''Operator overload for greater than.'''
        return self.calculate_area() > other.calculate_area()
    
    def __lt__(self, other):
        '''Operator overload for less than.'''
        return self.calculate_area() < other.calculate_area()
    
    def __ge__(self, other):
        '''Operator overload for greater than or equal to.'''
        return self.calculate_area() >= other.calculate_area()
    
    def __le__(self, other):
        '''Operator overload for less than or equal to.'''
        return self.calculate_area() <= other.calculate_area()


class Rectangle(GeometryShapes):
    '''Class representing a rectangle'''
    def __init__(self, x: int | float, y: int | float, height: int|float, width: int|float):
        '''Initialize a rectangle with given x and y coordinates, height and width.'''
        super().__init__(x, y)
        self.height = height
        self.width = width

    def __str__(self):
        '''Return a string representation of the rectangle'''
        return f"Rectangle: Postion (x, y): {self.x, self.y}, Height: {self.height}, Width: {self.width}"
    
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


class Circle(GeometryShapes):
    '''Class representation of circle'''
    def __init__(self, x: int | float, y: int | float, radius):
        '''Initialize a circle with given x and y coordinates and radius.'''
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        '''Return a string representation of the rectangle'''
        return f"Circle: Postion (x, y): {self.x, self.y}, Radius: {self.radius}."
    
    def __repr__(self):
        '''Return a string representation for developers'''
        return f"Circle({self.x}, {self.y}, {self.radius})"
    
    def calculate_area(self):
        '''Calcultate the area of the circle. Returns float.'''
        import numpy as np
        area = np.pi * self.radius* self.radius
        return round(area, 2)

    def circumference(self):
        '''Calcultate the circumference of the circle. Returns float.'''
        import numpy as np
        return 2 * np.pi * self.radius

    def is_unit_circle(self):
        '''Checks if the circle is a unit circle with center at (0, 0) and radius of 1.'''
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else: 
            return False

    def is_point_inside(self, point_x: (int, float), point_y: (int, float)):
        '''Checks if point (point_x, point_y) is inside circle. Returns bool (True/False).'''
        distance_to_point = (self.x - point_x)**2 + (self.y - point_y)**2
        return distance_to_point <= self.radius**2

    @property
    def radius(self):
        '''Getter of radius'''
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        '''Setter of Radius. Only positive numeric values is valid input.'''
        if not isinstance(radius, (int, float)):
            raise TypeError(f"Value of radius can only be numeric. You wrote '{radius}'.")
        elif radius <= 0:
            raise ValueError(f"Radius must be positive. You wrote '{radius}'.")
        self._radius = radius