from geometry_shapes import GeometryShapes
from circle import Circle
from rectangle import Rectangle
import pytest
'''Test of Geometyshapes class'''
def test_valid_input_for_setup():
    shape = GeometryShapes(1, 2)
    assert shape.x == 1
    assert shape.y == 2

def test_invalid_input_for_height():
    with pytest.raises(TypeError) as exc_info:
        shape = GeometryShapes("fem", 2)
    assert str(exc_info.value) == "Position of x can only be numeric (GeometryShapes(x, y))"

def test_string_representaion():
    shape = GeometryShapes(1, 2)
    assert str(shape) == "The position for this geometrical shape is (x, y): (1, 2)."
    assert repr(shape) == "GeometryShapes(self.x =1, self.y=2)"

def test_invalid_input_type_for_translate():
    with pytest.raises(TypeError) as exc_info:
        shape = Rectangle(2, 0, 1, 1)
        shape.translate("fem", 0)
    assert str(exc_info.value) == "x_move_units and y_move_units must be numeric values (int or float)."

'''Test of operator overload is in tests for Circel and Rectangle'''

'''Test of Rectangle class'''
def test_valid_input_for_setup_rectangle():
    shape = Rectangle(1, 2, 4, 5)
    assert shape.x == 1
    assert shape.y == 2

def test_invalid_input_type_for_height():
    with pytest.raises(TypeError) as exc_info:
        shape = Rectangle(2, 0, "fem", 1)
    assert str(exc_info.value) == "Value of height can only be numeric. You wrote 'fem'."

def test_invalid_input_value_for_height():
    with pytest.raises(ValueError) as exc_info:
        shape = Rectangle(2, 0, -1, 1)
    assert str(exc_info.value) == "Height must be positive. You wrote -1."

def test_invalid_input_type_for_widtht():
    with pytest.raises(TypeError) as exc_info:
        shape = Rectangle(2, 0, 1, "10")
    assert str(exc_info.value) == "Value of width can only be numeric. You wrote '10'."

def test_invalid_input_value_for_width():
    with pytest.raises(ValueError) as exc_info:
        shape = Rectangle(2, 0, 1, -1)
    assert str(exc_info.value) == "Width must be positive. You wrote -1."

