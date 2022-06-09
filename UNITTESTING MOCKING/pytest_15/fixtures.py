# WHAT ARE FIXTURES
"""
Software test fixtures initialize test functions. They provide a fixed baseline so
that tests execute reliably and produce consistent, repeatable, results.
Initialization may set up services, state, or other operating environments.
These are accessed by test functions through arguments; for each fixture used
by a test function there is typically a parameter (named after the fixture) in
the test function’s definition.
"""
import pytest


@pytest.fixture
def a():
    # initialization - NOTHING BUT THE DATABASE INITIALIZATION
    print("FIXTURE CALLED")
    return 10


@pytest.fixture
def b():
    # initialization - NOTHING BUT THE DATABASE INITIALIZATION
    print("FIXTURE CALLED")
    return 20


def test_multiply(a):  # using the decorator of fixture, you can use the fixture on your tests
    print("DATABASE RELATED CODE: ", str(a))


def test_divide(b):  # using the decorator of fixture, you can use the fixture on your tests
    print("DATABASE RELATED CODE: ", str(b))


def test_divide_with_two_fixtures(a, b):  # using the decorator of fixture, you can use the fixture on your tests
    print("DATABASE RELATED CODE: ", str(a, b))


@pytest.fixture(autouse=True)
def for_all():
    print("for all called")
