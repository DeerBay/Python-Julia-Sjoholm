class GeometryShapes2D:
    '''Base class for a 2D geometrical shape'''
    def __init__(self, x: (int|float), y:(int|float)):
        '''
        Initalize a position with given x and y coordinates for a geometrical shapes centerpoint.
        Only numric values are accepted.
        '''
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            '''Raises TypeError if type other than int or float'''
            raise TypeError("Coordinates (x, y) must be numeric.")
        self._x = x
        self._y = y

    def __str__(self):
        '''
        Return a position for a 2D gemetrical shape
        '''
        return f"The position for this geometrical shape is (x, y): ({self.x}, {self.y})."

    def __repr__(self):
        '''
        Return a string for developers
        '''
        return f"GeometryShapes2D({self.x=}, {self.y=})"

    @property
    def x(self):
        '''
        Getter of x
        '''
        return self._x   

    @property
    def y(self):
        '''
        Getter of y
        '''
        return self._y

    @property
    def area(self):
        return None
    
    @property
    def circumference(self):
        return None
    
    def translate_xy(self, x: (int, float), y: (int, float)):
        '''
        Method for moving a geometry shapes coordinates 
        (ex. translate(1, 1)) move x and y one unit.
        '''
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numeric values (int or float).")
        self._x += x
        self._y += y
    
    # Operator overlad for compairson of area 2D 
    def __eq__(self, other):
        '''
        Operator overload for equal.
        '''
        return self.area == other.area

    def __ne__(self, other):
        '''
        Operator overload for not equal.
        '''
        return self.area != other.area
    
    def __gt__(self, other):
        '''
        Operator overload for greater than.
        '''
        return self.area > other.area
    
    def __lt__(self, other):
        '''
        Operator overload for less than.
        '''
        return self.area < other.area
    
    def __ge__(self, other):
        '''
        Operator overload for greater than or equal to.
        '''
        return self.area >= other.area
    
    def __le__(self, other):
        '''
        Operator overload for less than or equal to.
        '''
        return self.area <= other.area


class Rectangle(GeometryShapes2D):
    '''
    Class representing a rectangle
    '''
    def __init__(self, x: int | float, y: int | float, height: int|float, width: int|float):
        '''
        Initialize a rectangle with given x and y coordinates, height and width.
            Only numreic values are accepted and positive numeric values for height and width.
        '''
        super().__init__(x, y)
        if not isinstance(height, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError(f"Value of height and width can only be numeric. You wrote '{height, width}'.")
        elif height <= 0 or width <= 0:
            raise ValueError(f"Height and width must be positive. You wrote {height, width}.")
        self._height = height
        self._width = width

    def __str__(self):
        '''
        Return a string representation of the rectangle
        '''
        return f"Rectangle: Postion (x, y): {self.x, self.y}, Height: {self.height}, Width: {self.width}"
    
    def __repr__(self):
        '''
        Return a string representation of the rectangle for developers
        '''
        return f"Rectangle({self.x=},{self.y=},{self.height=},{self.width=})"
    
    @property
    def height(self):
        '''
        Getter of rectangle height
        '''
        return self._height

    @property
    def width(self):
        '''
        Getter of rectangle width
        '''
        return self._width

    @property
    def area(self):
        '''
        Getter of area of the rectangle. Return float.
        '''
        return self._height * self._width
    
    @property
    def circumference(self):
        '''
        Getter of circumference of the rectangle. Return float.
        '''
        return self._height*2 + self._width*2
    
    def is_square(self):
        '''
        Checks if the rectangel is a square.
            Returns bool (True/False).
        '''
        return self._height == self._width
        
    def is_point_inside(self, x: (int, float), y: (int, float)):
        '''
        Checks if coordinate (x, y) is inside rectangle object. 
            Returns bool (True/False).
            Only numeric values are accepted.
        '''
        return self._x - self._width/2 <= x <= self._x + self._width/2 and  self._y - self._height/2 <= y <= self._y + self._height/2

class Circle(GeometryShapes2D):
    '''
    Class representation of circle
    '''
    def __init__(self, x: int | float, y: int | float, radius):
        '''
        Initialize a circle with given x and y coordinates and radius.
            Only numeric values are accepted and positive numric values for radius
        '''
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError(f"Value of radius can only be numeric. You wrote '{radius}'.")
        elif radius <= 0:
            raise ValueError(f"Radius must be positive. You wrote '{radius}'.")
        self._radius = radius

    def __str__(self):
        '''
        Return a string representation of the rectangle
        '''
        return f"Circle: Postion (x, y): {self.x, self.y}, Radius: {self.radius}."
    
    def __repr__(self):
        '''
        Return a string representation for developers
        '''
        return f"Circle({self.x=}, {self.y=}, {self.radius=})"
    
    @property
    def radius(self):
        '''
        Getter of circle radius.
        '''
        return self._radius

    @property
    def circumference(self):
        '''
        Getter of circumference of the circle. Returns float.
        '''
        import numpy as np
        return 2 * np.pi * self._radius
    
    @property
    def area(self):
        '''
        Calcultate the area of the circle. Returns float.
        '''
        import numpy as np
        area = np.pi * self._radius* self._radius
        return round(area, 2)
    
    def is_unit_circle(self):
        '''
        Checks if the circle is a unit circle with center at (0, 0) and radius of 1.
        '''
        return self._radius == 1 and self._x == 0 and self.y == 0

    def is_point_inside(self, x: (int, float), y: (int, float)):
        '''Checks if point (x, y) is inside circle. 
            Returns bool (True/False).  
        '''
        distance_to_point = (self._x - x)**2 + (self._y - y)**2
        return distance_to_point <= self._radius**2 # Compares with squared radius for optimization.

    
class GeometryShapes3D:
    '''
    Base class for 3D geometrical shapes
    '''
    def __init__(self, x: (int|float), y:(int|float), z:(int|float)):
        '''
        Initalize a position with given x, y and z coordinates for a 3D geometrical shapes centerpoint.
        Only numeric values are accepted.
        '''
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
            '''
            Raises TypeError if type other than int or float
            '''
            raise TypeError("Coordinates (x, y, z) must be numeric.")
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        '''
        Return a string representation for the 3D geometrical shape.
        '''
        return f"The position for this 3D geometrical shape is (x, y, z): ({self.x}, {self.y}, {self.z})."

    def __repr__(self):
        '''
        Return a string representation for developers.
        '''
        return f"GeometryShapes3D({self.x=}, {self.y=}, {self.z=})"
    
    @property
    def x(self):
        '''
        Getter of x
        '''
        return self._x   

    @property
    def y(self):
        '''
        Getter of y
        '''
        return self._y
    
    @property
    def z(self):
        '''
        Getter of z
        '''
        return self._z
    
    @property
    def volume(self):
        return None
    
    def translate_xyz(self, x: (int, float), y: (int, float), z: (int|float)):
        '''
        Method for moving a geometry shapes coordinates 
        (ex. translate(1, 1, 1)) move x, y and z one unit.
        Only numric values are accepted.
        '''
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"x and y and z must be numeric values (int or float). You wrote '({x},{ y}, {z})'.")
        self._x += x
        self._y += y
        self._z += z

    # Operator overloading for compairson of volume
    def __eq__(self, other):
        '''
        Operator overload for equal. Compares volume.
        '''
        return self.volume == other.volume

    def __ne__(self, other):
        '''
        Operator overload for not equal. Compares volume.
        '''
        return self.volume != other.volume
    
    def __gt__(self, other):
        '''
        Operator overload for greater than. Compares volume.
        '''
        return self.volume > other.volume
    
    def __lt__(self, other):
        '''
        Operator overload for less than. Compares volume.
        '''
        return self.volume < other.volume
    
    def __ge__(self, other):
        '''
        Operator overload for greater than or equal to. Compares volume.
        '''
        return self.volume >= other.volume
    
    def __le__(self, other):
        '''
        Operator overload for less than or equal to. Compares volume.
        '''
        return self.volume <= other.volume

class Cube(GeometryShapes3D):
    def __init__(self, x: int | float, y: int | float, z: int | float, side_length: (int|float)):
        '''
        Initalize a cube with given x, y and z coordinates and side length.
        Only numeric values are accepted and positive values for side length.
        '''
        super().__init__(x, y, z)
        if not isinstance(side_length, (int, float)):
            raise TypeError(f"Value of length can only be numeric. You wrote '{side_length}'.")
        elif side_length <= 0:
            raise ValueError(f"Side length must be positive. You wrote '{side_length}'.")
        self._side_length = side_length

    def __str__(self):
        '''
        Return a string representation of the cube.
        '''
        return f"Cube: Postion (x, y, z): {self.x, self.y, self.z}, Length: {self.side_length}."
    
    def __repr__(self):
        '''
        Return a string representation of the cube for developers.
        '''
        return f"Cube({self._x}, {self._y}, {self._z}, {self.side_length})"

    @property
    def side_length(self):
        '''
        Getter of cube side length
        '''
        return self._side_length

    @property
    def volume(self):
        '''
        Getter of volume for the cube. Return float.
        '''
        return self._side_length ** 3
    
    @property
    def surface_area(self):
        '''
        Getter of the surface area for the cube. Returns float.
        '''
        return 6 * self.side_length ** 2
    
    def is_point_inside(self, x: (int, float), y: (int, float), z: (int|float)):
        '''
        Checks if coordinate (x, y, z) is inside cube. 
        Returns bool (True/False).
        Only numeric values are accepted.
        '''
        half_side_length = self._side_length/2
        return self._x - half_side_length <= x <= self._x + half_side_length and self._y - half_side_length <= y <= self._y + half_side_length and self._z - half_side_length <= z <= self._z + half_side_length

    class Sphere(GeometryShapes3D):
        def __init__(self, x: int | float, y: int | float, z: int | float, radius: (int|float)):
            '''
            Initalize a sphere with given x, y and z coordinates and radius.
            Only numeric values are accepted and positive values for radius.
            '''
            super().__init__(x, y, z)
            if not isinstance(radius, (int|float)):
                raise TypeError(f"Value of radius can only be numeric. You wrote '{radius}'.")
            elif radius <= 0:
                raise ValueError(f"Radius must be positive. You wrote '{radius}'.")
            self._radius = radius

        def __str__(self):
            '''
            Return a string representation of the sphere.
            '''
            return f"Cube: Position (x, y, z): {self.x, self.y, self.z}, Radius: {self.radius}."
        
        def __repr__(self):
            '''
            Return a string representation for developers.
            '''
            return  f"Sphere({self._x}, {self._y}, {self._z}, {self._radius})"
        
        @property
        def radius(self):
            '''
            Getter of sphere radius
            '''
            return self._radius
        
        @property
        def volume(self):
            '''
            Getter of volume for the sphere.
            return float.
            '''
            import numpy as np
            return (4/3) * np.pi * self.radius ** 3
       
        @property
        def surface_area(self):
            '''
            Getter of surface area for the sphere. 
            Returns a rounded float of two decimals.
            '''
            import numpy as np
            surface_area = 4 * np.pi * self._radius**2
            return round(surface_area, 2)
        
        def is_unit_sphere(self):
            '''
            Checks if the sphere is a unit sphere.
            '''
            return self._radius == 1
        
        def is_point_inside(self, x: (int, float), y: (int, float), z: (int|float)):
            '''
            Checks if point (x, y, z) is inside sphere. 
            Returns bool (True/False).
            Only numeric values are accepted.
            '''
            distance_to_point = (self._x - x)**2 + (self._y - y)**2 + (self._z - z)**2
            return distance_to_point <= self._radius**2 # Compares with squared radius for optimization.
