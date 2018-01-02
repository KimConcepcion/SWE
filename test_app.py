
from Mycalc import add
from Mycalc import subtract
from Mycalc import multiply
from Mycalc import divide

def test_add():
	assert add(4, 4) == 8
	assert add(22, 10) == 32

def test_subtract():
	assert subtract(10, 5) == 5
	assert subtract(7, 1) == 6

def test_multiply():
	assert multiply(9, 9) == 81
	assert multiply(7, 6) == 42

def test_divide():
	assert divide(10, 5) == 2
	assert divide(90, 10) == 9
