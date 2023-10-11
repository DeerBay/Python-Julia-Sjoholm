from geometry_shapes import GeometryShapes
from geometry_shapes import Circle
from geometry_shapes import Rectangle
import pytest

# Test for Geometyshapes class

def test_valid_input_for_setup():
    shape = GeometryShapes(-1, 2.2)
    assert shape.x == -1
    assert shape.y == 2.2

def test_invalid_input_for_position():
    with pytest.raises(TypeError) as exc_info:
        shape = GeometryShapes("fem", 2)
        assert str(exc_info.value) == "Position of x can only be numeric (GeometryShapes(x, y))"

    with pytest.raises(TypeError) as exc_info:
        shape = GeometryShapes(5, "två")
        assert str(exc_info.value) == "Position of x can only be numeric (GeometryShapes(x, y))"

def test_string_representaion():
    shape = GeometryShapes(1, 2)
    assert str(shape) == "The position for this geometrical shape is (x, y): (1, 2)."
    assert repr(shape) == "GeometryShapes(self.x =1, self.y=2)"

def test_valid_input_translate():
    shape = Rectangle(2, 0, 1, 1)
    shape.translate(5, 0)
    assert shape.x == 7
    assert shape.y == 0

def test_invalid_input_type_for_translate():
    shape = Rectangle(2, 0, 1, 1)
    with pytest.raises(TypeError) as exc_info:
        shape.translate("fem", 0)
    assert str(exc_info.value) == "x_move_units and y_move_units must be numeric values (int or float)."

    with pytest.raises(TypeError) as exc_info:
        shape.translate(1, "sju")
    assert str(exc_info.value) == "x_move_units and y_move_units must be numeric values (int or float)."

    with pytest.raises(TypeError) as exc_info:
        shape.translate("fem", "sju")
    assert str(exc_info.value) == "x_move_units and y_move_units must be numeric values (int or float)."

def test_comparison_operators():
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

def test_string_representaion_rectangle():
    rectangle = Rectangle(1, 2, 3, 4)
    assert str(rectangle) == "Rectangle: Postion (x, y): (1, 2), Height: 3, Width: 4"
    assert repr(rectangle) == "Rectangle(1,2,3,4)"

def test_valid_input_for_setup_rectangle():
    rectangle = Rectangle(1, 2, 4, 5)
    assert rectangle.x == 1
    assert rectangle.y == 2
    assert rectangle.height == 4
    assert rectangle.width == 5

def test_invalid_input_type_for_height():
    with pytest.raises(TypeError) as exc_info:
        shape = Rectangle(2, 0, "fem", 1)
    assert str(exc_info.value) == "Value of height can only be numeric. You wrote 'fem'."

def test_invalid_input_value_for_height_width():
    with pytest.raises(ValueError) as exc_info:
        shape = Rectangle(2, 0, -1, 1)
    assert str(exc_info.value) == "Height must be positive. You wrote -1."

    with pytest.raises(ValueError) as exc_info:
        shape = Rectangle(2, 0, 1, -1)
    assert str(exc_info.value) == "Width must be positive. You wrote -1."

    with pytest.raises(TypeError) as exc_info:
        shape = Rectangle(2, 0, "minus ett", 1)
    assert str(exc_info.value) == "Value of height can only be numeric. You wrote 'minus ett'."

    with pytest.raises(TypeError) as exc_info:
        shape = Rectangle(2, 0, 1, "minus ett")
    assert str(exc_info.value) == "Value of width can only be numeric. You wrote 'minus ett'."


def test_rectangle_calculate_area():
        rectangle = Rectangle(0, 0, 5, 5)
        assert rectangle.calculate_area() == 25
        assert rectangle.calculate_area() != 20

def test_rectangle_circumference():
    rectangle = Rectangle(0, 0, 5, 5)
    assert rectangle.circumference() == 20
    assert rectangle.circumference() != 25

def test_rectangle_is_square():
    rectangle1 = Rectangle(0, 0, 4, 4)
    rectangle2 = Rectangle(0, 0, 5, 4)
    assert rectangle1.is_square() == "This rectangle is a square."
    assert rectangle2.is_square() == "This rectangle is not a square."

def test_is_point_inside_rectangle():
    rectangle1 = Rectangle(0, 0, 10, 10)
    assert rectangle1.is_point_inside(1.2, 3.2) == True
    assert rectangle1.is_point_inside(6, 6) == False
    
# Test for Circle class
    
def test_string_representation_circle():
    circle = Circle(1, 2, 3)
    assert str(circle) == "Circle: Postion (x, y): (1, 2), Radius: 3."
    assert repr(circle) == "Circle(1, 2, 3)"

def test_valid_input_for_setup_circle():
    circle = Circle(1, 2, 4)
    assert circle.x == 1
    assert circle.y == 2
    assert circle.radius == 4

def test_invalid_input_value_for_radius():
    with pytest.raises(ValueError) as exc_info:
        circle = Circle(2, 0, -1)
    assert str(exc_info.value) == "Radius must be positive. You wrote '-1'."

    with pytest.raises(TypeError) as exc_info:
        shape = Circle(2, 0, "minus ett")
    assert str(exc_info.value) == "Value of radius can only be numeric. You wrote 'minus ett'."

def test_calculate_area_circle():
    circle = Circle(1, 3, 5)
    assert circle.calculate_area() == 78.54

def test_circumference_circle():
    circle = Circle(1, 3, 6)
    assert circle.circumference() == 37.69911184307752
    
def test_is_unit_circle():
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(0, 0, 2)
    assert circle1.is_unit_circle() == True
    assert circle2.is_unit_circle() == False

def test_is_point_inside_circle():
    circle = Circle(0,0, 2)
    assert circle.is_point_inside(1, 1) == True
    assert circle.is_point_inside(5, 10) == False

