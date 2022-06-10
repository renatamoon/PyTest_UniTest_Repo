"""
SKIP MARKER: WHAT IS A SKIP MARKER?

- If a test is marked as skip then the test is not all executed

"""
import sys
import pytest
from ..app import add, divide


@pytest.mark.skip  # normal skipping
def test_add():
    print("Add executed")
    assert add(10, 20) == 30


# this is a skipping with reason then it will be printed
@pytest.mark.skip(reason="Just thought it is a good idea to skip this test")
def test_add():
    print("Add executed")
    assert add(10, 20) == 30


# this skip will be executed if the version is equal to 3, 7
@pytest.mark.skipif(sys.version_info > (3, 7), reason="Python version is not compatible")
def test_divide():
    assert divide(20, 10) == 2
