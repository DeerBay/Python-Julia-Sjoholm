from geometry_shapes import GeometryShapes
from circel import Circel
from rectangel import Rectangel
import pytest

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

'''Test of operator overload is in tests for Circel and Rectangel'''

def test_equal():
   pass
