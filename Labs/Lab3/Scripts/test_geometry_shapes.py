from geometry_shapes import GeometryShapes2D
from geometry_shapes import Circle
from geometry_shapes import Rectangle
import pytest

# Test for Geometyshapes class

def test_setup_GeometryShapes2D():
    """Test the GeometryShapes2D initialization to ensure it sets the expected values to x and y attribute."""
    shape = GeometryShapes2D(-1, 2.2)
    assert shape.x == -1
    assert shape.y == 2.2

def test_invalid_input_for_position():
    '''Test the GeometryShapes2D2D raises a TypeError when other than int or float are passed.'''
    with pytest.raises(TypeError):
        GeometryShapes2D(x="fem", y=2)

    with pytest.raises(TypeError):
        GeometryShapes2D(5, "två")

def test_string_representaion():
    '''Test the str and repr for GeometryShapes2D2D gives a string represenatation of the class.'''
    shape = GeometryShapes2D(1, 2)
    assert str(shape) == "The position for this geometrical shape is (x, y): (1, 2)."
    assert repr(shape) == "GeometryShapes2D(self.x=1, self.y=2)"

def test_valid_input_translate_xy():
    '''Test translate_xy method adds the input values to x and y'''
    shape = Rectangle(2, 0, 1, 1)
    shape.translate_xy(x=5, y=0)
    assert shape.x == 7
    assert shape.y == 0

def test_invalid_input_type_for_translate_xy():
    '''Test translate_xy method raises TypeError when other than int or float are passed.'''
    shape = Rectangle(2, 0, 1, 1)
    with pytest.raises(TypeError):
        shape.translate_xy("fem", 0)

    with pytest.raises(TypeError):
        shape.translate_xy(1, "sju")
 
def test_comparison_operators():
    '''
    Test comparison operators for shapes (Rectangle and Circle) objects based on their calculated areas.
    
    - Tests equality (==) between rectangles and circles based on area.
    - Tests inequality (!=) between rectangles based on area.
    - Tests greater than (>) between rectangles based on area.
    - Tests greater than or equal to (>=) between rectangles based on area.
    - Tests less than (<) between rectangles based on area.
    - Tests less than or equal to (<=) between rectangles based on area.
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
    """Test the Rectangle initialization to ensure it sets the expected values."""
    rectangle = Rectangle(1, 2, 4, 5)
    assert rectangle.x == 1
    assert rectangle.y == 2
    assert rectangle.height == 4
    assert rectangle.width == 5

def test_invalid_type_for_height():
    '''Test the Rectangle raises a TypeError when other than int or float are passed for attibute height.'''
    with pytest.raises(TypeError):
        Rectangle(2, 0, "fem", 1)

def test_invalid_type_for_width():
    '''Test the Rectangle raises a TypeError when other than int or float are passed for attibute width.'''
    with pytest.raises(TypeError):
        Rectangle(2, 0, 1, "sju")

def test_negative_value_height():
    '''Test the Rectangle raises a ValueError when negative values are passed for attibute height.'''
    with pytest.raises(ValueError):
        Rectangle(2, 0, -1, 1)

def test_negative_value_width():
    '''Test the Rectangle raises a ValueError when negative values are passed for attibute width.'''
    with pytest.raises(ValueError):
        Rectangle(2, 0, 1, -1)

def test_string_representaion_rectangle():
    '''Test the str and repr for Rectangle gives a string represenatation of the class.'''
    rectangle = Rectangle(1, 2, 3, 4)
    assert str(rectangle) == "Rectangle: Postion (x, y): (1, 2), Height: 3, Width: 4"
    assert repr(rectangle) == "Rectangle(self.x=1,self.y=2,self.height=3,self.width=4)"

def test_rectangle_area():
        '''Test calculation for area attribute for Rectangle works as expected.''' 
        rectangle = Rectangle(0, 0, 5, 5)
        assert rectangle.area == 25
        assert rectangle.area != 20

def test_rectangle_circumference():
    '''Test calculation for circumference attribute for Rectangle works as expected.''' 
    rectangle = Rectangle(0, 0, 5, 5)
    assert rectangle.circumference == 20
    assert rectangle.circumference != 25

def test_rectangle_is_square():
    '''Test the is_square() method provides True when height and width are the same value.'''
    rectangle1 = Rectangle(0, 0, 4, 4)
    assert rectangle1.is_square() == True

def test_rectangle_is_not_square():
    '''Test the is_square() method provides False when height and width are not the same value.'''
    rectangle2 = Rectangle(0, 0, 5, 4)
    assert rectangle2.is_square() == False

def test_is_point_inside_rectangle():
    '''Test is_point_inside() method provides True when point is inside rectangle.'''
    rectangle1 = Rectangle(0, 0, 10, 10)
    assert rectangle1.is_point_inside(1.2, 3.2) == True

def test_is_point_not_inside_rectangle():
    '''Test is_point_inside() method provides False when point is not inside rectangle.'''
    rectangle1 = Rectangle(0, 0, 10, 10)
    assert rectangle1.is_point_inside(6, 6) == False
    
# Test for Circle class

def test_valid_input_for_setup_circle():
    """Test the Circle initialization to ensure it sets the expected values."""
    circle = Circle(1, 2, 4)
    assert circle.x == 1
    assert circle.y == 2
    assert circle.radius == 4

def test_invalid_type_for_radius():
        '''Test the Circle raises a TypeError when other than int or float are passed for attibute radius.'''
        with pytest.raises(TypeError):
            Circle(2, 0, "minus ett")

def test_negative_value_for_radius():
    '''Test the Circle raises a ValueError when negative values are passed for attibute radius.'''
    with pytest.raises(ValueError):
        Circle(2, 0, -1)
   
def test_string_representation_circle():
    '''Test the str and repr for Circle gives a string represenatation of the class.'''
    circle = Circle(1, 2, 3)
    assert str(circle) == "Circle: Postion (x, y): (1, 2), Radius: 3."
    assert repr(circle) == "Circle(self.x=1, self.y=2, self.radius=3)"

def test_area_circle():
    '''Test calculation for area attribute for Circle works as expected.'''
    circle = Circle(1, 3, 5)
    assert circle.area == 78.54
    assert circle.area != 78

def test_circumference_circle():
    '''Test calculation for circumference attribute for Circle works as expected.'''
    circle = Circle(1, 3, 6)
    assert circle.circumference == 37.69911184307752
    assert circle.circumference != 0
    
def test_is_unit_circle():
    '''Test the is_unit_circle() method provides True when x=0, y=0, radius=1.'''
    circle1 = Circle(0, 0, 1)
    assert circle1.is_unit_circle() == True

def test_is_not_unit_circle():
    '''Test the is_unit_circle() method provides False when NOT x=0, y=0, radius=1.'''
    circle2 = Circle(0, 0, 2)
    assert circle2.is_unit_circle() == False

def test_is_point_inside_circle():
    '''Test is_point_inside() method provides True when point is inside circle.'''
    circle = Circle(0,0, 2)
    assert circle.is_point_inside(1, 1) == True

def test_is_point_not_inside_circle():
    '''Test is_point_inside() method provides False when point is NOT inside circle.'''
    circle = Circle(0,0, 2)
    assert circle.is_point_inside(5, 10) == False


