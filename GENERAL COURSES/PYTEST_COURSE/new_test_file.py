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

# --------- Asserting with the assert statement
def function_to_test(x):
    result = x * 3
    return result

def test_function_to_test():
    assert function_to_test(4) == 12
    assert function_to_test(5) == 15
    assert function_to_test != 0


# -------- Assertions about expecting EXCEPTIONS
@pytest.mark.xfail
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0 # this test doesn't pass

"""
# -------- Matching exception error
def function_to_raise_error():
    raise ValueError("Exception 456 raised")


def test_match_the_exception():
    with pytest.raises(ValueError, match=r".* 456 .*"):
        function_to_raise_error() """


# --------- Making use of context-sensitive comparisons
def test_set_comparison():
    res1 = set("1414")
    res2 = set("2020")
    assert res1 != res2

def test_set_comparison():
    res1 = set("1010")
    res2 = set("1010")
    assert res1 == res2


# https://docs.pytest.org/en/6.2.x/fixture.html