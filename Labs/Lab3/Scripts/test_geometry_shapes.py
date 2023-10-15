from geometry_shapes import GeometryShapes2D
from geometry_shapes import Circle
from geometry_shapes import Rectangle
from geometry_shapes import GeometryShapes3D
from geometry_shapes import Cube
from geometry_shapes import Sphere
import pytest

# Test for Geometyshapes2D class

def test_setup_GeometryShapes2D():
    """
    Test the GeometryShapes2D initialization to ensure it sets the expected values to x and y attribute.
    """
    shape = GeometryShapes2D(-1, 2.2)
    assert shape.x == -1
    assert shape.y == 2.2

def test_invalid_input_for_position():
    '''
    Test the GeometryShapes2D raises a TypeError when other than int or float are passed.
    '''
    with pytest.raises(TypeError):
        GeometryShapes2D(x="five", y=2)

    with pytest.raises(TypeError):
        GeometryShapes2D(5, "två")

def test_string_representaion_2D():
    '''
    Test the str and repr for GeometryShapes2D gives a string representation of the class.
    '''
    shape = GeometryShapes2D(1, 2)
    assert str(shape) == "The position for this 2D geometrical shape is (x, y): (1, 2)."
    assert repr(shape) == "GeometryShapes2D(1, 2)"

def test_valid_input_translate_xy():
    '''
    Test translate_xy method adds the input values to x and y
    '''
    shape = Rectangle(2, 0, 1, 1)
    shape.translate_xy(x=5, y=0)
    assert shape.x == 7
    assert shape.y == 0

def test_invalid_input_type_for_translate_xy():
    '''
    Test translate_xy method raises TypeError when other than int or float are passed.
    '''
    shape = Rectangle(2, 0, 1, 1)
    with pytest.raises(TypeError):
        shape.translate_xy("five", 0)

    with pytest.raises(TypeError):
        shape.translate_xy(1, "seven")
 
def test_comparison_operators_2D():
    '''
    Test comparison operators for shapes (Rectangle and/or Circle) objects based on their calculated areas.
    
    - Tests equality (==).
    - Tests inequality (!=).
    - Tests greater than (>).
    - Tests greater than or equal to (>=).
    - Tests less than (<).
    - Tests less than or equal to (<=).
    '''
    rectangle1 = Rectangle(1, 1, 2, 2)
    rectangel2 = Rectangle(2, 2, 1, 1)
    circle1 = Circle(1, 1, 1)
    circle2 = Circle(5, 5, 1)
    assert not rectangle1 == rectangel2
    assert circle1 == circle2
    assert not circle1 == rectangel2
    assert rectangle1 != rectangel2
    assert rectangle1 > rectangel2
    assert not rectangle1 < rectangel2
    assert rectangle1 >= rectangel2
    assert not rectangle1 <= rectangel2

# Test for Rectangle class

def test_setup_rectangle():
    """
    Test the Rectangle initialization to ensure it sets the expected values.
    """
    rectangle = Rectangle(1, 2, 4, 5)
    assert rectangle.x == 1
    assert rectangle.y == 2
    assert rectangle.height == 4
    assert rectangle.width == 5

def test_invalid_type_for_height_rectangle_rectangle():
    '''
    Test the Rectangle raises a TypeError when other than int or float are passed for attibute height.
    '''
    with pytest.raises(TypeError):
        Rectangle(2, 0, "five", 1)

def test_invalid_type_for_width_rectangle():
    '''
    Test the Rectangle raises a TypeError when other than int or float are passed for attibute width.
    '''
    with pytest.raises(TypeError):
        Rectangle(2, 0, 1, "seven")

def test_negative_value_height_rectangle():
    '''
    Test the Rectangle raises a ValueError when negative values are passed for attibute height.
    '''
    with pytest.raises(ValueError):
        Rectangle(2, 0, -1, 1)

def test_negative_value_width_rectangle():
    '''
    Test the Rectangle raises a ValueError when negative values are passed for attibute width.
    '''
    with pytest.raises(ValueError):
        Rectangle(2, 0, 1, -1)

def test_string_representaion_rectangle():
    '''
    Test the str and repr for Rectangle gives a string representation of the class.
    '''
    rectangle = Rectangle(1, 2, 3, 4)
    assert str(rectangle) == "Rectangle: Postion (x, y): (1, 2), Height: 3, Width: 4"
    assert repr(rectangle) == "Rectangle(1, 2, 3, 4)"

def test_area_rectangle():
    '''
    Test calculation for area attribute for Rectangle works as expected.
    ''' 
    rectangle = Rectangle(0, 0, 5, 5)
    assert rectangle.area == 25
    assert rectangle.area != 20

def test_circumference_rectangle():
    '''
    Test calculation for circumference attribute for Rectangle works as expected.
    ''' 
    rectangle = Rectangle(0, 0, 5, 5)
    assert rectangle.circumference == 20
    assert rectangle.circumference != 25

def test_is_square_rectangle():
    '''
    Test the is_square() method provides True when height and width are the same value.
    '''
    rectangle1 = Rectangle(0, 0, 4, 4)
    assert rectangle1.is_square() # True

def test_rectangle_is_not_square():
    '''
    Test the is_square() method provides False when height and width are not the same value.
    '''
    rectangle2 = Rectangle(0, 0, 5, 4)
    assert not rectangle2.is_square() # False

def test_is_point_inside_rectangle():
    '''
    Test is_point_inside() method provides True when point is inside rectangle.
    '''
    rectangle1 = Rectangle(0, 0, 10, 10)
    assert rectangle1.is_point_inside(1.2, 3.2) # True
    assert not rectangle1.is_point_inside(6, 6) # False
    
# Test for Circle class

def test_valid_input_for_setup_circle():
    """
    Test the Circle initialization to ensure it sets the expected values.
    """
    circle = Circle(1, 2, 4)
    assert circle.x == 1
    assert circle.y == 2
    assert circle.radius == 4

def test_invalid_type_for_radius_circle():
        '''
        Test the Circle raises a TypeError when other than int or float are passed for attibute radius.
        '''
        with pytest.raises(TypeError):
            Circle(2, 0, "minus ett")

def test_negative_value_for_radius_circle():
    '''
    Test the Circle raises a ValueError when negative values are passed for attibute radius.
    '''
    with pytest.raises(ValueError):
        Circle(2, 0, -1)
   
def test_string_representation_circle():
    '''
    Test the str and repr for Circle gives a string represenatation of the class.
    '''
    circle = Circle(1, 2, 3)
    assert str(circle) == "Circle: Postion (x, y): (1, 2), Radius: 3."
    assert repr(circle) == "Circle(1, 2, 3)"

def test_area_circle():
    '''
    Test calculation for area attribute for Circle works as expected.
    '''
    circle = Circle(1, 3, 5)
    assert circle.area == 78.54
    assert circle.area != 78

def test_circumference_circle():
    '''
    Test calculation for circumference attribute for Circle works as expected.
    '''
    circle = Circle(1, 3, 6)
    assert circle.circumference == 37.69911184307752
    assert circle.circumference != 0
    
def test_is_unit_circle():
    '''
    Test the is_unit_circle() method provides True when x=0, y=0, radius=1.
    '''
    circle1 = Circle(0, 0, 1)
    assert circle1.is_unit_circle() == True

def test_is_not_unit_circle():
    '''
    Test the is_unit_circle() method provides False when NOT x=0, y=0, radius=1.
    '''
    circle2 = Circle(0, 0, 2)
    assert circle2.is_unit_circle() == False

def test_is_point_inside_circle():
    '''
    Test is_point_inside() method provides True when point is inside circle and False otherwise.
    '''
    circle = Circle(0, 0, 2)
    assert circle.is_point_inside(1, 1) == True
    assert circle.is_point_inside(5, 10) == False

# Test for GeometryShapes3D class
def test_setup_GeometryShapes3D():
    """
    Test the GeometryShapes3D initialization to ensure it sets the expected values to x, y and z attribute.
    """
    shape = GeometryShapes3D(-1, 2.2, -10)
    assert shape.x == -1
    assert shape.y == 2.2
    assert shape.z == -10

def test_invalid_input_for_position():
    '''
    Test the GeometryShapes3D raises a TypeError when other than int or float are passed.
    '''
    with pytest.raises(TypeError):
        GeometryShapes2D(x="five", y=2, z=0)

    with pytest.raises(TypeError):
        GeometryShapes2D(x=0, y="seven", z=0)

    with pytest.raises(TypeError):
        GeometryShapes2D(x=0, y=2, z="eight")

def test_string_representaion_3D():
    '''
    Test the str and repr for GeometryShapes3D gives a
    string representation of the class.
    '''
    shape = GeometryShapes3D(1, 2, 0)
    assert str(shape) == "The position for this 3D geometrical shape is (x, y, z): (1, 2, 0)."
    assert repr(shape) == "GeometryShapes3D(1, 2, 0)"

def test_translate_xyz_3D():
    '''
    Test translate_xyz method adds the input values to x, y and z
    '''
    shape = Cube(2, 0, 1, 1)
    shape.translate_xyz(x=1, y=1, z=1)
    assert shape.x == 3
    assert shape.y == 1
    assert shape.z == 2

def test_invalid_input_translate_xyz_3D():
    '''
    Test translate_xy method raises TypeError when other than int or float are passed.
    '''
    shape = Sphere(0, 0, 0, 1)
    with pytest.raises(TypeError):
        shape.translate_xyz("one", 0, 0)
    
    with pytest.raises(TypeError):
        shape.translate_xyz(1, 1, "five")


def test_comparison_operators_3D():
    '''
    Test comparison operators for shapes (Cube and/or Sphere) objects based on their calculated volumes.
    
    - Tests equality (==).
    - Tests inequality (!=).
    - Tests greater than (>).
    - Tests greater than or equal to (>=).
    - Tests less than (<).
    - Tests less than or equal to (<=).
    '''
    cube_1 = Cube(1, 1, 2, 1)
    cube_2 = Cube(2, 2, 1, 2)
    sphere_1 = Sphere(1, 1, 1, 1)
    sphere_2 = Sphere(5, 5, 1, 1)
    assert not cube_1 == cube_2
    assert sphere_2 == sphere_1
    assert not cube_1 == sphere_1
    assert cube_1 != cube_2
    assert cube_2 > cube_1
    assert cube_2 >= cube_1
    assert not sphere_2 < sphere_1
    assert not sphere_1 <= cube_1

# Test for Cube class

def test_setup_cube():
    """
    Test the Cube initialization to ensure it sets the expected values.
    """
    cube = Cube(1, 2, 4, 5)
    assert cube.x == 1
    assert cube.y == 2
    assert cube.z == 4
    assert cube.side_length == 5

def test_invalid_type_for_side_length_cube():
    '''
    Test the Cube raises a TypeError when other than int or float are passed for attibute side length.
    '''
    with pytest.raises(TypeError):
        Cube(2, 0, 0, "five")

def test_negative_value_side_length_cube():
    '''
    Test the Cube raises a ValueError when negative values are passed for attibute side length.
    '''
    with pytest.raises(ValueError):
        Cube(2, 0, -1, -1)

def test_string_representation_cube():
    '''
    Test the str and repr for Cube gives a string representation of the class.
    '''
    cube = Cube(1, 2, 3, 4)
    assert str(cube) == "Cube: Position (x, y, z): (1, 2, 3), Side length: 4."
    assert repr(cube) == "Cube(1, 2, 3, 4)"

def test_volume_cube():
    '''
    Test calculation for volume attribute for cube.
    '''
    cube = Cube(1, 1, 1, 10)
    assert cube.volume == 1000

def test_surface_area_cube():
    '''
    Test calculation for surface area attribute cube.
    '''
    cube = Cube(1, 1, 1, 10)
    assert cube.surface_area == 600

def test_is_point_inside_cube():
    '''
    Test is_point_inside() method provides True when point inside cube  and False otherwise.
    '''
    my_cube = Cube(1,1,1,5)
    assert my_cube.is_point_inside(1.2, 1.5, 1.7) # True
    assert not my_cube.is_point_inside(5.1, 5.4, 1) # False


# test for Sphere class

def test_setup_sphere():
    """
    Test the Sphere initialization to ensure it sets the expected values.
    """
    sphere = Sphere(1, 2, 3, 4)
    assert sphere.x == 1
    assert sphere.y == 2
    assert sphere.z == 3
    assert sphere.radius == 4

def test_invalid_type_for_radius_sphere():
    '''
    Test the sphere raises a TypeError when other than int or float are passed for attibute radius.
    '''
    with pytest.raises(TypeError):
        Sphere(2, 0, 0, "five")

def test_negative_value_radius_sphere():
    '''
    Test the sphere raises a ValueError when negative values are passed for attibute radius.
    '''
    with pytest.raises(ValueError):
        Sphere(2, 0, -1, -1)

def test_string_representation_sphere():
    '''
    Test the str and repr for Sphere gives a string representation of the class.
    '''
    sphere = Sphere(1, 2, 3, 4)
    assert str(sphere) == "Sphere: Position (x, y, z): (1, 2, 3), Radius: 4."
    assert repr(sphere) == "Sphere(1, 2, 3, 4)"

def test_volume_sphere():
    '''
    Test calculation for volume attribute for sphere.
    '''
    sphere = Sphere(1, 1, 1, 10)
    assert sphere.volume == 4188.790204786391

def test_surface_area_sphere():
    '''
    Test calculation for surface area attribute sphere.
    '''
    sphere = Sphere(1, 1, 1, 10)
    assert sphere.surface_area == 1256.64

def test_is_point_inside_sphere():
    '''
    Test is_point_inside() method provides True when point inside sphere and False otherwise.
    '''
    my_sphere = Sphere(0, 0, 0, 10)
    assert my_sphere.is_point_inside(2,2,2) # True
    assert not my_sphere.is_point_inside(11,11,11) # False

def test_is_unit_sphere():
    '''
    Test is_unit_sphere method provides True when radius == 1 and False otherwise.
    '''
    enhets_sfär = Sphere(1,1,1,1) # unit sphere
    ej_enhets_sfär = Sphere(0, 0, 0, 3)
    assert enhets_sfär.is_unit_sphere() # True, radius =1
    assert not ej_enhets_sfär.is_unit_sphere() # False

