# USING MARKERS - XFAIL
"""There will be scenarios that you wanna to scape
- xfail - if the test is marked as xfail - then the test is executed but not considered in final result of execution.
@pytest.mark.xfail
Is helpful if you are expecting a test case to fail already
- skip -
"""
import pytest
from .app import add, multiply, divide


@pytest.mark.xfail  # this test will be executed but it will be passed
def test_add():
    assert add(10, 20) == 30


def test_multiply():
    assert multiply(10, 20) == 200


def test_divide():
    assert divide(20, 10) == 2
