# ASSERTING EXCEPTIONS
import pytest


# pytest.raises() - function that will check if your assertion towards an exception is valid or invalid
def test_exception_example():
    with pytest.raises(ZeroDivisionError, match=r".* by1 .*") as exceptinfo:
        print(100 / 0)
    print(type(exceptinfo))
    print(exceptinfo.type)
    print(exceptinfo.value)
    print(exceptinfo.traceback)
