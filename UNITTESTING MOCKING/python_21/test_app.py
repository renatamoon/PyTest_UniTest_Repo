# PARAMETRIZE
import pytest
from .app import add


# parametrize allows us to pass the values that we want to use as parameters and also set an OUTPUT for it
# we can use it for a lot of parameters as we can see on the example. Also, different types of parameters;
@pytest.mark.parametrize("output, a, b", [
                             (30, 10, 20),
                             (300, 100, 200),
                             (3000, 1000, 2000)],
                         ids=["first", "second", "third"])
def test_add_parametrize(output, a, b):
    assert add(a, b) == output
