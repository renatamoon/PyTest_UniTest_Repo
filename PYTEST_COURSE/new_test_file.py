from re import X
from signal import raise_signal
from black import assert_equivalent
import pytest

""" DOCUMENTATION: https://docs.pytest.org/en/6.2.x/contents.html
FIRST DOC -> https://docs.pytest.org/en/6.2.x/getting-started.html#create-your-first-test
doing these tests accordingly to the documentation"""

"""
# --------- first steps

# function to be tested
def sum(x):
    return x * 2


# test function
def test_if_a_number_is_equals_to_another(): # passed
    assert function(5) == 10
    assert function(10) != 0


# test if it raises an exception
def function_to_raise_exception():
    raise SystemExit(1)

def test_function_a_as_my_test(): # passed
    with pytest.raises(SystemExit):
        function_to_raise_exception()

"""
# --------- group multiple tests in a class

class TestingClass:
    def test_one(self):
        x = "renata"
        assert "r" in x

    # mark to assure that the test is gonna fail
    @pytest.mark.xfail    
    def test_two(self):
        y = "ola"
        assert hasattr(y, "check") # this test hasn't passed cause y is not equals to check


# --------- Detailed summary report
@pytest.fixture
def fixture_error():
    assert 0

def test_return_ok():
    x = "OK"
    assert x == "OK"

def test_error(error_fixture):
    pass